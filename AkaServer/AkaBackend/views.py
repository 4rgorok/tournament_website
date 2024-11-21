from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class TatamiListView(APIView):
    def get(self, request):
        items = Tatami.objects.all().filter(isactive=True)
        serializer = TatamiSerializer(items, many=True)
        return Response(serializer.data)
    
class ContestantListView(APIView):
    def get(self, request):
        items = Contestant.objects.all()
        if 'id' in request.GET:
            id=request.GET['id']
            items = Contestant.objects.all().filter(id=id)
        elif 'fid' in request.GET:
            fid = request.GET['fid']
            type = request.GET['type']
            uid = 0
            if type == '0':
                uid = Kumitetournament.objects.get(id=fid).akaid
            else:
                uid = Kumitetournament.objects.get(id=fid).shiroid
            items = Contestant.objects.filter(id=uid)
        serializer = ContestantSerializer(items, many=True)
        return Response(serializer.data)
    
class KataListView(APIView):
    def get(self, request):
        items = Kata.objects.all()

        if 'uid' in request.GET:
            uid = request.GET['uid']
            user = Contestant.objects.get(id=uid).idkatagroup
            items = Kata.objects.filter(id=user)
        elif 'id' in request.GET:
            id = request.GET['id']
            items = Kata.objects.all().filter(id=id)

        serializer = KataSerializer(items, many=True)
        return Response(serializer.data)
    
class KumiteListView(APIView):
    def get(self, request):
        items = Kumite.objects.all()

        if 'uid' in request.GET:
            uid = request.GET['uid']
            user = Contestant.objects.get(id=uid).idkumitegroup
            items = Kumite.objects.filter(id=user)
        elif 'fid' in request.GET:
            fid = request.GET['fid']
            fight = Kumitetournament.objects.get(id=fid).idgroup
            items = Kumite.objects.filter(id=fight)
        elif 'id' in request.GET:
            id = request.GET['id']
            items = Kumite.objects.all().filter(id=id)

        serializer = KumiteSerializer(items, many=True)
        return Response(serializer.data)
    
class DojoListView(APIView):
    def get(self, request):
        items = Dojo.objects.all()
        if 'fid' in request.GET:
            fid = request.GET['fid']
            type = request.GET['type']
            uid = 0
            if type == '0':
                uid = Kumitetournament.objects.get(id=fid).akaid
            else:
                uid = Kumitetournament.objects.get(id=fid).shiroid
            user = Contestant.objects.get(id=uid).iddojo
            items = Dojo.objects.filter(id=user)
        if 'uid' in request.GET:
            uid = request.GET['uid']
            user = Contestant.objects.get(id=uid).iddojo
            items = Dojo.objects.filter(id=user)
        elif 'id' in request.GET:
            id = request.GET['id']
            items = Dojo.objects.all().filter(id=id)

        serializer = DojoSerializer(items, many=True)
        return Response(serializer.data)
    
class SetupListView(APIView):
    def get(self, request):
        items = Setup.objects.all()
        serializer = SetupSerializer(items, many=True)
        return Response(serializer.data)