# Generated by Django 5.2.3 on 2025-06-21 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMS_APP', '0004_alter_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]
