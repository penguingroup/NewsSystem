# Generated by Django 2.2.3 on 2019-08-01 14:16

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False, verbose_name='Id')),
                ('title', models.CharField(db_index=True, max_length=256, verbose_name='标题')),
                ('sub_title', models.CharField(default='', max_length=512, null=True, verbose_name='副标题')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='内容')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('category_set', models.ManyToManyField(related_name='category_news_tag', to='Category.Category', verbose_name='分类')),
                ('city_set', models.ManyToManyField(related_name='city_news_tag', to='Category.City', verbose_name='可见城市')),
            ],
            options={
                'verbose_name': '新闻',
                'verbose_name_plural': '新闻',
                'permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
            ],
            options={
                'verbose_name': '活动',
                'verbose_name_plural': '活动',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('Channel.news',),
        ),
    ]
