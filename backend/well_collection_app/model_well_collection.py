from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
from simple_history.models import HistoricalRecords

import datetime as dt
from utils.suppl_mixin import LogBaseModel
from source_reference_models_app import Src_afe_type

# The master well table to add any evaulation well
class Well_master_info(LogBaseModel):
    master_well_id = models.BigAutoField(primary_key = True, db_column='master_well_id')
    well_creation_type = models.CharField(max_length=60, null = True, blank=True, default=None)
    # well_id= models.CharField(max_length=40, default=increment_deal_well_id, unique=True, primary_key=True)
    # deal_well_seq_no = models.BigIntegerField(default=None, blank=True, null=True)
    api = models.CharField(max_length=14, null=True, blank=True, unique=True, default=None)
    api10 = models.CharField(max_length=10, null=True, blank=True, unique=True, default=None)
    rseg_well_id = models.BigIntegerField(blank=True,null=True)

    leasename = models.CharField(max_length=255, null=True, blank=True, unique=True, default=None)
    operatorname = models.CharField(max_length=255, null=True, blank=True, default=None)

    crdcno = models.CharField(max_length=9, null=True, blank=True, default=None)

    rigrelease_date = models.DateField(blank=True, null=True)
    spud_date = models.DateField(blank=True, null=True)
    cmpl_date = models.DateField(blank=True, null=True)
    dofs = models.DateField(blank=True, null=True)

    crcat = models.CharField(max_length=255, null=True, blank=True, default=None)
    crcat_phase1 = models.CharField(max_length=255, null=True, blank=True, default=None)
    crcat_phase2 = models.CharField(max_length=255, null=True, blank=True, default=None)
    crcat_phase3 = models.CharField(max_length=255, null=True, blank=True, default=None)

    # wc_drilling = models.FloatField(blank=True, null=True, default=0)
    # wc_completion = models.FloatField(blank=True, null=True, default=0)
    # wc_facility = models.FloatField(blank=True, null=True, default=0)
    # wc_total = models.FloatField(blank=True, null=True, default=0)
    lateral_length = models.FloatField(blank=True, null=True, default=0)
    total_proppant = models.FloatField(blank=True, null=True, default=0)
    total_fluid = models.FloatField(blank = True, null=True, default=0)

    field_name = models.CharField(max_length=255, blank=True, null=True)
    reservoir_name = models.CharField(max_length=255, blank=True, null=True)
    play_name = models.CharField(max_length=255, blank=True, null=True)

    location = models.CharField(max_length=255, blank=True, null=True)
    twp = models.IntegerField(blank=True, null=True)
    rng = models.IntegerField(blank=True, null=True)
    sec = models.IntegerField(blank=True, null=True)
    county_name = models.CharField(max_length=255, blank=True, null=True)
    state_name = models.CharField(max_length=120, blank=True, null=True)

    sl_latitude = models.FloatField(null=True, blank=True, default=0)
    sl_longitude = models.FloatField(null=True, blank=True, default=0)
    bh_latitude = models.FloatField(null=True, blank=True, default=0)
    bh_longitude = models.FloatField(null=True, blank=True, default=0)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='user_master_well_created')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='user_master_well_updated')

    history = HistoricalRecords(custom_model_name=lambda x:f'Audit_historical_{x}')
    _DATABASE = 'default'

    class Meta:
        db_table = 'well_master_info'

class Well_master_afe_info(LogBaseModel):
    afe_id = models.BigAutoField(primary_key=True, db_column='afe_id')
    # afe_type = models.CharField(max_length=255, blank=True, null=True)
    afe_type = models.ForeignKey(Src_afe_type, on_delete = models.CASCADE, db_column='afe_type')
    master_well = models.ForeignKey(well_master_tbl, on_delete=models.CASCADE, db_column='master_well_id')
    tang_drlg_ct = models.FloatField(null=True, blank=True, default=0)
    intang_drlg_ct = models.FloatField(null=True, blank=True, default=0)
    total_drlg_ct = models.FloatField(null=True, blank=True, default=0)
    tang_cmpl_ct = models.FloatField(null=True, blank=True, default=0)
    intang_cmpl_ct = models.FloatField(null=True, blank=True, default=0)
    total_cmpl_ct = models.FloatField(null=True, blank=True, default=0)
    tang_fac_ct = models.FloatField(null=True, blank=True, default=0)
    intang_fac_ct = models.FloatField(null=True, blank=True, default=0)
    total_fac_ct = models.FloatField(null=True, blank=True, default=0)
    cmb_total_cpx =models.FloatField(null=True, blank=True, default=0)
    afe_date = models.DateField(blank=True, null=True)
    afe_status_date = models.DateField(blank=True, null=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='user_master_well_afe_created')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='user_master_well_afe_updated')

    history = HistoricalRecords(custom_model_name=lambda x:f'Audit_historical_{x}')
    _DATABASE = 'default'

    class Meta:
        db_table = 'well_master_afe_info'


# Limit to max 4 segments
class Well_master_prod_fc(LogBaseModel):
    well_prod_fc_id = models.BigAutoField(primary_key=True, db_column='well_prod_fc_id')
    master_well = models.ForeignKey(Well_master_info, on_delete=models.CASCADE, db_column='master_well_id')
    forecast_qualifier = models.CharField(max_length=255, blank=True, null=True)
    product_type =  models.CharField(max_length=25, blank=True, null=True)
    seg_no = models.IntegerField(blank=True, null=True)  # Multi segment to default Hyp to Exp or simple Exp etc
    s1_ip0 = models.FloatField(null=True, blank=True, default=0)
    s1_ip1 = models.FloatField(null=True, blank=True, default=0)
    s1_until_type = models.CharField(max_length=60, blank=True, null=True)
    s1_until_value = models.FloatField(null=True, blank=True, default=0)
    s1_b_value = models.FloatField(null=True, blank=True, default=0)
    s1_secant = models.FloatField(null=True, blank=True, default=0)
    s2_ip0 = models.FloatField(null=True, blank=True, default=0)
    s2_ip1 = models.FloatField(null=True, blank=True, default=0)
    s2_until_type = models.CharField(max_length=60, blank=True, null=True)
    s2_until_value = models.FloatField(null=True, blank=True, default=0)
    s2_b_value = models.FloatField(null=True, blank=True, default=0)
    s2_secant = models.FloatField(null=True, blank=True, default=0)
    s3_ip0 = models.FloatField(null=True, blank=True, default=0)
    s3_ip1 = models.FloatField(null=True, blank=True, default=0)
    s3_until_type = models.CharField(max_length=60, blank=True, null=True)
    s3_until_value = models.FloatField(null=True, blank=True, default=0)
    s3_b_value = models.FloatField(null=True, blank=True, default=0)
    s3_secant = models.FloatField(null=True, blank=True, default=0)
    s4_ip0 = models.FloatField(null=True, blank=True, default=0)
    s4_ip1 = models.FloatField(null=True, blank=True, default=0)
    s4_until_type = models.CharField(max_length=60, blank=True, null=True)
    s4_until_value = models.FloatField(null=True, blank=True, default=0)
    s4_b_value = models.FloatField(null=True, blank=True, default=0)
    s4_secant = models.FloatField(null=True, blank=True, default=0)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='user_master_well_prod_fc_created')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='user_master_well_prod_fc_updated')
    history = HistoricalRecords(custom_model_name=lambda x:f'Audit_historical_{x}')
    _DATABASE = 'default'

    class Meta:
        db_table = 'well_master_prod_fc'
        unique_together = ['master_well', 'forecast_qualifier','product_type']


# class RS_energy_well_info()