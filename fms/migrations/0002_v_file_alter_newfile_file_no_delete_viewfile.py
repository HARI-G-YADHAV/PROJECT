# Generated by Django 4.1.5 on 2023-09-10 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fms", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="v_file",
            fields=[
                (
                    "vf_computer_no",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("vf_description", models.TextField()),
                ("vf_file_opned", models.DateField()),
                ("vf_file_closed", models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name="newfile",
            name="file_no",
            field=models.IntegerField(default=10, unique=True),
        ),
        migrations.DeleteModel(
            name="viewfile",
        ),
    ]
