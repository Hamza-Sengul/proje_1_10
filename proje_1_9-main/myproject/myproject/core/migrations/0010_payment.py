# Generated by Django 5.1.4 on 2025-03-13 06:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_material_materialtransaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ödenen Tutar')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Not')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='core.customer')),
            ],
        ),
    ]
