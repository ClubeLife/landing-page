# Generated by Django 2.0.3 on 2018-03-30 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180324_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='associate',
            name='member_code',
            field=models.CharField(default='', max_length=32, verbose_name='código de membro'),
            preserve_default=False,
        ),
    ]
