from rest_framework import serializers
from .models import Leaderboarddetail

class leaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model= Leaderboarddetail
        fields= ['id','name','age','address','points']
