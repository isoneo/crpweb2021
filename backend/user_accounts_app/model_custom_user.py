from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords

from source_reference_models_app.model_sources import Src_fund_list, Src_department_list

# class CustomUser(AbstractUser):
#     pass

class Gondor_mgmt(models.Model):
    rcd_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,related_name='gondor_to_user')

    related_user_fund = models.ManyToManyField(Src_fund_list, blank=True, symmetrical=True, related_name='gondor_fund')
    related_user_department = models.ManyToManyField(Src_department_list, blank=True, symmetrical=True,related_name='gondor_department')
    history = HistoricalRecords(custom_model_name=lambda x:f'Audit_historical_{x}')
    _DATABASE = 'default'

    class Meta(object):
        db_table = 'gondor_mgmt'

    def gondor_user_details(self):
        return self.rcd_user

