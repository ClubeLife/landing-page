# Generated by Django 2.0.3 on 2018-03-30 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20180330_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associate',
            name='member_code',
            field=models.CharField(max_length=32, unique=True, verbose_name='código de membro'),
        ),
    ]
