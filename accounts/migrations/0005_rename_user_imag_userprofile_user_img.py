# Generated by Django 5.0.3 on 2024-03-28 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_userprofile_user_imag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_imag',
            new_name='user_img',
        ),
    ]
