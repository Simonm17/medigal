from django.shortcuts import render, redirect
from .models import Applicant
from contacts.models import Address, Telephone, Email
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

class ApplicantListView(ListView):
    model = Applicant
    template_name = 'applicant/applicant_list.html'
    context_object_name = 'applicants'
    ordering = ['first_name']

class ApplicantDetailView(DetailView):
    # for template context, use 'applicant' or 'object'
    model = Applicant

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address'] = Address.objects.all()
        context['telephone'] = Telephone.objects.all()
        context['email'] = Email.objects.all()
        return context

class ApplicantUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Applicant
    fields = ['prefix', 'first_name', 'last_name', 'suffix']
    template_name = 'applicants/applicant_update.html'
    success_message = 'Contact detail has been updated successfully!'
