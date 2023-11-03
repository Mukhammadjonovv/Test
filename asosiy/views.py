from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import *
from .serializers import *

class SuvViewSet(viewsets.ModelViewSet):
    queryset = Suv.objects.all()
    serializer_class = SuvSerializer

class MijozViewSet(viewsets.ModelViewSet):
    queryset = Mijoz.objects.all()
    serializer_class = MijozSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class HaydovchiViewSet(viewsets.ModelViewSet):
    queryset = Haydovchi.objects.all()
    serializer_class = HaydovchiSerializer

class BuyurtmaViewSet(viewsets.ModelViewSet):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializer

class MijozQidirish(generics.ListAPIView):
    queryset = Mijoz.objects.all()
    serializer_class = MijozSerializer

    def get_queryset(self):
        queryset = Mijoz.objects.all()
        name = self.request.query_params.get('ism', None)
        tel = self.request.query_params.get('tel', None)
        if name is not None and tel is not None:
            queryset = queryset.filter(ism__icontains=name, tel__icontains=tel)
        return queryset
