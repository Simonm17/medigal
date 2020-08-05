from django.shortcuts import render, redirect
from .models import Doctor
from contacts.models import Address, Telephone, Email
from .forms import DoctorCreationForm
from contacts.forms import AddressForm, TelephoneForm, EmailForm
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


@login_required
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
            last_a = Address.objects.last()
            last_t = Telephone.objects.last()
            last_e = Email.objects.last()
            doctor = Doctor.objects.last()
            doctor.address.add(last_a)
            doctor.telephone.add(last_t)
            doctor.email.add(last_e)
            doctor.save()
            messages.success(request, f'Your contact form has been saved.')
            return redirect('doctor_list')
    else:
        d_form = DoctorCreationForm()
        a_form = AddressForm()
        t_form = TelephoneForm()
        e_form = EmailForm()
    return render(request, 'doctors/create_doctor.html', context={
        'd_form': d_form, 
        'a_form': a_form,
        't_form': t_form,
        'e_form': e_form,
        'title': 'New QME/AME Doctor',
    })


class DoctorListView(LoginRequiredMixin, ListView):
    model = Doctor
    template_name = 'doctors/doctor_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'doctors'
    ordering = ['last_name']

    def get_queryset(self):
        if self.request.user.is_staff:
            return Doctor.objects.all()
        return Doctor.objects.filter(created_by=self.request.user)

class DoctorDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """ for template context, use 'doctor' or 'object' """
    model = Doctor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address'] = Address.objects.all()
        context['telephone'] = Telephone.objects.all()
        context['email'] = Email.objects.all()
        return context

    def test_func(self):
        self.doctor = self.get_object()
        if self.request.user.is_staff or self.request.user == self.doctor.created_by:
            return True
        return False

class DoctorUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Doctor
    fields = ['prefix', 'first_name', 'last_name', 'suffix']
    template_name = 'doctors/doctor_update.html'
    success_message = 'Contact detail has been updated successfully!'

    def test_func(self):
        self.doctor = self.get_object()
        if self.request.user.is_staff or self.request.user == self.doctor.created_by:
            return True
        return False
