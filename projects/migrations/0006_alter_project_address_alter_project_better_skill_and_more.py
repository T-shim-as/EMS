# Generated by Django 5.1.2 on 2024-10-19 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_remove_project_end_date_remove_project_start_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='勤務地'),
        ),
        migrations.AlterField(
            model_name='project',
            name='better_skill',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='尚可スキル'),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='作成日時'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(verbose_name='案件詳細'),
        ),
        migrations.AlterField(
            model_name='project',
            name='is_telework',
            field=models.BooleanField(default=False, verbose_name='テレワーク有'),
        ),
        migrations.AlterField(
            model_name='project',
            name='must_skill',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='必須スキル'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=200, verbose_name='案件名'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_period',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='業務期間'),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('proposal', '提案'), ('offering', '営業中'), ('interview', '面談'), ('waiting', '結果待ち'), ('join', '確定'), ('decline', '辞退')], default='proposal', max_length=20, verbose_name='状態'),
        ),
        migrations.AlterField(
            model_name='project',
            name='work_time',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='勤務時間'),
        ),
    ]
