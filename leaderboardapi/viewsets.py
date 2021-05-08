
from rest_framework import viewsets
from . import models
from . import serializers

class leaderBoardViewset(viewsets.ModelViewSet):
    queryset = models.Leaderboarddetail.objects.all()
    serializer_class = serializers.leaderboardSerializer