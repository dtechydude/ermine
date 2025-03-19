# Generated by Django 4.2.20 on 2025-03-19 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriberList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_status', models.CharField(choices=[('Select', 'Select'), ('Business_Owner', 'Business_Owner'), ('Employee', 'Employee')], default='Select', max_length=25)),
                ('business_name', models.CharField(blank=True, max_length=20)),
                ('office_address', models.CharField(blank=True, max_length=20)),
                ('business_address', models.CharField(blank=True, max_length=20)),
                ('business_phone', models.CharField(blank=True, max_length=16)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
            options={
                'ordering': ['profile'],
            },
        ),
    ]
