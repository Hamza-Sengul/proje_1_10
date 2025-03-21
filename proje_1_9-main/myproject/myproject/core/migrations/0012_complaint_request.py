# Generated by Django 5.1.4 on 2025-03-13 11:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_payment_payment_method'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Şikayet Başlığı')),
                ('description', models.TextField(verbose_name='Şikayet Açıklaması')),
                ('status', models.CharField(choices=[('beklemede', 'Beklemede'), ('cozuldu', 'Çözüldü'), ('cozulemedi', 'Çözülemedi')], default='beklemede', max_length=20)),
                ('cozum_detay', models.TextField(blank=True, null=True, verbose_name='Çözüm/Neden Detayı')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.customer', verbose_name='Müşteri')),
                ('rep', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Temsilci')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='İstek Adı')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Fiyat')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Açıklama')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.customer', verbose_name='Müşteri')),
                ('rep', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Temsilci')),
            ],
        ),
    ]
