# Generated by Django 2.2.3 on 2019-07-04 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_student_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
