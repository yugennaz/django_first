# Generated by Django 2.1.7 on 2019-04-08 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_first', '0004_auto_20190408_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
