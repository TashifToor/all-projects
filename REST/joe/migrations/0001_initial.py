# Generated by Django 5.2 on 2025-05-03 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('type', models.CharField(choices=[('IT', 'IT'), ('NON-IT', 'NON-IT'), ('MOBILE-USER', 'MOBILE-USER')], max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=70)),
                ('About', models.TextField()),
                ('position', models.CharField(choices=[('IT LEADER', 'IT LEADER'), ('Project Manager', 'Project Manager'), ('Software ENgineer', 'Software Engineer')], max_length=111)),
            ],
        ),
    ]
