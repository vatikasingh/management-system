# Generated by Django 4.2.3 on 2023-09-16 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_branch_program_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='year',
            old_name='Year',
            new_name='year',
        ),
    ]
