# Generated by Django 2.2.3 on 2019-08-02 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Channel', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'permissions': [('beijing', '北京'), ('shanghai', '上海'), ('guangzhou', '广州'), ('shenzhen', '深圳'), ('wuhan', '武汉'), ('politic', '时政'), ('entertainment', '娱乐'), ('technology', '科技'), ('hot', '热点'), ('life', '生活')], 'verbose_name': '新闻', 'verbose_name_plural': '新闻'},
        ),
    ]