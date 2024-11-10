from django.urls import path
from .views import *
urlpatterns = [
    # Doctor URLs
    path('doctors/', DoctorListView.as_view(), name='doctor_list'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('doctors/add/', DoctorCreateView.as_view(), name='doctor_add'),
    path('doctors/<int:pk>/edit/', DoctorUpdateView.as_view(), name='doctor_edit'),
    path('doctors/<int:pk>/delete/', DoctorDeleteView.as_view(), name='doctor_delete'),

    # Patient URLs
    path('patients/', PatientListView.as_view(), name='patient_list'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('patients/add/', PatientCreateView.as_view(), name='patient_add'),
    path('patients/<int:pk>/edit/', PatientUpdateView.as_view(), name='patient_edit'),
    path('patients/<int:pk>/delete/', PatientDeleteView.as_view(), name='patient_delete'),

    # Appointment URLs
    path('appointments/', AppointmentListView.as_view(), name='appointment_list'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment_detail'),
    path('appointments/add/', AppointmentCreateView.as_view(), name='appointment_add'),
    path('appointments/<int:pk>/edit/', AppointmentUpdateView.as_view(), name='appointment_edit'),
    path('appointments/<int:pk>/delete/', AppointmentDeleteView.as_view(), name='appointment_delete'),

    # Medical Record URLs
    path('medical_records/', MedicalRecordListView.as_view(), name='medical_record_list'),
    path('medical_records/<int:pk>/', MedicalRecordDetailView.as_view(), name='medical_record_detail'),
    path('medical_records/add/', MedicalRecordCreateView.as_view(), name='medical_record_add'),
    path('medical_records/<int:pk>/edit/', MedicalRecordUpdateView.as_view(), name='medical_record_edit'),
    path('medical_records/<int:pk>/delete/', MedicalRecordDeleteView.as_view(), name='medical_record_delete'),

    # Billing URLs
    path('billing/', BillingListView.as_view(), name='billing_list'),
    path('billing/<int:pk>/', BillingDetailView.as_view(), name='billing_detail'),
    path('billing/add/', BillingCreateView.as_view(), name='billing_add'),
    path('billing/<int:pk>/edit/', BillingUpdateView.as_view(), name='billing_edit'),
    path('billing/<int:pk>/delete/', BillingDeleteView.as_view(), name='billing_delete'),

]
