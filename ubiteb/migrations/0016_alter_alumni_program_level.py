# Generated by Django 4.2 on 2023-06-09 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ubiteb", "0015_delete_alumnibulkupload"),
    ]

    operations = [
        migrations.AlterField(
            model_name="alumni",
            name="program_level",
            field=models.CharField(
                choices=[("Certificate", "certificate"), ("diploma", "Diploma")],
                default="certificate",
                max_length=30,
            ),
        ),
    ]
