# Generated by Django 5.1.2 on 2024-10-24 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('url', models.TextField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserPreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
                ('preferred_category', models.CharField(max_length=100)),
            ],
        ),
    ]
