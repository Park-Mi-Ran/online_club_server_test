# Generated by Django 3.2.3 on 2021-08-12 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_alter_clubs_club_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubs',
            name='recruitment_content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
