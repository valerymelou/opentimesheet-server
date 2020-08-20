# Generated by Django 3.0.5 on 2020-08-20 20:46

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100, verbose_name='first name')),
                ('last_name', models.CharField(max_length=100, verbose_name='last name')),
                ('hire_date', models.DateField(blank=True, null=True, verbose_name='hire date')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='release date')),
            ],
            options={
                'verbose_name': 'account',
                'verbose_name_plural': 'accounts',
                'ordering': ('first_name', 'last_name'),
            },
        ),
    ]
