# Generated by Django 4.2.1 on 2023-06-15 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_pet_animal_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='description',
            field=models.CharField(default=' ', max_length=70),
            preserve_default=False,
        ),
    ]
