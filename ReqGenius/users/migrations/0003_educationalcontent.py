# Generated by Django 5.0.7 on 2024-08-20 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_supportticket'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationalContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField(max_length=500)),
            ],
        ),
    ]
