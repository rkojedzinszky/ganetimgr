# -*- coding: utf-8 -*-

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customregistrationprofile',
            name='registrationprofile_ptr',
        ),
        migrations.DeleteModel(
            name='CustomRegistrationProfile',
        ),
    ]
