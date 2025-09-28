from django.urls import path

from AkaBackend.views import *

urlpatterns = [
    path("tatami", TatamiListView, name='tatami-list'),
    path("setup", SetupListView.as_view(), name='setup-list'),

    #path("kata", KataListView.as_view(), name='kata-list'), TODO kata całość
    path("kumite", KumiteListView.as_view(), name='kumite-list'),
    path("kumite/<int:id>", KumiteView.as_view(), name='kumite'),
    path("kumite/fight/<int:id>", KumiteFightView.as_view(), name='kumite-fight'),

    path("dojo", DojoListView.as_view(), name='dojo-list'),
    # id - dojo id
    path("dojo/<int:id>", DojoView.as_view(), name='dojo'),
    # id - fight id
    path("dojo/<int:id>/aka", DojoAkaView.as_view(), name='dojo-aka'),
    path("dojo/<int:id>/shiro", DojoShiroView.as_view(), name='dojo-shiro'),
    # id - contestant id
    path("dojo/contestant/<int:id>", DojoContestantView.as_view(), name='dojo'),
    
    path("fighters/<int:iddojo>", contestant_kumite_status_view, name='fighters-list'),


    path("contestants", ContestantListView.as_view(), name='contestant-list'),

    # id - contestant id
    path("contestant/<int:id>", ContestantView.as_view(), name='contestant'),
    # id - fight id
    path("contestant/<int:id>/aka", ContestantAkaView.as_view(), name='contestant-aka'),
    path("contestant/<int:id>/shiro", ContestantShiroView.as_view(), name='contestant-shiro'),
    
    path("kumitetournament/", KumitetournamentListView.as_view(), name='kumitetournament-list'),
    path("kumitetournament/<int:idgroup>", KumitetournamentGroupView.as_view(), name='kumitetournament-group'),
]