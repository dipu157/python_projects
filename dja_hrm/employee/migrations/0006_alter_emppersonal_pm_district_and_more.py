# Generated by Django 4.2.4 on 2023-09-16 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_alter_emppersonal_photo_alter_emppersonal_signature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emppersonal',
            name='pm_district',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='emppersonal',
            name='pm_post_code',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='emppersonal',
            name='pr_district',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='emppersonal',
            name='pr_post_code',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
