# Generated by Django 5.1 on 2024-09-28 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_delete_course_info_course_about_course_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sign_up_table',
            name='about_me',
            field=models.TextField(blank=True, null=True),
        ),
    ]
