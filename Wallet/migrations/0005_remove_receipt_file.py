# Generated by Django 4.0.6 on 2022-08-19 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Wallet', '0004_alter_receipt_first_name_alter_reward_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipt',
            name='file',
        ),
    ]
