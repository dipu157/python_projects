# Generated by Django 4.2.4 on 2023-09-06 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_rename_working_status_id_empprofessional_working_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empprofessional',
            old_name='emp_personals',
            new_name='emp_personal',
        ),
        migrations.AlterModelTable(
            name='emppersonal',
            table='emp_personal',
        ),
        migrations.AlterModelTable(
            name='empprofessional',
            table='emp_professional',
        ),
    ]
