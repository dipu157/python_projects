# Generated by Django 4.1.9 on 2023-07-10 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('construction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
                ('district', models.CharField(max_length=240)),
                ('area', models.CharField(max_length=240)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('details', models.CharField(blank=True, max_length=200, null=True)),
                ('land_owner_name', models.CharField(max_length=240)),
                ('owner_mobile', models.CharField(blank=True, max_length=200, null=True)),
                ('flat_qty', models.CharField(max_length=20)),
                ('parking_qty', models.CharField(max_length=20)),
                ('strat_date', models.DateField()),
                ('end_date', models.DateField()),
                ('image', models.ImageField(blank=True, upload_to='contractor/')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='company.company')),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='construction.contractor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
