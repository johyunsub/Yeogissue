from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import Club, Club_article, Club_member
from .serializers import ClubSerializer, ClublistSerializer

@api_view(['GET'])
def club_list(reqeust):
    club = Club.objects.all()
    serializer = ClublistSerializer(club,many=True)
    print('1111111111111111111111111111111')
    return Response(serializer.data)



@api_view(['POST'])
def club_create(reqeust):
    serializer = ClubSerializer(data=reqeust.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def club_detail(request, club_pk):
    club = get_object_or_404(Club, pk=club_pk)
    # club
    if request.method == 'GET':
        serializer = ClubSerializer(club)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClubSerializer(club, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        club.delete()
        return Response({ 'id': club_pk }, status=status.HTTP_204_NO_CONTENT)