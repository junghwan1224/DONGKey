# Generated by Django 2.0.1 on 2018-02-10 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0007_applylist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='position',
        ),
    ]
