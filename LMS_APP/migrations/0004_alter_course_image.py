# Generated by Django 5.2.3 on 2025-06-21 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMS_APP', '0003_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
