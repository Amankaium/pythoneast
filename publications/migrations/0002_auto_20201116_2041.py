# Generated by Django 3.1.3 on 2020-11-16 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='publication_pictures', verbose_name='Картинка публикации'),
        ),
    ]
