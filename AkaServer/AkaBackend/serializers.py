from rest_framework import serializers
from .models import *

class TatamiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tatami
        fields = "__all__"

class ContestantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contestant
        fields = "__all__"

class KataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kata
        fields = "__all__"

class KumiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kumite
        fields = "__all__"

class DojoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dojo
        fields = "__all__"

class SetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setup
        fields = "__all__"
