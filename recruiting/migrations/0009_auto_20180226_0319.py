# Generated by Django 2.0.1 on 2018-02-25 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiting', '0008_auto_20180226_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantresume',
            name='is_accepted',
            field=models.BooleanField(default=False, verbose_name='합격 여부'),
        ),
    ]
