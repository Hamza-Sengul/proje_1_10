# Generated by Django 5.1.4 on 2025-03-13 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_paymenttype_subscriptionduration_subscriptiontype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='agreement_status',
            field=models.CharField(choices=[('beklemede', 'Beklemede'), ('olumlu', 'Olumlu'), ('olumsuz', 'Olumsuz')], max_length=10),
        ),
    ]
