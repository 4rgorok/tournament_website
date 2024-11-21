# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Arkusz(models.Model):
    iddojo = models.IntegerField(db_column='IdDojo', blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    weight = models.FloatField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    rank = models.CharField(db_column='Rank', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    kumitetxt = models.CharField(db_column='KumiteTxt', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    katatxt = models.CharField(db_column='KataTxt', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rok = models.IntegerField(db_column='Rok', blank=True, null=True)  # Field name made lowercase.
    miesiac = models.IntegerField(db_column='Miesiac', blank=True, null=True)  # Field name made lowercase.
    dzien = models.IntegerField(db_column='Dzien', blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    idrank = models.IntegerField(db_column='IdRank', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    kumite = models.BooleanField(db_column='Kumite')  # Field name made lowercase.
    kata = models.BooleanField(db_column='Kata')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Arkusz'


class Contestant(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idcountry = models.IntegerField(db_column='IdCountry', blank=True, null=True)  # Field name made lowercase.
    iddojo = models.IntegerField(db_column='IdDojo', blank=True, null=True)  # Field name made lowercase.
    contestantnumber = models.IntegerField(db_column='ContestantNumber', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    weight = models.IntegerField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    dob = models.DateTimeField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    t5 = models.BooleanField(db_column='T5')  # Field name made lowercase.
    kumite = models.BooleanField(db_column='Kumite')  # Field name made lowercase.
    kata = models.BooleanField(db_column='Kata')  # Field name made lowercase.
    idkatagroupt5 = models.IntegerField(db_column='IdKataGroupT5')  # Field name made lowercase.
    idkumitegroup = models.IntegerField(db_column='IdKumiteGroup')  # Field name made lowercase.
    idkatagroup = models.IntegerField(db_column='IdKataGroup')  # Field name made lowercase.
    sortingroup = models.IntegerField(db_column='SortInGroup')  # Field name made lowercase.
    verified = models.BooleanField(db_column='Verified')  # Field name made lowercase.
    idrank = models.IntegerField(db_column='IdRank')  # Field name made lowercase.
    kumiterank = models.IntegerField(db_column='KumiteRank')  # Field name made lowercase.
    katarank = models.IntegerField(db_column='KataRank')  # Field name made lowercase.
    judge = models.BooleanField(db_column='Judge')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Contestant'


class Country(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    countryname = models.CharField(db_column='CountryName', max_length=70, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Country'


class Dojo(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    dojoname = models.CharField(db_column='DojoName', max_length=150, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    dojoshort = models.CharField(db_column='DojoShort', max_length=30, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    contactname = models.CharField(db_column='ContactName', max_length=70, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=30, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=150, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=70, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    nip = models.CharField(db_column='NIP', max_length=20, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    pzk = models.BooleanField(db_column='PZK')  # Field name made lowercase.
    organization = models.CharField(db_column='Organization', max_length=70, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    dojolink = models.CharField(db_column='DojoLink', max_length=50, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    qty1 = models.IntegerField(db_column='Qty1')  # Field name made lowercase.
    qty2 = models.IntegerField(db_column='Qty2')  # Field name made lowercase.
    qty3 = models.IntegerField(db_column='Qty3')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dojo'


class Kata(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idtatami = models.IntegerField(db_column='IdTatami')  # Field name made lowercase.
    t5 = models.BooleanField(db_column='T5')  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    groupname = models.CharField(db_column='GroupName', max_length=150, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=150, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    matstatus = models.IntegerField(db_column='MatStatus')  # Field name made lowercase.
    stage = models.IntegerField(db_column='Stage')  # Field name made lowercase.
    kata5judge = models.BooleanField(db_column='Kata5Judge')  # Field name made lowercase.
    senior = models.BooleanField(db_column='Senior')  # Field name made lowercase.
    grouporder = models.IntegerField(db_column='GroupOrder')  # Field name made lowercase.
    printstatus = models.IntegerField(db_column='PrintStatus')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Kata'


class Katatournament(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idgroup = models.IntegerField(db_column='IdGroup')  # Field name made lowercase.
    idcontestant = models.IntegerField(db_column='IdContestant')  # Field name made lowercase.
    place = models.IntegerField(db_column='Place')  # Field name made lowercase.
    final = models.BooleanField(db_column='Final')  # Field name made lowercase.
    placeeliminations = models.IntegerField(db_column='PlaceEliminations')  # Field name made lowercase.
    pointseliminations = models.IntegerField(db_column='PointsEliminations')  # Field name made lowercase.
    pointseliminationsplusmin = models.IntegerField(db_column='PointsEliminationsPlusMin')  # Field name made lowercase.
    pointseliminationstotal = models.IntegerField(db_column='PointsEliminationsTotal')  # Field name made lowercase.
    placefinal = models.IntegerField(db_column='PlaceFinal')  # Field name made lowercase.
    pointsfinal = models.IntegerField(db_column='PointsFinal')  # Field name made lowercase.
    pointsfinalplusmin = models.IntegerField(db_column='PointsFinalPlusMin')  # Field name made lowercase.
    pointsfinaltotal = models.IntegerField(db_column='PointsFinalTotal')  # Field name made lowercase.
    disqualification = models.BooleanField(db_column='Disqualification')  # Field name made lowercase.
    j1 = models.IntegerField(db_column='J1')  # Field name made lowercase.
    j2 = models.IntegerField(db_column='J2')  # Field name made lowercase.
    j3 = models.IntegerField(db_column='J3')  # Field name made lowercase.
    j4 = models.IntegerField(db_column='J4')  # Field name made lowercase.
    j5 = models.IntegerField(db_column='J5')  # Field name made lowercase.
    j6 = models.IntegerField(db_column='J6')  # Field name made lowercase.
    j7 = models.IntegerField(db_column='J7')  # Field name made lowercase.
    f1 = models.IntegerField(db_column='F1')  # Field name made lowercase.
    f2 = models.IntegerField(db_column='F2')  # Field name made lowercase.
    f3 = models.IntegerField(db_column='F3')  # Field name made lowercase.
    f4 = models.IntegerField(db_column='F4')  # Field name made lowercase.
    f5 = models.IntegerField(db_column='F5')  # Field name made lowercase.
    f6 = models.IntegerField(db_column='F6')  # Field name made lowercase.
    f7 = models.IntegerField(db_column='F7')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    startorder = models.IntegerField(db_column='StartOrder')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KataTournament'


class Kumite(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idtatami = models.IntegerField(db_column='IdTatami')  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=1, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    weight = models.IntegerField(db_column='Weight')  # Field name made lowercase.
    groupname = models.CharField(db_column='GroupName', max_length=150, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=150, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    matstatus = models.IntegerField(db_column='MatStatus')  # Field name made lowercase.
    stage = models.IntegerField(db_column='Stage')  # Field name made lowercase.
    time1 = models.IntegerField(db_column='Time1')  # Field name made lowercase.
    time2 = models.IntegerField(db_column='Time2')  # Field name made lowercase.
    time3 = models.IntegerField(db_column='Time3')  # Field name made lowercase.
    timefinal = models.IntegerField(db_column='TimeFinal')  # Field name made lowercase.
    kumiteorder = models.IntegerField(db_column='KumiteOrder', unique=True)  # Field name made lowercase.
    g3 = models.BooleanField(db_column='G3')  # Field name made lowercase.
    senior = models.BooleanField(db_column='Senior')  # Field name made lowercase.
    printstatus = models.IntegerField(db_column='PrintStatus')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Kumite'


class Kumiteg3(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idgroup = models.IntegerField(db_column='IdGroup')  # Field name made lowercase.
    idcontestant = models.IntegerField(db_column='IdContestant')  # Field name made lowercase.
    place = models.IntegerField(db_column='Place')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KumiteG3'


class Kumitegroupsort(models.Model):
    contestantid = models.IntegerField(db_column='ContestantId', primary_key=True)  # Field name made lowercase.
    iddojo = models.IntegerField(db_column='IdDojo')  # Field name made lowercase.
    idkumitegroup = models.IntegerField(db_column='IdKumiteGroup')  # Field name made lowercase.
    kumiterank = models.IntegerField(db_column='KumiteRank')  # Field name made lowercase.
    dojoqty = models.IntegerField(db_column='DojoQty')  # Field name made lowercase.
    los = models.IntegerField(db_column='Los')  # Field name made lowercase.
    sortingroup = models.IntegerField(db_column='SortInGroup')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KumiteGroupSort'


class Kumitetournament(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    fightno = models.IntegerField(db_column='FightNo')  # Field name made lowercase.
    idgroup = models.IntegerField(db_column='IdGroup')  # Field name made lowercase.
    entityno = models.CharField(db_column='EntityNo', max_length=6, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    orderno = models.IntegerField(db_column='OrderNo')  # Field name made lowercase.
    level = models.IntegerField(db_column='Level')  # Field name made lowercase.
    leveltxt = models.CharField(db_column='LevelTxt', max_length=100, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    akaid = models.IntegerField(db_column='AkaId')  # Field name made lowercase.
    shiroid = models.IntegerField(db_column='ShiroId')  # Field name made lowercase.
    kumitestatus = models.IntegerField(db_column='KumiteStatus')  # Field name made lowercase.
    nextfightno = models.IntegerField(db_column='NextFightNo')  # Field name made lowercase.
    isnextaka = models.IntegerField(db_column='IsNextAka')  # Field name made lowercase.
    winner = models.IntegerField(db_column='Winner')  # Field name made lowercase.
    loser = models.IntegerField(db_column='Loser')  # Field name made lowercase.
    idtatami = models.IntegerField(db_column='IdTatami')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    g3 = models.BooleanField(db_column='G3')  # Field name made lowercase.
    nextentityno = models.CharField(db_column='NextEntityNo', max_length=6, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KumiteTournament'


class Organization(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    short = models.CharField(db_column='Short', max_length=25, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=250, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Organization'


class Rank(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    rank = models.CharField(db_column='Rank', max_length=50, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Rank'


class Role(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag')  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=50, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Role'


class Setup(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    minweightf = models.IntegerField(db_column='MinWeightF')  # Field name made lowercase.
    minagef = models.IntegerField(db_column='MinAgeF')  # Field name made lowercase.
    minweightm = models.IntegerField(db_column='MinWeightM')  # Field name made lowercase.
    minagem = models.IntegerField(db_column='MinAgeM')  # Field name made lowercase.
    contestantnumber = models.IntegerField(db_column='ContestantNumber')  # Field name made lowercase.
    kata5judge = models.BooleanField(db_column='Kata5Judge')  # Field name made lowercase.
    directedfights = models.BooleanField(db_column='DirectedFights')  # Field name made lowercase.
    fivetechniques = models.BooleanField(db_column='FiveTechniques')  # Field name made lowercase.
    tournament = models.CharField(db_column='Tournament', max_length=250, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    kumiteno = models.IntegerField(db_column='KumiteNo')  # Field name made lowercase.
    printfooter = models.CharField(db_column='PrintFooter', max_length=2500, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    announcement = models.CharField(db_column='Announcement', max_length=2500, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    printer = models.CharField(db_column='Printer', max_length=350, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    pdffolder = models.CharField(db_column='PdfFolder', max_length=350, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    printtofile = models.BooleanField(db_column='PrintToFile')  # Field name made lowercase.
    katarunda2 = models.IntegerField(db_column='KataRunda2')  # Field name made lowercase.
    tournamentdate = models.DateField(db_column='TournamentDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Setup'


class Tatami(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    isactivekumite = models.BooleanField(db_column='IsActiveKumite')  # Field name made lowercase.
    isactivekata = models.BooleanField(db_column='IsActiveKata')  # Field name made lowercase.
    stage = models.IntegerField(db_column='Stage')  # Field name made lowercase.
    prefix = models.CharField(db_column='Prefix', max_length=1, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    kumiteno = models.IntegerField(db_column='KumiteNo')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=150, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    issemifinalsactive = models.BooleanField(db_column='IsSemifinalsActive')  # Field name made lowercase.
    isfinalsactive = models.BooleanField(db_column='IsFinalsActive')  # Field name made lowercase.
    idcontestantkata = models.IntegerField(db_column='IdContestantKata')  # Field name made lowercase.
    idkumitetournament = models.IntegerField(db_column='IdKumiteTournament')  # Field name made lowercase.

    def save(self, *args, **kwargs):
        return

    def delete(self, *args, **kwargs):
        print("CWEL")
        self.active = False
        return
    
    def create(self, *args, **kwargs):
        print("CWE2L")
        self.active = False
        return
    
    def update(self, *args, **kwargs):
        print("CWEL3")
        self.active = False
        return

    class Meta:
        managed = False
        db_table = 'Tatami'


class User(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User'


class Websetup(models.Model):
    isactive = models.BooleanField(db_column='IsActive', primary_key=True)  # Field name made lowercase.
    akakey = models.CharField(db_column='AkaKey', max_length=50, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WebSetup'
