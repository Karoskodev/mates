# Generated by Django 3.2.23 on 2024-02-23 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_userprofile_user_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_nickname',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]