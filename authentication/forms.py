from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Aadhaar, Details, TimeSheet


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


class SignUpForm_Student(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    standard = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Standard",
                "class": "form-control"
            }
        ))
    section = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Section",
                "class": "form-control"
            }
        ))
    stream = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Stream",
                "class": "form-control"
            }
        ))
    roll_no = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Roll No",
                "class": "form-control"
            }
        ))
    student_id = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Student Id",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Retype Password",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class SignUpForm_teacher(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Subject",
                "class": "form-control"
            }
        ))
    classes_taught = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "classes Taught",
                "class": "form-control"
            }
        ))
    contact_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Contact Number",
                "class": "form-control"
            }
        ))
    teacher_id = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Teacher Id",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Retype Password",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AadhaarForm(forms.Form):
    aadhaar_number = forms.CharField(max_length=12,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Your Adhar number",
            }
        ))
    aadhaar_file = forms.FileField(
        widget=forms.FileInput(
            attrs={
                "placeholder": "Upload Your Adhar Card",
                "class": "form-control",
                'text-align': 'center',
            }
        ))

class DetailForm(forms.Form):
    company_name = forms.CharField(max_length=250,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                'placeholder': 'Enter Company Name',
            }
        ))
    joining_date = forms.DateField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                'placeholder': 'Enter Joining Date in (year-month-date) format',
            }
        ))
    last_working_date = forms.DateField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                'placeholder': 'Enter Last Woring Date (year-month-date) format',
            }
        ))
    upload_document = forms.FileField(
        widget=forms.FileInput(
            attrs={
                "placeholder": "Upload Your Document",
                "class": "form-control",
                'text-align': 'center',
            }
        ))

class TimeSheetForm(forms.Form):
    date = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    'placeholder': 'Enter Date in YYYY-MM-DD format',
                }
        ))
    start_time = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    'placeholder': 'Enter Start Time in HH:MM format',
                }
        ))
    end_time = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    'placeholder': 'Enter End Time in HH:MM format',
                }
        ))


class GiveTaskForm(forms.Form):
    task = forms.CharField(max_length=250,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                'placeholder': 'Enter Task',
            }
        ))

class SubmitResultForm(forms.Form):
    answer = forms.CharField(max_length=250,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                'placeholder': 'Enter Answer',
            }
        ))