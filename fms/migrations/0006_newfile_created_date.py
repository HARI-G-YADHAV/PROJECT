# Generated by Django 4.1.5 on 2023-09-20 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fms", "0005_delete_section_delete_user_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="newfile",
            name="created_date",
            field=models.DateTimeField(auto_now=True),
        ),
    ]