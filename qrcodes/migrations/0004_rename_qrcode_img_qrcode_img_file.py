# Generated by Django 4.2.5 on 2023-09-30 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qrcodes', '0003_qrcode_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qrcode',
            old_name='qrcode_img',
            new_name='img_file',
        ),
    ]
