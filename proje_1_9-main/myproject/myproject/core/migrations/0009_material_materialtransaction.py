# Generated by Django 5.1.4 on 2025-03-13 06:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_employeetasklog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Malzeme Adı')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Fiyat')),
                ('quantity', models.PositiveIntegerField(verbose_name='Stok Adedi')),
                ('available', models.BooleanField(default=True, verbose_name='Verilebilir mi?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Verilen Adet')),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField(blank=True, null=True, verbose_name='Not')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.customer', verbose_name='Müşteri')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='core.material')),
                ('rep', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Temsilci')),
            ],
        ),
    ]
