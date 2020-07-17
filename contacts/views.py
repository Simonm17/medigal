from django.shortcuts import render
from .forms import DoctorCreationForm, AddressForm, TelephoneForm, EmailForm
from django.contrib import messages

def add_doctor(request):
    if request.method == 'POST':
        d_form = DoctorCreationForm(request.POST)
        a_form = AddressForm(request.POST)
        t_form = TelephoneForm(request.POST)
        e_form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your form has been saved.')
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