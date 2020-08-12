from django.db import models
from applicants.models import Applicant
from doctors.models import Doctor
from users.models import User

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

    appointment_type = models.CharField(max_length=20, choices=APPOINTMENT_TYPE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    panel_number = models.CharField(max_length=120, blank=True, null=True)

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