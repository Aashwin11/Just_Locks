# Generated by Django 4.2.4 on 2023-08-24 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=122)),
                ('lname', models.CharField(max_length=122)),
                ('dob', models.DateField()),
                ('phone', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=122)),
                ('curr_address', models.CharField(max_length=1000)),
            ],
        ),
    ]
