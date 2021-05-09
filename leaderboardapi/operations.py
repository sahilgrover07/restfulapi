from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import Leaderboarddetail
import json
from . import serializers
from django.http import JsonResponse, HttpResponse


@api_view(['GET', 'POST'])
def snippet_detail(request):
    """
    Retrieve, update or delete a code snippet.
    """
  
    if request.method == 'GET':
        queryset = Leaderboarddetail.objects.all()
        serializer = serializers.leaderboardSerializer(queryset, many=True)
        return JsonResponse(serializer.data,  safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.leaderboardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['DELETE'])
def delete(request, pk):
    try:
        queryset = Leaderboarddetail.objects.get(pk=pk) 
    except Leaderboarddetail.DoesNotExist:
        return HttpResponse(status=404)
    queryset.delete()
    return HttpResponse(status=204)
@api_view(['POST'])
def changePoints(request, pk):
    data = JSONParser().parse(request)
    print(data)
    if data["type"] == "add":
        try:
            queryset = Leaderboarddetail.objects.get(pk=pk)
        except Leaderboarddetail.DoesNotExist:
            return HttpResponse(status=404)
        queryset.points=int(queryset.points)+1
        queryset.save()
        return HttpResponse(status=200)
    elif data["type"] == "sub":
        try:
            queryset = Leaderboarddetail.objects.get(pk=pk)
        except Leaderboarddetail.DoesNotExist:
            return HttpResponse(status=404)
        queryset.points=int(queryset.points)-1
        queryset.save()
        return HttpResponse(status=200)











    
   
 
