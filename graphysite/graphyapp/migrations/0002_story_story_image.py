# Generated by Django 3.0.6 on 2020-05-30 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphyapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='story_image',
            field=models.ImageField(default=None, upload_to='storyimages'),
            preserve_default=False,
        ),
    ]
