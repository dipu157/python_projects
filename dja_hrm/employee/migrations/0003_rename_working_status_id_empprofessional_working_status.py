# Generated by Django 4.2.4 on 2023-08-23 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_rename_emp_personals_id_empprofessional_emp_personals'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empprofessional',
            old_name='working_status_id',
            new_name='working_status',
        ),
    ]
