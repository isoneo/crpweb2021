# Generated by Django 3.1.6 on 2021-02-11 19:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('source_reference_models_app', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gondor_mgmt',
            fields=[
                ('rcd_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='gondor_to_user', serialize=False, to='auth.user')),
                ('related_user_department', models.ManyToManyField(blank=True, related_name='gondor_department', to='source_reference_models_app.Src_department_list')),
                ('related_user_fund', models.ManyToManyField(blank=True, related_name='gondor_fund', to='source_reference_models_app.Src_fund_list')),
            ],
            options={
                'db_table': 'gondor_mgmt',
            },
        ),
        migrations.CreateModel(
            name='Audit_historical_Gondor_mgmt',
            fields=[
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('rcd_user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical gondor_mgmt',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]