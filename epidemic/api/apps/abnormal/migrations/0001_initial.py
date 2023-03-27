# Generated by Django 4.0.4 on 2022-09-19 00:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Abnormal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created_at')),
                ('modified_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified_at')),
                ('detail', models.CharField(max_length=125, verbose_name='检查详情')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abnormal', to=settings.AUTH_USER_MODEL, verbose_name='记录员')),
            ],
            options={
                'db_table': 'abnormal',
            },
        ),
    ]
