from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from announcement.models import Announcement
from announcement.serializers import AnnouncementSerializer

# Create your views here.


class AnnouncementView(APIView):
    def get(self, request, id=None):
        if id is None:
            items = Announcement.objects.all()
            serializer = AnnouncementSerializer(items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            immobile = Announcement.objects.get(id=id)
            serializer = AnnouncementSerializer(immobile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Announcement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id=None):
        try:
            if id is not None:
                immobile = Announcement.objects.get(id=id)
                serializer = AnnouncementSerializer(immobile, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except Announcement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = AnnouncementSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
