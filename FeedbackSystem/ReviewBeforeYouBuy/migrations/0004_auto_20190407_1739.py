# Generated by Django 2.1.7 on 2019-04-07 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ReviewBeforeYouBuy', '0003_cameras_feedback_computer_hardware_feedback_electronic_accessory_feedback_laptop_feedback_mobile_fee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cameras',
            name='c_feedback_link',
        ),
        migrations.RemoveField(
            model_name='computer_hardware',
            name='h_feedback_link',
        ),
        migrations.RemoveField(
            model_name='electronic_accessory',
            name='e_feedback_link',
        ),
        migrations.RemoveField(
            model_name='laptop',
            name='l_feedback_link',
        ),
        migrations.RemoveField(
            model_name='mobile',
            name='m_feedback_link',
        ),
        migrations.RemoveField(
            model_name='smart_watches',
            name='s_feedback_link',
        ),
    ]