# Generated by Django 4.2 on 2023-06-09 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ubiteb", "0020_alter_alumni_center_alter_alumni_certificate_status_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="alumni", name="center",),
        migrations.AddField(
            model_name="alumni",
            name="exam_center",
            field=models.CharField(choices=[], default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name="alumni",
            name="certificate_status",
            field=models.CharField(
                choices=[("Received", "Received"), ("Not Received", "Not Received")],
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="alumni",
            name="employment_entity",
            field=models.CharField(
                choices=[
                    ("Government", "Government"),
                    ("Private", "Private"),
                    ("NGO", "NGO"),
                    ("Missionary", "Missionary"),
                    ("None", "None"),
                ],
                max_length=40,
            ),
        ),
        migrations.AlterField(
            model_name="alumni",
            name="employment_status",
            field=models.CharField(
                choices=[("Employed", "Employed"), ("Unemployed", "Unemployed")],
                max_length=40,
            ),
        ),
        migrations.AlterField(
            model_name="alumni",
            name="gender",
            field=models.CharField(
                choices=[("Male", "Male"), ("Female", "Female")],
                default="male",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="alumni",
            name="program",
            field=models.CharField(
                choices=[
                    (
                        "National Diploma in Mechanic Engineering",
                        "National Diploma in Mechanical Engineering",
                    ),
                    (
                        "National Diploma in Civil Engineering",
                        "National Diploma in Civil Engineering",
                    ),
                    (
                        "National Diploma in Water Engineering",
                        "National Diploma in Water Engineering",
                    ),
                    (
                        "National Diploma in Electrical Engineering",
                        "National Diploma in Electrical Engineering",
                    ),
                ],
                default=None,
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="alumni",
            name="program_level",
            field=models.CharField(
                choices=[
                    ("Higher Diploma", "Higher Diploma"),
                    ("Diploma", "Diploma"),
                    ("National Certificate", "National Certificate"),
                    ("Uganda Community of Polytechnic Certificate", "UCPC"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="alumni",
            name="transcript_status",
            field=models.CharField(
                choices=[("Received", "Received"), ("Not Received", "Not Received")],
                max_length=30,
            ),
        ),
    ]
