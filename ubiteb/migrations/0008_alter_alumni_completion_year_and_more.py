# Generated by Django 4.2 on 2023-06-06 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ubiteb", "0007_remove_alumni_finish_year_alumni_completion_year_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="alumni",
            name="completion_year",
            field=models.IntegerField(
                choices=[
                    (1980, 1980),
                    (1981, 1981),
                    (1982, 1982),
                    (1983, 1983),
                    (1984, 1984),
                    (1985, 1985),
                    (1986, 1986),
                    (1987, 1987),
                    (1988, 1988),
                    (1989, 1989),
                    (1990, 1990),
                    (1991, 1991),
                    (1992, 1992),
                    (1993, 1993),
                    (1994, 1994),
                    (1995, 1995),
                    (1996, 1996),
                    (1997, 1997),
                    (1998, 1998),
                    (1999, 1999),
                    (2000, 2000),
                    (2001, 2001),
                    (2002, 2002),
                    (2003, 2003),
                    (2004, 2004),
                    (2005, 2005),
                    (2006, 2006),
                    (2007, 2007),
                    (2008, 2008),
                    (2009, 2009),
                    (2010, 2010),
                    (2011, 2011),
                    (2012, 2012),
                    (2013, 2013),
                    (2014, 2014),
                    (2015, 2015),
                    (2016, 2016),
                    (2017, 2017),
                    (2018, 2018),
                    (2019, 2019),
                    (2020, 2020),
                    (2021, 2021),
                    (2022, 2022),
                    (2023, 2023),
                ],
                default=2023,
                max_length=4,
                verbose_name="Completion Year",
            ),
        ),
        migrations.AlterField(
            model_name="alumni",
            name="employment_entity",
            field=models.CharField(
                choices=[
                    ("government", "Government"),
                    ("private", "Private"),
                    ("ngo", "NGO"),
                    ("missionnary", "Missionary"),
                    ("none", "None"),
                ],
                default="government",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="alumni",
            name="start_year",
            field=models.IntegerField(
                choices=[
                    (1980, 1980),
                    (1981, 1981),
                    (1982, 1982),
                    (1983, 1983),
                    (1984, 1984),
                    (1985, 1985),
                    (1986, 1986),
                    (1987, 1987),
                    (1988, 1988),
                    (1989, 1989),
                    (1990, 1990),
                    (1991, 1991),
                    (1992, 1992),
                    (1993, 1993),
                    (1994, 1994),
                    (1995, 1995),
                    (1996, 1996),
                    (1997, 1997),
                    (1998, 1998),
                    (1999, 1999),
                    (2000, 2000),
                    (2001, 2001),
                    (2002, 2002),
                    (2003, 2003),
                    (2004, 2004),
                    (2005, 2005),
                    (2006, 2006),
                    (2007, 2007),
                    (2008, 2008),
                    (2009, 2009),
                    (2010, 2010),
                    (2011, 2011),
                    (2012, 2012),
                    (2013, 2013),
                    (2014, 2014),
                    (2015, 2015),
                    (2016, 2016),
                    (2017, 2017),
                    (2018, 2018),
                    (2019, 2019),
                    (2020, 2020),
                    (2021, 2021),
                    (2022, 2022),
                    (2023, 2023),
                ],
                default=2023,
                max_length=4,
                verbose_name="Start Year",
            ),
        ),
    ]
