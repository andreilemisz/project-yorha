# Generated by Django 5.1 on 2024-08-21 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_log', '0002_contact_position_alter_contact_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='first_name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='contact',
            name='position',
            field=models.CharField(max_length=50),
        ),
    ]
