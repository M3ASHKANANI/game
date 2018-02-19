# Generated by Django 2.0.2 on 2018-02-19 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('release_date', models.DateField()),
                ('platforms', models.CharField(max_length=220, null=True)),
                ('multiplayer', models.BooleanField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]