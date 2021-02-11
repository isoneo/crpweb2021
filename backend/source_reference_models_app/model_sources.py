from django.db import models
# from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords
from utils.suppl_mixin import LogBaseModel
from django.conf import settings


class Reftbl_countystate(models.Model):
    county_state_id = models.CharField(max_length=255, primary_key=True)
    country = models.CharField(max_length=255, db_index=True)
    state_id = models.CharField(max_length=255)
    county_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255, db_index=True)
    short_name = models.CharField(max_length=255)
    state_long_name = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, db_index=True, null=True, blank=True)
    # history = HistoricalRecords()
    _DATABASE = 'default'

    class Meta(object):
        db_table = 'ref_county_state_code'


class Ref_crcat_list(models.Model):
    cat_type = models.CharField(max_length=255)
    cat_name = models.CharField(max_length=255)
    # created_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True)
    # updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    history = HistoricalRecords(custom_model_name=lambda x:f'Audit_historical_{x}')
    _DATABASE = 'default'

    class Meta(object):
        db_table = 'ref_crcat_list'
        unique_together = ('cat_type', 'cat_name')


class Src_tbl_deal_seller(LogBaseModel):
    seller_id = models.AutoField(primary_key=True)
    seller_name = models.CharField(max_length=4000, unique=True)
    company = models.CharField(max_length=255, null=True, blank=True)
    main_contact_person_name = models.CharField(max_length=255, null=True, blank=True)
    address1 = models.CharField(max_length=255, null=True, blank=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=100, null=True, blank=True)
    phone1 = models.CharField(max_length=100, null=True, blank=True)
    phone2 = models.CharField(max_length=100, null=True, blank=True)
    main_email = models.EmailField(max_length=255, null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='user_seller_created')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='user_seller_updated')
    history = HistoricalRecords(custom_model_name=lambda x:f'Audit_historical_{x}')
    _DATABASE = 'default'

    class Meta:
        db_table = 'src_tbl_deal_seller'


class Src_tbl_deal_status(LogBaseModel):
    src_tbl_deal_status_id = models.AutoField(primary_key=True)
    deal_status_order = models.BigIntegerField(default=None, blank=True, null=True)
    deal_status_code = models.CharField(max_length=40, default=None, blank=True, null=True)
    deal_status_text = models.CharField(max_length=80, default=None, blank=True, null=True)
    deal_status_helper = models.CharField(max_length=255, default=None, blank=True, null=True)
    # created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    # updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    history = HistoricalRecords(custom_model_name=lambda x:f'Audit_historical_{x}')
    _DATABASE = 'default'

    class Meta:
        db_table = 'src_tbl_deal_status'

    def save(self, *args, **kwargs):
        def increment_order_no():
            try:
                last_order = Src_tbl_deal_status.objects.latest('deal_status_order').deal_status_order
            except:
                last_order = None
            print(last_order)
            if last_order == None:
                new_order = 1
            else:
                new_order = last_order + 1
            return new_order

        print(self)
        # Saving unique id
        print("Printing Deal Status Order \n")
        print(self.deal_status_order)
        print(self.deal_status_text)
        print("Printed deal status order....\n")
        if self.deal_status_order is None or self.deal_status_order == '' or self.deal_status_order == 0:
            self.deal_status_order = increment_order_no()
        else:
            check_order = increment_order_no()
            if int(self.deal_status_order) > check_order:
                self.deal_status_order = check_order
            elif int(self.deal_status_order) < check_order:
                # Need to update the order for all wells after current order
                update_ls_order = Src_tbl_deal_status.objects.filter(
                    deal_status_order__gte=int(self.deal_status_order)).update(
                    deal_status_order=models.F('deal_status_order') + 1)
                # print(Src_tbl_deal_status.objects.filter(deal_status_order__gte=int(self.deal_status_order)))

        if self.deal_status_code is None:
            self.deal_status_code = 'dstat_' + str(self.deal_status_order)
        super(Src_tbl_deal_status, self).save(*args, **kwargs)


class Src_tbl_deal_type(LogBaseModel):
    src_tbl_deal_type_id = models.AutoField(primary_key=True)
    deal_type = models.CharField(max_length=4000, unique=True)
    deal_type_helper = models.CharField(max_length=255, null=True, blank=True)

    history = HistoricalRecords(custom_model_name=lambda x:f'Audit_historical_{x}')
    _DATABASE = 'default'

    class Meta:
        db_table = 'src_tbl_deal_type'


class Src_tbl_deal_source(LogBaseModel):
    src_tbl_deal_source_id = models.AutoField(primary_key=True)
    deal_source = models.CharField(max_length=4000, unique=True)
    deal_source_helper = models.CharField(max_length=255, null=True, blank=True)

    # history = HistoricalRecords()
    _DATABASE = 'default'

    class Meta:
        db_table = 'src_tbl_deal_source'


class Src_int_type(models.Model):
    ref_int_type_id = models.AutoField(primary_key=True)
    int_type_name = models.CharField(max_length=255, unique=True)
    int_type_name_descrip = models.CharField(max_length=255, null=True, blank=True)

    history = HistoricalRecords(custom_model_name=lambda x:f'Audit_historical_{x}')
    _DATABASE = 'default'

    class Meta(object):
        db_table = 'src_int_type'


class Src_fund_list(models.Model):
    ref_fund_list_id = models.AutoField(primary_key=True)
    fund_name = models.CharField(max_length=255, unique=True)
    fund_name_descrip = models.CharField(max_length=255, null=True, blank=True)

    history = HistoricalRecords(custom_model_name=lambda x:f'Audit_historical_{x}')
    _DATABASE = 'default'

    class Meta(object):
        db_table = 'src_fund_list'

class Src_department_list(models.Model):
    ref_dept_list_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=255, unique=True)
    dept_name_descrip = models.CharField(max_length=255, null=True, blank=True)

    # history = HistoricalRecords(custom_model_name=lambda x:f'Audit_historical_{x}')
    _DATABASE = 'default'

    class Meta(object):
        db_table = 'src_dept_list'

class Src_payout_type(models.Model):
    ref_payout_type_id = models.AutoField(primary_key=True)
    payout_type = models.CharField(max_length=255, unique=True)
    payout_type_descrip = models.CharField(max_length=255, null=True, blank=True)

    # history = HistoricalRecords()
    _DATABASE = 'default'

    class Meta(object):
        db_table = 'src_payout_type'



# well AFE type
class Src_afe_type(models.Model):
    ref_afe_type_id = models.AutoField(primary_key=True)
    afe_type = models.CharField(max_length=255, unique=True)
    afe_type_descrip = models.CharField(max_length=255, null=True, blank=True)

    # history = HistoricalRecords()
    _DATABASE = 'default'

    class Meta(object):
        db_table = 'src_afe_type'


