# Generated by Django 4.0.4 on 2024-03-12 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_home_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.CharField(blank=True, max_length=300)),
                ('description', models.TextField(blank=True)),
                ('icon', models.FileField(blank=True, upload_to='images/')),
            ],
        ),
    ]