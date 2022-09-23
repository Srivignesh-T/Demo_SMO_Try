# Generated by Django 4.1.1 on 2022-09-23 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirements',
            name='business_type',
            field=models.CharField(choices=[('B', 'Branding'), ('L', 'Leads'), ('BU', 'Brand unlead')], max_length=100),
        ),
        migrations.AlterField(
            model_name='requirements',
            name='month',
            field=models.CharField(max_length=50),
        ),
    ]