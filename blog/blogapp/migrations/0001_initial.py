# Generated by Django 4.1.4 on 2023-04-05 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='image')),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=10000)),
            ],
        ),
    ]
