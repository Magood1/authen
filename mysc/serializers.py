from rest_framework import serializers
from .models import Doctor, Patient, Appointment

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'specialization', 'email']

class PatientSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Patient
        fields = ['id', 'first_name', 'last_name', 'email', 'created_by']

class AppointmentSerializer(serializers.ModelSerializer):
    doctor = serializers.HiddenField(default=serializers.CurrentUserDefault())
    patient = PatientSerializer(read_only=True)
    patient_id = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all(), source='patient', write_only=True)

    class Meta:
        model = Appointment
        fields = ['id', 'doctor', 'patient', 'patient_id', 'appointment_date']