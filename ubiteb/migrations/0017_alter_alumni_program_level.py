# Generated by Django 4.2 on 2023-06-09 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ubiteb", "0016_alter_alumni_program_level"),
    ]

    operations = [
        migrations.AlterField(
            model_name="alumni",
            name="program_level",
            field=models.CharField(
                choices=[("certificate", "Certificate"), ("diploma", "Diploma")],
                default="Certificate",
                max_length=30,
            ),
        ),
    ]