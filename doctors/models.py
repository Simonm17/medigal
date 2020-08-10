from django.db import models
from django.urls import reverse
from contacts.models import Person


class Specialty(models.Model):
    SPECIALTY = [
        ('ACA', 'ACUPUNCTURE'),
        ('MAI', 'ALLERGY AND IMMUNOLOGY'),
        ('MAA', 'ANESTHESIOLOGY'),
        ('DCH', 'CHIROPRACTIC'),
        ('DEN', 'DENTISTRY'),
        ('MDE', 'DERMATOLOGY'),
        ('MEM', 'EMERGENCY MEDICINE'),
        ('MFP', 'FAMILY PRACTICE'),
        ('MPM', 'GENERAL PREVENTATIVE MEDICINE'),
        ('MHH', 'HAND'),
        ('MMM', 'INTERNAL MEDICINE'),
        ('MMV', 'INTERNAL MEDICINE-CARDIOVASCULAR DISEASE'),
        ('MME', 'INTERNAL MEDICINE-ENDOCRINOLOGY DIABETES AND METBOLISM'),
        ('MMG', 'INTERNAL MEDICINE-GASTROENTEROLOGY'),
        ('MMH', 'INTERNAL MEDICINE-HEMATOLOY'),
        ('MMI', 'INTERNAL MEDICINE-INFECTIOUS DISEASE'),
        ('MMN', 'INTERNAL MEDICINE-NEPHROLOGY'),
        ('MMP', 'INTERNAL MEDICINE-PULMONARY DISEASE'),
        ('MMR', 'INTERNAL MEDICINE-RHEUMATOLOGY'),
        ('MOQ', 'MEDICINE OTHERWISE QUALIFIED'),
        ('MNS', 'NEUROLOGICAL SURGERY (OTHER THAN SPINE)'),
        ('MPN', 'NEUROLOGY'),
        ('MOG', 'OBSTETRICS AND GYNECOLOGY'),
        ('MPO', 'OCCUPATIONAL MEDICINE'),
        ('MMO', 'ONCOLOGY-INTERNAL MEDICINE'),
        ('MOP', 'OPHTHALMOLOGY'),
        ('OPT', 'OPTOMETRY'),
        ('MOS', 'ORTHOPAEDIC SURGERY (OTHER THAN SPINE OR HAND'),
        ('MTO', 'OTOLARYNGOLOGY'),
        ('MPA', 'PAIN MEDICINE'),
        ('MHA', 'PATHOLOGY'),
        ('MPR', 'PHYSICAL MEDICINE AND REHABILITATION'),
        ('MPS', 'PLASTIC SURGERY (OTHER THAN HAND'),
        ('POD', 'PODIATRY'),
        ('MPD', 'PSYCHIATRY'),
        ('PSY', 'PSYCHOLOGY'),
        ('MNB', 'SPINE'),
        ('MSY', 'SURGERY (OTHER THAN SPINE OR HAND'),
        ('MSG', 'SURGERY-GENERAL VASCULAR'),
        ('MTS', 'THORACIC SURGERY'),
        ('MTT', 'TOXICOLOGY'),
        ('MUU', 'UROLOGY'),
        ('OTHER', 'OTHER')
    ]
    field = models.CharField(max_length=100, choices=SPECIALTY)


class Doctor(Person):
    specialty = models.ForeignKey(Specialty, on_delete=models.PROTECT)

    # Doctor preferences
    by_hardcopy = models.BooleanField(default=False)
    by_cd = models.BooleanField(default=False)
    by_usb = models.BooleanField(default=False)
    by_email = models.BooleanField(default=False)

    # For UpdateView to reverse back to after form POST request
    def get_absolute_url(self):
        return reverse('doctor_detail', kwargs={'pk': self.pk})