# Generated by Django 2.2.3 on 2019-07-02 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_library_sut'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='photo',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
