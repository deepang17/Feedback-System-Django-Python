# Generated by Django 2.1.7 on 2019-04-07 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReviewBeforeYouBuy', '0004_auto_20190407_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notify',
            fields=[
                ('notify_email', models.CharField(max_length=30, primary_key='true', serialize=False)),
            ],
        ),
    ]
