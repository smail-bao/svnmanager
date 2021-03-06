# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-02 02:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cronapp', '0003_cron_info_cron_run_user'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cron_info',
            unique_together=set([('cron_status', 'cron_rule', 'cron_cmd', 'cron_service_ip')]),
        ),
        migrations.AlterIndexTogether(
            name='cron_info',
            index_together=set([('cron_status', 'cron_rule', 'cron_cmd', 'cron_service_ip')]),
        ),
    ]
