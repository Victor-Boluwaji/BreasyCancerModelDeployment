# Generated by Django 4.0.6 on 2022-07-28 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PredResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('race_group', models.IntegerField()),
                ('first_degree_hx', models.IntegerField()),
                ('current_hrt', models.IntegerField()),
                ('menopaus', models.IntegerField()),
                ('bmi', models.IntegerField()),
                ('biophx', models.IntegerField()),
                ('status', models.CharField(max_length=300)),
            ],
        ),
    ]