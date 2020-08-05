from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from .models import Applicant
from contacts.models import Address, Telephone, Email
from users.models import User
from .forms import ApplicantCreationForm
from contacts.forms import AddressForm, TelephoneForm, EmailForm
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


@login_required
def add_applicant(request):
    if request.method == 'POST':
        form = ApplicantCreationForm(request.POST)
        a_form = AddressForm(request.POST)
        t_form = TelephoneForm(request.POST)
        e_form = EmailForm(request.POST)
        if form.is_valid() and a_form.is_valid() and t_form.is_valid() and e_form.is_valid():
            check_form = form.save(commit=False)
            a_form.save()
            t_form.save()
            e_form.save()
            check_form.created_by = request.user
            check_form.updated_by = request.user
            check_form.save()
            last_a = Address.objects.last()
            last_t = Telephone.objects.last()
            last_e = Email.objects.last()
            applicant = Applicant.objects.last()
            applicant.address.add(last_a)
            applicant.telephone.add(last_t)
            applicant.email.add(last_e)
            applicant.save()
            messages.success(request, f'Your contact form has been saved!')
            return redirect('applicant_list')
    else:
        form = ApplicantCreationForm()
        a_form = AddressForm()
        t_form = TelephoneForm()
        e_form = EmailForm()
    return render(request, 'applicants/create_applicant.html', context={
        'form': form,
        'a_form': a_form,
        't_form': t_form,
        'e_form': e_form,
        'title': 'Add new Applicant',
    })

class ApplicantListView(LoginRequiredMixin, ListView):
    model = Applicant
    template_name = 'applicant/applicant_list.html'
    context_object_name = 'applicants'
    ordering = ['last_name']

    def get_queryset(self):
        if self.request.user.is_staff:
            return Applicant.objects.all()
        return Applicant.objects.filter(created_by=self.request.user)

class ApplicantDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    # for template context, use 'applicant' or 'object'
    model = Applicant

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address'] = Address.objects.all()
        context['telephone'] = Telephone.objects.all()
        context['email'] = Email.objects.all()
        return context

    def test_func(self):
        self.applicant = self.get_object()
        if self.request.user.is_staff or self.request.user == self.applicant.created_by:
            return True
        return False

class ApplicantUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Applicant
    fields = ['prefix', 'first_name', 'last_name', 'suffix']
    template_name = 'applicants/applicant_update.html'
    success_message = 'Contact detail has been updated successfully!'

    def test_func(self):
        self.applicant = self.get_object()
        if self.request.user.is_staff or self.request.user == self.applicant.created_by:
            return True
        return False
