# Generated by Django 3.2 on 2021-12-27 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_write_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select', models.CharField(max_length=100)),
                ('store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.write')),
            ],
        ),
    ]
