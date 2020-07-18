from django.shortcuts import render, redirect
from users.models import User
from .forms import DoctorCreationForm, AddressForm, TelephoneForm, EmailForm
from django.contrib import messages

def add_doctor(request):
    if request.method == 'POST':
        d_form = DoctorCreationForm(request.POST)
        a_form = AddressForm(request.POST)
        t_form = TelephoneForm(request.POST)
        e_form = EmailForm(request.POST)
        if d_form.is_valid() and a_form.is_valid() and t_form.is_valid() and e_form.is_valid():
            a_form.save()
            t_form.save()
            e_form.save()
            check_d_form = d_form.save(commit=False)
            check_d_form.created_by = request.user
            check_d_form.updated_by = request.user
            check_d_form.save()
            messages.success(request, f'Your contact form has been saved.')
            return redirect('index-home')
    else:
        d_form = DoctorCreationForm()
        a_form = AddressForm()
        t_form = TelephoneForm()
        e_form = EmailForm()
    return render(request, 'contacts/create_doctor.html', context={
        'd_form': d_form, 
        'a_form': a_form,
        't_form': t_form,
        'e_form': e_form,
        'title': 'New QME/AME Doctor',
    })