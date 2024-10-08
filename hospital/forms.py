from django import forms
from .models import Patient, Employee, Doctor, Appointment, Ward, Bed, OTBooking, Payroll, PatientBilling, Medication, Prescription, PrescriptionItem
from django.contrib.auth.models import User
from django.forms import inlineformset_factory

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'date_of_birth', 'gender', 
                  'phone_number', 'email', 'address', 'photo', 'patient_type']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'position', 'department', 'phone_number', 'email', 'photo']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialization', 'phone_number', 'photo']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'date', 'time', 'reason']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

class WardForm(forms.ModelForm):
    class Meta:
        model = Ward
        fields = ['name', 'capacity']

class BedForm(forms.ModelForm):
    class Meta:
        model = Bed
        fields = ['number', 'ward', 'is_occupied']
        widgets = {
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'ward': forms.Select(attrs={'class': 'form-control'}),
            'is_occupied': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class OTBookingForm(forms.ModelForm):
    class Meta:
        model = OTBooking
        fields = ['patient', 'doctor', 'scheduled_time', 'procedure', 'status', 'notes']
        widgets = {
            'scheduled_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class PayrollForm(forms.ModelForm):
    class Meta:
        model = Payroll
        fields = ['employee', 'salary', 'bonus', 'deductions', 'pay_date']
        widgets = {
            'pay_date': forms.DateInput(attrs={'type': 'date'}),
        }

class PatientBillingForm(forms.ModelForm):
    class Meta:
        model = PatientBilling
        fields = ['patient', 'total_amount', 'payment_status', 'description']
        widgets = {
            'billing_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ['name', 'company', 'action', 'description', 'price', 'stock']

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['patient', 'doctor', 'diseases']

class PrescriptionItemForm(forms.ModelForm):
    class Meta:
        model = PrescriptionItem
        fields = ['medication', 'dosage', 'frequency']

PrescriptionItemFormSet = inlineformset_factory(
    Prescription, PrescriptionItem, form=PrescriptionItemForm,
    extra=1, can_delete=True
)