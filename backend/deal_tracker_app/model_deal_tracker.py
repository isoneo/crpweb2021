from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
from simple_history.models import HistoricalRecords

from source_reference_models import Src_tbl_deal_source,Src_tbl_deal_type,Src_tbl_deal_status,Src_tbl_deal_seller,Src_fund_list,Src_int_type,Src_payout_type
from well_collection_app import Master_well_info
import datetime as dt
from utils.suppl_mixin import LogBaseModel


class Deal_info(LogBaseModel):
    deal_id = models.BigAutoField(primary_key=True, db_column='deal_id')
    suppl_deal_id  = models.CharField(max_length=50,  unique=True)


    deal_name = models.CharField(max_length=200, default=None, blank=True, null=True, verbose_name='deal_name')
    deal_source = models.ForeignKey(Src_tbl_deal_source, models.SET_NULL, blank=True, null=True)
    deal_type = models.ForeignKey(Src_tbl_deal_type, models.SET_NULL, blank=True, null=True)
    deal_status = models.ForeignKey(Src_tbl_deal_status, models.SET_NULL, blank=True, null=True)
    current_reviewer = models.ManyToManyField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null = True, related_name='user_current_deal_reviewer', through='Xref_current_deal_reviewer')
    sellername = models.ForeignKey(Src_tbl_deal_seller, models.SET_NULL, blank=True, null=True)

    deal_date_added = models.DateField(default=dt.datetime.date.today)
    deal_date_status = models.DateField(default=dt.datetime.date.today)
    deal_date_duedate = models.DateField(default=(dt.datetime.datetime.now() + dt.datetime.timedelta(days=7)).date(),
                                         blank=True,
                                         null=True, verbose_name='Due Date')
    deal_date_commit = models.DateField(default=None, blank=True, null=True)
    deal_date_closed = models.DateField(default=None, blank=True, null=True)
    deal_date_modified = models.DateTimeField(default=dt.datetime.datetime.now())

    closed_deal_no = models.BigIntegerField(default=None, blank=True, null=True)
    closed_deal_no_str = models.CharField(max_length=200, default=None, blank=True, null=True)
    deal_total_closing_acq_amt = models.FloatField(blank=True, null=True)
    deal_gr_afe_amt =  models.FloatField(blank=True, null=True)
    deal_net_afe_amt = models.FloatField(blank=True, null=True)
    deal_total_net_acs = models.FloatField(blank=True, null=True)
    deal_total_no_wells = models.BigIntegerField(default=None, blank=True, null=True)
    deal_metric_gr_irr = models.FloatField(blank=True,
                                           null=True)  # This Asset level well economics without bonus terms IRR
    deal_metric_net_irr = models.FloatField(blank=True,
                                            null=True)  # This is Deal level well economics with bonus terms IRR
    deal_closing_comments = models.TextField(default=None, blank=True,
                                             null=True)  # Seperate from comments(?) Deal closing comments only
    master_well = models.ManyToManyField(Master_well_info, through='Xref_deal_well', blank=True, symmetrical=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='user_deal_created')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='user_deal_updated')
    history = HistoricalRecords()
    _DATABASE = 'default'

    class Meta:
        db_table = 'deal_info'

class Deal_status_history(LogBaseModel):
    deal_status_history_id = models.BigAutoField(primary_key=True, db_column='deal_status_history_id')
    deal = models.ForeignKey(Deal_info, models.SET_NULL, blank=True, null=True)
    deal_status = models.ForeignKey(Src_tbl_deal_status,models.SET_NULL, blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                                   related_name='user_deal_created')
    status_comment = models.CharField(max_length=255, blank = True, null = True)
    _DATABASE = 'default'

    class Meta:
        db_table = 'deal_status_history'

class Xref_current_deal_reviewer(models.Model):
    xref_deal_current_reviewer_id = models.AutoField(primary_key=True, db_column='xref_deal_current_reviewer_id')
    deal = models.ForeignKey(Deal_info, on_delete=models.CASCADE, related_name='deal_current_reviewer', db_column='deal')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='current_reviewer_to_deal', db_column='user')

    history = HistoricalRecords(custom_model_name=lambda x:f'Audit_historical_{x}')
    _DATABASE = 'default'

    class Meta:
        db_table = 'xref_current_deal_reviewer'
        unique_together = ("deal", "user")


class Xref_deal_well(models.Model):
    xref_deal_well_id = models.AutoField(primary_key=True, db_column='xref_deal_well_id')
    deal = models.ForeignKey(Deal_info, on_delete=models.CASCADE, related_name='deal_to_well', db_column='deal')
    master_well = models.ForeignKey(Master_well_info, on_delete=models.CASCADE, related_name='well_to_deal', db_column='master_well')

    history = HistoricalRecords(custom_model_name=lambda x:f'Audit_historical_{x}')
    _DATABASE = 'default'

    class Meta:
        db_table = 'xref_deal_well'
        unique_together = ("deal", "master_well")


class Deal_well_interest(LogBaseModel):
    dw_id = models.AutoField(primary_key=True, db_column ='dw_id')
    xref_dw = models.ForeignKey(Xref_deal_well, on_delete=models.CASCADE, related_name='dw_interest',db_column='xref_dw')
    int_fund = models.ForeignKey(Src_fund_list, models.SET_NULL, blank=True, null=True)
    int_type = models.ForeignKey(Src_int_type, models.SET_NULL, blank=True, null=True)
    payout_type = models.ForeignKey(Src_payout_type, models.SET_NULL, blank=True, null=True)
    payout_value = models.FloatField(null=True, blank=True)
    bpo_wi = models.DecimalField(null=True, blank=True, default=0, decimal_places=8, max_digits=10)
    bpo_nri = models.DecimalField(null=True, blank=True, default=0, decimal_places=8, max_digits=10)
    apo1_wi = models.DecimalField(null=True, blank=True, default=0, decimal_places=8, max_digits=10)
    apo1_nri = models.DecimalField(null=True, blank=True, default=0, decimal_places=8, max_digits=10)
    apo2_wi = models.DecimalField(null=True, blank=True, default=0, decimal_places=8, max_digits=10)
    apo2_nri = models.DecimalField(null=True, blank=True, default=0, decimal_places=8, max_digits=10)
    orri1 = models.DecimalField(null=True, blank=True, default=0, decimal_places=8, max_digits=10)
    orri2 = models.DecimalField(null=True, blank=True, default=0, decimal_places=8, max_digits=10)
    assgn_nri = models.DecimalField(null=True, blank=True, default=0, decimal_places=8, max_digits=10)
    bpo_burden = models.DecimalField(null=True, blank=True, default=0, decimal_places=8, max_digits=10)
    apo1_burden = models.DecimalField(null=True, blank=True, default=0, decimal_places=8, max_digits=10)
    apo2_burden = models.DecimalField(null=True, blank=True, default=0, decimal_places=8, max_digits=10)
    unit_size = models.FloatField(null=True, blank=True)
    net_acs = models.FloatField(null=True, blank=True)
    bonus_amt = models.FloatField(null=True, blank=True)
    interest_comments = models.TextField(default=None, blank=True, null=True)
    po_comments = models.TextField(default=None, blank=True, null=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='user_dw_int_created')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='user_dw_int_updated')
    history = HistoricalRecords(custom_model_name=lambda x:f'Audit_historical_{x}')
    _DATABASE = 'default'

    class Meta:
        db_table = 'deal_well_interest_info'
        ordering = ('xref_deal_well_id','int_fund__ref_fund_list_id')

