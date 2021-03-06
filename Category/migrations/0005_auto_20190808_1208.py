# Generated by Django 2.2.3 on 2019-08-08 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0004_category_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.SmallIntegerField(choices=[(0, '下线'), (1, '上线')], db_index=True, default=0, null=True, verbose_name='媒体状态'),
        ),
        migrations.AddField(
            model_name='city',
            name='status',
            field=models.SmallIntegerField(choices=[(0, '下线'), (1, '上线')], db_index=True, default=0, null=True, verbose_name='媒体状态'),
        ),
    ]
