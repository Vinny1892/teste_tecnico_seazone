from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from immobile.models import Immobile
from immobile.serializers import ImmobileSerializer

# Create your views here.


class ImmobileView(APIView):
    """
    List all immobiles.
    """

    def get(self, request, id=None):
        if id is None:
            items = Immobile.objects.all()
            serializer = ImmobileSerializer(items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            immobile = Immobile.objects.get(id=id)
            serializer = ImmobileSerializer(immobile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Immobile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = ImmobileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, id=None):
        try:
            if id is not None:
                immobile = Immobile.objects.get(id=id)
                serializer = ImmobileSerializer(immobile, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except Immobile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id=None):
        try:
            immobile = Immobile.objects.get(id=id)
            immobile.delete()
        except Immobile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
