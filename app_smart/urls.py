
from django.contrib import admin
from django.urls import path, include
from . import views
from app_smart.api.viewsets import CreateUserAPIViewSet, SensorViewSet, SensorFilterView, SensorSelect, TemperaturaDataViewSet, CustomTokenObtainPairView, UserViewSet, ContadorDataViewSet, LuminosidadeDataViewSet, UmidadeDataViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView                
from rest_framework.routers import DefaultRouter
from app_smart.api.filters import TemperaturaFilterView, ContadorFilterView, LuminosidadeFilterView, UmidadeFilterView

router = DefaultRouter()
router.register(r'sensores', SensorViewSet)
router.register(r'temperatura', TemperaturaDataViewSet)
router.register(r'contador', ContadorDataViewSet)
router.register(r'luminosidade', LuminosidadeDataViewSet)
router.register(r'umidade', UmidadeDataViewSet)

urlpatterns = [
    path('', views.abre_index, name='abre_index'),
    path('api/create_user/', CreateUserAPIViewSet.as_view(), name='createsuperuser'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('api/sensor_filter/', SensorFilterView.as_view(), name='sensor_filter'),
    path('api/select_sensor/', SensorSelect.sensor_select, name='sensor_select'), #url used in mobile
    path('api/temperatura_filter/', TemperaturaFilterView.as_view(), name='temperatura_filter'),
    path('api/user/', UserViewSet.as_view({'get': 'get_username'}), name='user'),
    path('api/contador_filter/', ContadorFilterView.as_view(), name='contador_filter'),
    path('api/luminosidade_filter/', LuminosidadeFilterView.as_view(), name='luminosidade_filter'),
    path('api/umidade_filter/', UmidadeFilterView.as_view(), name='umidade_filter'),
]