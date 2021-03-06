# Generated by Django 3.1.6 on 2021-02-22 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reftbl_countystate',
            fields=[
                ('county_state_id', models.CharField(db_column='county_state_id', max_length=255, primary_key=True, serialize=False)),
                ('country', models.CharField(db_index=True, max_length=255)),
                ('state_id', models.CharField(max_length=255)),
                ('county_id', models.CharField(max_length=255)),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('short_name', models.CharField(max_length=255)),
                ('state_long_name', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'ref_county_state_code',
            },
        ),
        migrations.CreateModel(
            name='Src_afe_type',
            fields=[
                ('ref_afe_type_id', models.AutoField(db_column='ref_afe_type_id', primary_key=True, serialize=False)),
                ('afe_type', models.CharField(max_length=255, unique=True)),
                ('afe_type_descrip', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'src_afe_type',
            },
        ),
        migrations.CreateModel(
            name='Src_department_list',
            fields=[
                ('ref_dept_list_id', models.AutoField(db_column='ref_dept_list_id', primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=255, unique=True)),
                ('dept_name_descrip', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'src_dept_list',
            },
        ),
        migrations.CreateModel(
            name='Src_fund_list',
            fields=[
                ('ref_fund_list_id', models.AutoField(db_column='ref_fund_list_id', primary_key=True, serialize=False)),
                ('fund_name', models.CharField(max_length=255, unique=True)),
                ('fund_name_descrip', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'src_fund_list',
            },
        ),
        migrations.CreateModel(
            name='Src_int_type',
            fields=[
                ('ref_int_type_id', models.AutoField(db_column='ref_int_type_id', primary_key=True, serialize=False)),
                ('int_type_name', models.CharField(max_length=255, unique=True)),
                ('int_type_name_descrip', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'src_int_type',
            },
        ),
        migrations.CreateModel(
            name='Src_payout_type',
            fields=[
                ('ref_payout_type_id', models.AutoField(db_column='ref_payout_type_id', primary_key=True, serialize=False)),
                ('payout_type', models.CharField(max_length=255, unique=True)),
                ('payout_type_descrip', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'src_payout_type',
            },
        ),
        migrations.CreateModel(
            name='Src_tbl_deal_source',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('src_tbl_deal_source_id', models.AutoField(db_column='src_tbl_deal_source_id', primary_key=True, serialize=False)),
                ('deal_source', models.CharField(max_length=4000, unique=True)),
                ('deal_source_helper', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'src_tbl_deal_source',
            },
        ),
        migrations.CreateModel(
            name='Src_tbl_deal_status',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('src_tbl_deal_status_id', models.AutoField(db_column='src_tbl_deal_status_id', primary_key=True, serialize=False)),
                ('deal_status_order', models.BigIntegerField(blank=True, default=None, null=True)),
                ('deal_status_code', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('deal_status_text', models.CharField(blank=True, default=None, max_length=80, null=True)),
                ('deal_status_helper', models.CharField(blank=True, default=None, max_length=255, null=True)),
            ],
            options={
                'db_table': 'src_tbl_deal_status',
            },
        ),
        migrations.CreateModel(
            name='Src_tbl_deal_type',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('src_tbl_deal_type_id', models.AutoField(db_column='src_tbl_deal_type_id', primary_key=True, serialize=False)),
                ('deal_type', models.CharField(max_length=4000, unique=True)),
                ('deal_type_helper', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'src_tbl_deal_type',
            },
        ),
        migrations.CreateModel(
            name='Src_tbl_deal_seller',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('seller_id', models.AutoField(db_column='seller_id', primary_key=True, serialize=False)),
                ('seller_name', models.CharField(max_length=4000, unique=True)),
                ('company', models.CharField(blank=True, max_length=255, null=True)),
                ('main_contact_person_name', models.CharField(blank=True, max_length=255, null=True)),
                ('address1', models.CharField(blank=True, max_length=255, null=True)),
                ('address2', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=100, null=True)),
                ('phone1', models.CharField(blank=True, max_length=100, null=True)),
                ('phone2', models.CharField(blank=True, max_length=100, null=True)),
                ('main_email', models.EmailField(blank=True, max_length=255, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_seller_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_seller_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'src_tbl_deal_seller',
            },
        ),
        migrations.CreateModel(
            name='Ref_crcat_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_type', models.CharField(max_length=255)),
                ('cat_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'ref_crcat_list',
                'unique_together': {('cat_type', 'cat_name')},
            },
        ),
        migrations.CreateModel(
            name='Audit_historical_Src_tbl_deal_type',
            fields=[
                ('created_date', models.DateTimeField(blank=True, editable=False)),
                ('modified_date', models.DateTimeField(blank=True, editable=False)),
                ('src_tbl_deal_type_id', models.IntegerField(blank=True, db_column='src_tbl_deal_type_id', db_index=True)),
                ('deal_type', models.CharField(db_index=True, max_length=4000)),
                ('deal_type_helper', models.CharField(blank=True, max_length=255, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical src_tbl_deal_type',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Audit_historical_Src_tbl_deal_status',
            fields=[
                ('created_date', models.DateTimeField(blank=True, editable=False)),
                ('modified_date', models.DateTimeField(blank=True, editable=False)),
                ('src_tbl_deal_status_id', models.IntegerField(blank=True, db_column='src_tbl_deal_status_id', db_index=True)),
                ('deal_status_order', models.BigIntegerField(blank=True, default=None, null=True)),
                ('deal_status_code', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('deal_status_text', models.CharField(blank=True, default=None, max_length=80, null=True)),
                ('deal_status_helper', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical src_tbl_deal_status',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Audit_historical_Src_tbl_deal_seller',
            fields=[
                ('created_date', models.DateTimeField(blank=True, editable=False)),
                ('modified_date', models.DateTimeField(blank=True, editable=False)),
                ('seller_id', models.IntegerField(blank=True, db_column='seller_id', db_index=True)),
                ('seller_name', models.CharField(db_index=True, max_length=4000)),
                ('company', models.CharField(blank=True, max_length=255, null=True)),
                ('main_contact_person_name', models.CharField(blank=True, max_length=255, null=True)),
                ('address1', models.CharField(blank=True, max_length=255, null=True)),
                ('address2', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=100, null=True)),
                ('phone1', models.CharField(blank=True, max_length=100, null=True)),
                ('phone2', models.CharField(blank=True, max_length=100, null=True)),
                ('main_email', models.EmailField(blank=True, max_length=255, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('created_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical src_tbl_deal_seller',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Audit_historical_Src_int_type',
            fields=[
                ('ref_int_type_id', models.IntegerField(blank=True, db_column='ref_int_type_id', db_index=True)),
                ('int_type_name', models.CharField(db_index=True, max_length=255)),
                ('int_type_name_descrip', models.CharField(blank=True, max_length=255, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical src_int_type',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Audit_historical_Src_fund_list',
            fields=[
                ('ref_fund_list_id', models.IntegerField(blank=True, db_column='ref_fund_list_id', db_index=True)),
                ('fund_name', models.CharField(db_index=True, max_length=255)),
                ('fund_name_descrip', models.CharField(blank=True, max_length=255, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical src_fund_list',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Audit_historical_Ref_crcat_list',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('cat_type', models.CharField(max_length=255)),
                ('cat_name', models.CharField(max_length=255)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical ref_crcat_list',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
