# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccapages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flatpage',
            name='registration_required',
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='template_name',
            field=models.CharField(max_length=70, help_text="Example: 'ccapages/contact_page.html'. If this isn't provided, the system will use 'ccapages/default.html'.", blank=True, verbose_name='template name'),
            preserve_default=True,
        ),
    ]
