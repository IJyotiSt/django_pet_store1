# Generated by Django 4.2.1 on 2023-06-15 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='animal_type',
            field=models.CharField(choices=[('D', 'Dog'), ('C', 'Cat')], default='D', max_length=3),
        ),
    ]
