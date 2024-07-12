from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from .forms import UserRegistrationForm, UserLoginForm, MedicationForm, CitaForm
from .models import Medication, Cita, CardData

User = get_user_model()

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('registration_success')
    else:
        form = UserRegistrationForm()
    return render(request, 'app/nuevo_usuario.html', {'form': form})

def registration_success(request):
    return render(request, 'app/registration_success.html')

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard') 
    else:
        form = UserLoginForm()
    return render(request, 'app/login.html', {'form': form})

def medication_list(request):
    medications = Medication.objects.all()
    return render(request, 'app/8.Medicamentos.html', {'medications': medications})

def calculate_payment(request):
    if request.method == 'GET':
        medication_name = request.GET.get('medicamento')
        quantity = int(request.GET.get('cantidad', 1))
        medication = get_object_or_404(Medication, name=medication_name)
        total = medication.price * quantity
        return render(request, 'app/pagomed.html', {'medication': medication, 'quantity': quantity, 'total': total})
    return redirect('medication_list')

def citas(request):
    citas = Cita.objects.all()
    return render(request, 'app/citas.html', {'citas': citas})

def crear_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('citas')
    else:
        form = CitaForm()
    return render(request, 'app/crear_cita.html', {'form': form})

def editar_cita(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('citas')
    else:
        form = CitaForm(instance=cita)
    return render(request, 'app/editar_cita.html', {'form': form})

def eliminar_cita(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id)
    if request.method == 'POST':
        cita.delete()
        return redirect('citas')
    return render(request, 'app/eliminar_cita.html', {'cita': cita})

from django.views.decorators.csrf import csrf_protect

@csrf_protect
def save_card_data(request):
    if request.method == 'POST':
        card_number = request.POST.get('cardNumber')
        card_name = request.POST.get('cardName')
        expiry_date = request.POST.get('expiryDate')
        cvv = request.POST.get('cvv')

        CardData.objects.create(
            card_number=card_number,
            card_name=card_name,
            expiry_date=expiry_date,
            cvv=cvv
        )

        return redirect('medication_list')

    return render(request, 'OncoLife/pagomed.html')
