# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-25 19:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Hostel', '0005_guestentry_hostelcomplaint_inoutlist_roomregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=None, max_length=50)),
                ('middle_name', models.CharField(default=None, max_length=50)),
                ('last_name', models.CharField(default=None, max_length=50)),
                ('gender', models.CharField(max_length=2)),
                ('joining_year', models.CharField(max_length=10)),
                ('blood_grp', models.CharField(default=None, max_length=20)),
                ('role', models.CharField(max_length=10)),
                ('department', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='guestentry',
            name='roll_no',
        ),
        migrations.RemoveField(
            model_name='hostelcomplaint',
            name='roll_no',
        ),
        migrations.RemoveField(
            model_name='inoutlist',
            name='roll_no',
        ),
        migrations.RemoveField(
            model_name='mobileno',
            name='student',
        ),
        migrations.RemoveField(
            model_name='roomregistration',
            name='roll_no',
        ),
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='roll_no',
        ),
        migrations.AddField(
            model_name='guestentry',
            name='student',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Hostel.Student'),
        ),
        migrations.AddField(
            model_name='hostelcomplaint',
            name='student',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Hostel.Student'),
        ),
        migrations.AddField(
            model_name='inoutlist',
            name='student',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Hostel.Student'),
        ),
        migrations.AddField(
            model_name='mobileno',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='roomregistration',
            name='student',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='Hostel.Student'),
        ),
        migrations.AddField(
            model_name='student',
            name='rollno',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='guestentry',
            name='guest_gender',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='guestentry',
            name='no_of_stay',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='hostelcomplaint',
            name='complaint',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='inoutlist',
            name='in_time',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='inoutlist',
            name='out_place',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='inoutlist',
            name='out_reason',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='inoutlist',
            name='out_time',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='mobileno',
            name='mobile_no',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='roomregistration',
            name='hostel_name',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='blood_grp',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='curr_sem',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='student',
            name='curr_year',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='middle_name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='regis_deg',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='regis_deg_dur',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='student',
            name='regis_year',
            field=models.IntegerField(default=None),
        ),
    ]
