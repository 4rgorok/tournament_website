from rest_framework.views import APIView
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from django.db.models import Q, Prefetch
from django.http import JsonResponse
from .models import *
from .serializers import *

#class TatamiListView(generics.ListAPIView):
#    queryset = Tatami.objects.all().filter(isactive=True).select_related('idkumitetournament')
#    serializer_class = TatamiSerializer

class ContestantListView(generics.ListAPIView):
    queryset = Contestant.objects.all()
    serializer_class = ContestantSerializer

class FighterByDojoView(generics.ListAPIView):
    serializer_class = ContestantSerializer
    def get_queryset(self):
        iddojo = self.kwargs['iddojo']
        return Contestant.objects.filter(kumite = True).filter(iddojo=iddojo)

class ContestantView(generics.RetrieveAPIView):
    queryset = Contestant.objects.all()
    serializer_class = ContestantSerializer
    lookup_field = 'id'
    def get_object(self):
        contestant = super().get_object()
        return contestant

class ContestantAkaView(generics.RetrieveAPIView):
    queryset = Kumitetournament.objects.all()
    serializer_class = ContestantSerializer
    lookup_field = 'id'
    def get_object(self):
        contestant = super().get_object()
        return contestant.akaid

class ContestantShiroView(generics.RetrieveAPIView):
    queryset = Kumitetournament.objects.all()
    serializer_class = ContestantSerializer
    lookup_field = 'id'
    def get_object(self):
        contestant = super().get_object()
        return contestant.shiroid

class KumiteListView(generics.ListAPIView):
    queryset = Kumite.objects.all().order_by('kumiteorder')
    serializer_class = KumiteSerializer

class KumiteView(generics.RetrieveAPIView):
    queryset = Kumite.objects.all()
    serializer_class = KumiteSerializer
    lookup_field = 'id'
    def get_object(self):
        group = super().get_object()
        return group

class KumiteFightView(generics.RetrieveAPIView):
    queryset = Kumitetournament.objects.all()
    serializer_class = KumiteSerializer
    lookup_field = 'id'
    def get_object(self):
        group = super().get_object()
        return group.idgroup

class DojoListView(generics.ListAPIView):
    queryset = Dojo.objects.all()
    serializer_class = DojoSerializer

class DojoView(generics.RetrieveAPIView):
    queryset = Dojo.objects.all()
    serializer_class = DojoSerializer
    lookup_field = 'id'
    def get_object(self):
        dojo = super().get_object()
        return dojo

class DojoContestantView(generics.RetrieveAPIView):
    queryset = Contestant.objects.all()
    serializer_class = DojoSerializer
    lookup_field = 'id'
    def get_object(self):
        contestant = super().get_object()
        return contestant.iddojo

class DojoAkaView(generics.RetrieveAPIView):
    queryset = Kumitetournament.objects.all()
    serializer_class = DojoSerializer
    lookup_field = 'id'
    def get_object(self):
        fight = super().get_object()
        return fight.akaid.iddojo

class DojoShiroView(generics.RetrieveAPIView):
    queryset = Kumitetournament.objects.all()
    serializer_class = DojoSerializer
    lookup_field = 'id'
    def get_object(self):
        fight = super().get_object()
        return fight.shiroid.iddojo
    
class SetupListView(generics.ListAPIView):
    queryset = Setup.objects.all()
    serializer_class = SetupSerializer

class KumitetournamentListView(generics.ListAPIView):
    queryset = Kumitetournament.objects.all()
    serializer_class = KumitetournamentSerializer

class KumitetournamentGroupView(generics.ListAPIView):
    serializer_class = KumitetournamentSerializer
    def get_queryset(self):
        idgroup = self.kwargs['idgroup']
        return Kumitetournament.objects.filter(idgroup=idgroup)

def TatamiListView(request):
    tatamis = Tatami.objects.all().filter(isactive=True)
    result = []
    for tatami in tatamis:
        ktour = Kumitetournament.objects.filter(id=tatami.idkumitetournament_id)
        fight_no = -1
        if ktour:
            fight_no = int(ktour[0].orderno / 10)
        tatami_data = {
                'id': tatami.id,
                'isactive': tatami.isactive,
                'isactivekumite': tatami.isactivekumite,
                'isactivekata': tatami.isactivekata,
                'stage': tatami.stage,
                'prefix': tatami.prefix,
                'kumiteno': tatami.kumiteno,
                'description': tatami.description,
                'issemifinalsactive': tatami.issemifinalsactive,
                'isfinalsactive': tatami.isfinalsactive,
                'idcontestantkata': tatami.idcontestantkata_id,
                'idkumitetournament': tatami.idkumitetournament_id,
                'fightno' : fight_no, 
            }
        result.append(tatami_data)
    return JsonResponse(result, safe=False)


def contestant_kumite_status_view(request, iddojo):
    # Prefetch related kumite tournaments with status 0
    kumite_prefetch = Prefetch(
        'kumitetournament_set',
        queryset=Kumitetournament.objects.filter(kumitestatus=0),
        to_attr='active_kumite_aka'
    )
    
    kumite_prefetch_shiro = Prefetch(
        'kumitetournament_shiroid_set',
        queryset=Kumitetournament.objects.filter(kumitestatus=0),
        to_attr='active_kumite_shiro'
    )

    # Filter contestants by dojo ID
    contestants = Contestant.objects.filter(kumite=True).filter(iddojo=iddojo).prefetch_related(
        kumite_prefetch, kumite_prefetch_shiro
    )

    result = []
    for contestant in contestants:
        # Check if contestant has active kumite as aka
        aka_kumite = contestant.active_kumite_aka
        shiro_kumite = contestant.active_kumite_shiro
        kumite_data = None
        role = 'none'
        opponent = -1
        opponent_name = ""
        
        kumite_data = aka_kumite + shiro_kumite
        kumite_data.sort(key=lambda x: x.orderno)

        if not kumite_data:
            contestant_data = {
                'id': contestant.id,
                'iddojo': contestant.iddojo_id,
                'contestantnumber': contestant.contestantnumber,
                'gender': contestant.gender,
                'lastname': contestant.lastname,
                'firstname': contestant.firstname,
                'role': role,
                'opponent': opponent,
                'opponent_name': opponent_name,
            }
            result.append(contestant_data)
        else:
            for kumite in aka_kumite:
                opponent = kumite.shiroid_id
                if opponent != 0:
                    opponent_name = kumite.shiroid.firstname + " " + kumite.shiroid.lastname
                contestant_data = {
                    'id': contestant.id,
                    'iddojo': contestant.iddojo_id,
                    'contestantnumber': contestant.contestantnumber,
                    'gender': contestant.gender,
                    'lastname': contestant.lastname,
                    'firstname': contestant.firstname,
                    'role': "aka",
                    'opponent': opponent,
                    'opponent_name': opponent_name,
                    'fightno': kumite.fightno,
                    'idgroup_id': kumite.idgroup_id,
                    'entityno': kumite.entityno,
                    'orderno': kumite.orderno,
                    'kumite_id': kumite.id,
                    'level': kumite.leveltxt,
                    'g3':kumite.g3,
                }
                result.append(contestant_data)
            for kumite in shiro_kumite:
                opponent = kumite.akaid_id
                if opponent != 0:
                    opponent_name = kumite.akaid.firstname + " " + kumite.akaid.lastname
                contestant_data = {
                    'id': contestant.id,
                    'iddojo': contestant.iddojo_id,
                    'contestantnumber': contestant.contestantnumber,
                    'gender': contestant.gender,
                    'lastname': contestant.lastname,
                    'firstname': contestant.firstname,
                    'role': "shiro",
                    'opponent': opponent,
                    'opponent_name': opponent_name,
                    'fightno': kumite.fightno,
                    'idgroup_id': kumite.idgroup_id,
                    'entityno': kumite.entityno,
                    'orderno': kumite.orderno,
                    'kumite_id': kumite.id,
                    'level': kumite.leveltxt,
                    'g3':kumite.g3,
                }
                result.append(contestant_data)

    return JsonResponse(result, safe=False)