# Generated by Django 5.0 on 2024-01-12 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0003_alter_event_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sinup',
            name='partecipant_first_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='sinup',
            name='partecipant_last_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='sinup',
            name='partecipant_phone',
            field=models.CharField(max_length=20),
        ),
    ]
