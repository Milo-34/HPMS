from pyexpat.errors import messages
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from emergency_49.utils import *
from .models import *
from .forms import *
from django.urls import reverse_lazy


#Doctor
class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctor_list.html'
    context_object_name = 'doctors'

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_by = self.request.GET.get('sort', 'first_name')
        search_query = self.request.GET.get('search', '').strip()

        if search_query:
            queryset = queryset.filter(
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query) |
                Q(specialization__icontains=search_query) |
                Q(phone_number__icontains=search_query) |
                Q(email__icontains=search_query)
            )

        queryset_list = list(queryset)
        sorted_doctors = quicksort(queryset_list, key=lambda x: getattr(x, sort_by))
        if search_query:
            result = binary_search(sorted_doctors, search_query, 'first_name')
        return sorted_doctors

class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'doctor_detail.html'

class DoctorCreateView(CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctor_form.html'
    success_url = '/doctors/'

class DoctorUpdateView(UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctor_form.html'
    success_url = '/doctors/'

class DoctorDeleteView(DeleteView):
    model = Doctor
    template_name = 'doctor_confirm_delete.html'
    success_url = '/doctors/'

#Patient
class PatientListView(ListView):
    model = Patient
    template_name = 'patient_list.html'
    context_object_name = 'patients'

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_by = self.request.GET.get('sort', 'id')
        search_query = self.request.GET.get('search', '').strip()

        if search_query:
            queryset = queryset.filter(
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query) |
                Q(date_of_birth__icontains=search_query) |
                Q(phone_number__icontains=search_query) |
                Q(email__icontains=search_query)
            )

        queryset_list = list(queryset)
        sorted_patients = quicksort(queryset_list, key=lambda x: getattr(x, sort_by))
        if search_query:
            result = binary_search(sorted_patients, search_query, 'first_name')
        return sorted_patients


class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patient_detail.html'

class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient_form.html'
    success_url = '/patients/'

class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient_form.html'
    success_url = '/patients/'

class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'patient_confirm_delete.html'
    success_url = '/patients/'

#Appointment
class AppointmentListView(ListView):
    model = Appointment
    template_name = 'appointment_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_by = self.request.GET.get('sort', 'appointment_date')
        search_query = self.request.GET.get('search', '').strip()
        
        if search_query:
            queryset = queryset.filter(
                Q(patient__first_name__icontains=search_query) |
                Q(patient__last_name__icontains=search_query) |
                Q(doctor__first_name__icontains=search_query) |
                Q(doctor__last_name__icontains=search_query)
            )
        queryset_list = list(queryset)
        if sort_by == 'patient':
            sorted_appointments = quicksort(queryset_list, key=lambda x: (x.patient.first_name, x.patient.last_name))
        elif sort_by == 'doctor':
            sorted_appointments = quicksort(queryset_list, key=lambda x: (x.doctor.first_name, x.doctor.last_name))
        else:
            sorted_appointments = quicksort(queryset_list, key=lambda x: x.appointment_date)
        if search_query:
            result = binary_search(sorted_appointments, search_query, 'patient') 
        return sorted_appointments



class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = 'appointment_detail.html'

class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointment_form.html'
    success_url = '/appointments/'

class AppointmentUpdateView(UpdateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointment_form.html'
    success_url = '/appointments/'

class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'appointment_confirm_delete.html'
    success_url = '/appointments/'

#MedicalRecord
class MedicalRecordListView(ListView):
    model = MedicalRecord
    template_name = 'medicalrecord_list.html'
    context_object_name = 'medical_records'

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_by = self.request.GET.get('sort', 'id')
        search_query = self.request.GET.get('search', '').strip()

        if search_query:
            queryset = queryset.filter(
                Q(patient__first_name__icontains=search_query) |
                Q(patient__last_name__icontains=search_query) |
                Q(details__icontains=search_query)
            )

        queryset_list = list(queryset)
        valid_sort_options = ['id', 'patient__first_name', 'patient__last_name', 'record_date', 'details']
        if sort_by in valid_sort_options:
            if sort_by == 'patient__first_name':
                sorted_records = quicksort(queryset_list, key=lambda x: x.patient.first_name)
            elif sort_by == 'patient__last_name':
                sorted_records = quicksort(queryset_list, key=lambda x: x.patient.last_name)
            elif sort_by == 'record_date':
                sorted_records = quicksort(queryset_list, key=lambda x: x.record_date)
            elif sort_by == 'details':
                sorted_records = quicksort(queryset_list, key=lambda x: x.details)
            else:
                sorted_records = quicksort(queryset_list, key=lambda x: x.id)
        else:
            sorted_records = queryset_list
        if search_query:
            result = binary_search(sorted_records, search_query, 'details')
        return sorted_records




class MedicalRecordDetailView(DetailView):
    model = MedicalRecord
    template_name = 'medicalrecord_detail.html'
    context_object_name = 'medical_record'

class MedicalRecordCreateView(CreateView):
    model = MedicalRecord
    form_class = MedicalRecordForm
    template_name = 'medicalrecord_form.html'
    success_url = '/medical_records/'

class MedicalRecordUpdateView(UpdateView):
    model = MedicalRecord
    form_class = MedicalRecordForm
    template_name = 'medicalrecord_form.html'
    success_url = '/medical_records/'

class MedicalRecordDeleteView(DeleteView):
    model = MedicalRecord
    template_name = 'medicalrecord_confirm_delete.html'
    success_url = '/medical_records/'

#Billing
from django.db.models import Q
from django.views.generic import ListView
from .models import Billing

class BillingListView(ListView):
    model = Billing
    template_name = 'billing_list.html'
    context_object_name = 'billings'

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_by = self.request.GET.get('sort', 'id')
        search_query = self.request.GET.get('search', '').strip()
        filter_status = self.request.GET.get('status', '')

        if filter_status:
            if filter_status.lower() == 'paid':
                queryset = queryset.filter(is_paid=True)
            elif filter_status.lower() == 'unpaid':
                queryset = queryset.filter(is_paid=False)

        if search_query:
            queryset = queryset.filter(
                Q(patient__first_name__icontains=search_query) |
                Q(patient__last_name__icontains=search_query) |
                Q(amount_due__icontains=search_query) |
                Q(due_date__icontains=search_query)
            )

        queryset_list = list(queryset)

        valid_sort_options = ['patient', 'amount_due', 'due_date', 'status']
        if sort_by in valid_sort_options:
            if sort_by == 'patient':
                sorted_billings = quicksort(queryset_list, key=lambda x: x.patient.first_name)
            elif sort_by == 'amount_due':
                sorted_billings = quicksort(queryset_list, key=lambda x: x.amount_due)
            elif sort_by == 'due_date':
                sorted_billings = quicksort(queryset_list, key=lambda x: x.due_date)
            elif sort_by == 'status':
                sorted_billings = quicksort(queryset_list, key=lambda x: x.is_paid)
            else:
                sorted_billings = queryset_list
        else:
            sorted_billings = queryset_list 

        if search_query:
            sorted_billings = binary_search(sorted_billings, search_query, 'amount_due')

        return sorted_billings


class BillingDetailView(DetailView):
    model = Billing
    template_name = 'billing_detail.html'

class BillingCreateView(CreateView):
    model = Billing
    form_class = BillingForm
    template_name = 'billing_form.html'
    success_url = '/billing/'

class BillingUpdateView(UpdateView):
    model = Billing
    form_class = BillingForm
    template_name = 'billing_form.html'
    success_url = '/billing/'

class BillingDeleteView(DeleteView):
    model = Billing
    template_name = 'billing_confirm_delete.html'
    success_url = '/billing/'




