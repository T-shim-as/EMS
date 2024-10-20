# Generated by Django 5.1.2 on 2024-10-19 08:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_rename_time_project_work_time_alter_project_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='start_date',
        ),
        migrations.AddField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 10, 19, 8, 43, 40, 743828, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='is_telework',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='project_period',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('proposal', '提案'), ('offering', '営業中'), ('interview', '面談'), ('waiting', '結果待ち'), ('join', '確定'), ('decline', '辞退')], default='proposal', max_length=20),
        ),
        migrations.AlterField(
            model_name='project',
            name='work_time',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
