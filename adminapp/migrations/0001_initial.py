# Generated by Django 4.1 on 2022-09-13 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('name', models.CharField(max_length=40)),
                ('address', models.TextField()),
                ('contactno', models.CharField(max_length=10)),
                ('aadhaarno', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('noofpacket', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('totalamt', models.IntegerField()),
                ('advance', models.IntegerField()),
                ('restamt', models.IntegerField()),
                ('bookingdate', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='mBooking',
            fields=[
                ('name', models.CharField(max_length=14)),
                ('firmname', models.CharField(max_length=100)),
                ('firmaddress', models.TextField()),
                ('contactno', models.CharField(max_length=10)),
                ('aadhaarno', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('panno', models.CharField(max_length=10)),
                ('gstno', models.CharField(max_length=15)),
                ('demand', models.CharField(max_length=20)),
                ('ninkg', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('totalamt', models.IntegerField()),
                ('advance', models.IntegerField()),
                ('restamt', models.IntegerField()),
                ('bookingdate', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newstext', models.TextField()),
                ('newsdate', models.CharField(max_length=30)),
            ],
        ),
    ]