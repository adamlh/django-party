# Generated by Django 4.2.7 on 2023-12-29 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0002_party_guest_gift'),
    ]

    operations = [
        migrations.RenameField(
            model_name='party',
            old_name='invitiation',
            new_name='invitation',
        ),
    ]
