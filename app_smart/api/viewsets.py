from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from app_smart.api import serializers
from app_smart.models import Sensor, TemperaturaData, ContadorData, LuminosidadeData, UmidadeData
from rest_framework import viewsets
from app_smart.api.filters import SensorFilter, TemperaturaDataFilter, ContadorFilterView, LuminosidadeFilterView, UmidadeFilterView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.decorators import action

class CreateUserAPIViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')

        if User.objects.filter(username=username).exists():
            return Response(
                {"detail": "Esse nome de usuário já foi cadastrado."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().post(request, *args, **kwargs)
    
class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = serializers.SensorSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SensorFilter

class SensorFilterView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args):
        tipo = request.data.get('tipo', None)
        localizacao = request.data.get('localizacao', None)
        responsavel = request.data.get('responsavel', None)
        status_operacional = request.data.get('status_operacional', None)

        filters = Q() #localiza um filtro vazio

        if tipo:
            filters &= Q(tipo__icontains=tipo)
        if localizacao:
            filters &= Q(localizacao__icontains=localizacao)
        if responsavel:
            filters &= Q(responsavel__icontains=responsavel)
        if status_operacional is not None:
            filters &= Q(status_operacional=status_operacional)

        queryset = Sensor.objects.filter(filters)
        serializer = serializers.SensorSerializer(queryset, many=True)
        return Response(serializer.data)
    
#function used in mobile
class SensorSelect():
    def sensor_select(request):
        results = Sensor.objects.all()[:6]  #limity 6 results
        data = list(results.values()) 
        return JsonResponse(data, safe=False)
    

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')

        if not User.objects.filter(username=username).exists():
            return Response(
                {"detail": "Usuário não possui cadastro."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().post(request, *args, **kwargs)
    
class UserViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def get_username(self, request):
        user = request.user
        if user.is_authenticated:
            return Response({"username": user.username}, status=status.HTTP_200_OK)
        return Response({"detail": "Usuário não está autenticado"}, status=status.HTTP_401_UNAUTHORIZED)

class TemperaturaDataViewSet(viewsets.ModelViewSet):
    queryset = TemperaturaData.objects.all()
    serializer_class = serializers.TemperaturaDataSerializar
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TemperaturaDataFilter

class ContadorDataViewSet(viewsets.ModelViewSet):
    queryset = ContadorData.objects.all()
    serializer_class = serializers.ContadorDataSerializar
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ContadorFilterView

class LuminosidadeDataViewSet(viewsets.ModelViewSet):
    queryset = LuminosidadeData.objects.all()
    serializer_class = serializers.LuminosidadeDataSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = LuminosidadeFilterView

class UmidadeDataViewSet(viewsets.ModelViewSet):
    queryset = UmidadeData.objects.all()
    serializer_class = serializers.UmidadeDataSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = UmidadeFilterView