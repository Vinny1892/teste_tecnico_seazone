from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from reserve.models import Reserve
from reserve.serializers import ReserveSerializer

# Create your views here.


class ReserveView(APIView):
    def get(self, request, id=None):
        if id is None:
            items = Reserve.objects.all()
            serializer = ReserveSerializer(items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            immobile = Reserve.objects.get(id=id)
            serializer = ReserveSerializer(immobile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Reserve.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = ReserveSerializer(data=request.data, context={"request": request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, id=None):
        try:
            reserve = Reserve.objects.get(id=id)
            reserve.delete()
        except Reserve.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
