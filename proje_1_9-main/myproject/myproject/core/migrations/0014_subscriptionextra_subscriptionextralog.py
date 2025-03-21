# Generated by Django 5.1.4 on 2025-03-13 11:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_vehicle'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionExtra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Extra Adı')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Extra Fiyatı')),
                ('status', models.CharField(choices=[('active', 'Aktif'), ('canceled', 'İptal')], default='active', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.customer', verbose_name='Müşteri')),
                ('rep', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Temsilci')),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionExtraLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation', models.CharField(choices=[('create', 'Ekstra Ekleme'), ('update', 'Ekstra Güncelleme'), ('cancel', 'Ekstra İptali')], max_length=10)),
                ('old_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('new_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('details', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('extra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='core.subscriptionextra')),
                ('performed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
