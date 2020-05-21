# Generated by Django 3.0.5 on 2020-05-21 17:58

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import opentimesheet.utils.storages


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('logo', models.ImageField(blank=True, upload_to=opentimesheet.utils.storages.upload_to, verbose_name='Logo')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this organization should be treated as active', verbose_name='Active')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]