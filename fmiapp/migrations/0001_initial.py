# Generated by Django 4.1 on 2022-09-13 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
                ('address', models.TextField()),
                ('contactno', models.CharField(max_length=15)),
                ('emailaddress', models.EmailField(max_length=50)),
                ('enquirytext', models.TextField()),
                ('enquirydate', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='FarmerInfo',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
                ('address', models.TextField()),
                ('contactno', models.CharField(max_length=10)),
                ('aadhaarno', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('regdate', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='LoginInfo',
            fields=[
                ('userid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='MerchantInfo',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
                ('firmname', models.CharField(max_length=100)),
                ('firmaddress', models.TextField()),
                ('contactno', models.CharField(max_length=12)),
                ('emailaddress', models.EmailField(max_length=50)),
                ('aadhaarno', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('panno', models.CharField(max_length=10)),
                ('gstno', models.CharField(max_length=15)),
                ('demand', models.CharField(max_length=20)),
                ('regdate', models.CharField(max_length=30)),
            ],
        ),
    ]
