# Generated by Django 4.0.4 on 2024-03-12 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_image_research'),
    ]

    operations = [
        migrations.AddField(
            model_name='research',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]