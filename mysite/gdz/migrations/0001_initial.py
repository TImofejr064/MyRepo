# Generated by Django 3.0.2 on 2020-01-15 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.TextField()),
                ('number_of_task', models.IntegerField(max_length=5)),
                ('image', models.ImageField(upload_to='image_solution')),
            ],
        ),
    ]