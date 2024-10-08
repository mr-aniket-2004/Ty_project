# Generated by Django 5.0.6 on 2024-08-15 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_sign_up_table_pincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign_up_table',
            name='add',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='sign_up_table',
            name='city_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sign_up_table',
            name='collge_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='sign_up_table',
            name='f_name',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='sign_up_table',
            name='p_email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sign_up_table',
            name='p_mobile',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sign_up_table',
            name='pincode',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sign_up_table',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='profiles'),
        ),
        migrations.AlterField(
            model_name='sign_up_table',
            name='qualification',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='sign_up_table',
            name='s_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='sign_up_table',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
