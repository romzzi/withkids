# Generated by Django 3.2 on 2022-03-02 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_google_filtering'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='google',
            name='filtering',
        ),
    ]