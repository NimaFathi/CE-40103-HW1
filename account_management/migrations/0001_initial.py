# Generated by Django 3.1.7 on 2021-03-07 18:24

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
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='زمان ساخت')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='آخرین زمان تغییر')),
                ('name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'اکانت',
                'verbose_name_plural': 'اکانت\u200cها',
            },
        ),
        migrations.CreateModel(
            name='HistoricalAccount',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created', models.DateTimeField(blank=True, db_index=True, editable=False, verbose_name='زمان ساخت')),
                ('modified', models.DateTimeField(blank=True, db_index=True, editable=False, verbose_name='آخرین زمان تغییر')),
                ('name', models.CharField(max_length=30)),
                ('username', models.CharField(db_index=True, max_length=30)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical اکانت',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]