# Generated by Django 3.2.5 on 2022-11-05 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eviction_scraper', '0006_alter_evictionrecord_case_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evictionrecord',
            options={'managed': False},
        ),
    ]
