# Generated by Django 4.2.6 on 2023-11-19 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='название статьи')),
                ('author', models.CharField(max_length=30, verbose_name='автор статьи')),
                ('iq', models.IntegerField(default=-1, verbose_name='я вумный ггыгыгг')),
            ],
        ),
    ]