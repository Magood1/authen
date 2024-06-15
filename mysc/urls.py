from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthViewSet, PatientViewSet, AppointmentViewSet

router = DefaultRouter()
router.register(r'auth', AuthViewSet, basename='auth')
router.register(r'patients', PatientViewSet, basename='patients')
router.register(r'appointments', AppointmentViewSet, basename='appointments')

urlpatterns = [
    path('', include(router.urls)),
]
