from django.db import models
from applicants.models import Applicant
from doctors.models import Doctor
from users.models import User
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Appointment(models.Model):
    INITIAL = 'Initial'
    RE_EVAL = 'Re-evaluation'
    RESCHEDULED = 'Reschedued'
    APPOINTMENT_TYPE = [
        (INITIAL, 'Initial'),
        (RE_EVAL, 'Re-evaluation'),
        (RESCHEDULED, 'Rescheduled')
    ]

    AME = 'AME'
    QME = 'QME'
    EXAM_TYPE = [
        (QME, 'QME'),
        (AME, 'AME'),
    ]
    appointment_type = models.CharField(max_length=20, choices=APPOINTMENT_TYPE, default=INITIAL)
    exam_type = models.CharField(max_length=120, choices=EXAM_TYPE, default=QME)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    panel_number = models.CharField(max_length=120, blank=True, null=True)

    scheduled_by = models.ForeignKey(User, on_delete=models.PROTECT)
    scheduled_date = models.DateTimeField(auto_now_add=True)

    records_sent = models.BooleanField(default=False)
    # datetimefields require null or else integrityerror
    records_sent_date = models.DateTimeField(blank=True, null=True)

    records_received = models.BooleanField(default=False)
    records_received_date = models.DateTimeField(blank=True, null=True)

    notes = models.TextField(blank=True)

    # Following fields will be hidden from initial create view and displayed on updateview once applicant has attended or missed appt.
    # For attended, keep default None or else default = "didn't attend"
    # LOGIC: If appointment date, show:
    attended = models.BooleanField(default=False)
    # if didn't attend, set logic:
    """
    create another instance of appt model, 
    input necessary previous data except 
    appt date/attneded will be blank on new object and 
    type=rescheduled
    """

    def get_absolute_url(self):
        return reverse('appointment', kwargs={'pk': self.pk})
