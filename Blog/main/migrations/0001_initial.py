# Generated by Django 4.2.4 on 2023-08-27 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2048)),
                ('content', models.TextField()),
                ('category', models.CharField(max_length=256)),
                ('publish_date', models.DateTimeField()),
            ],
        ),
    ]
