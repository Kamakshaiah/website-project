# Generated by Django 4.0.5 on 2022-06-22 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_myuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='image',
            field=models.ImageField(blank=True, default='media/default.jpg', null=True, upload_to='media/'),
        ),
    ]
