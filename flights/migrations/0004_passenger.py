# Generated by Django 3.1.1 on 2020-09-20 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_auto_20200919_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='flights.Flight')),
            ],
        ),
    ]
