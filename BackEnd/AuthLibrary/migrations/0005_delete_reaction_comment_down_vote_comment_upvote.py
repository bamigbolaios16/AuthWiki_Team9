# Generated by Django 4.0.6 on 2022-08-02 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthLibrary', '0004_authlibrary_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reaction',
        ),
        migrations.AddField(
            model_name='comment',
            name='down_vote',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='upvote',
            field=models.IntegerField(default=0),
        ),
    ]
