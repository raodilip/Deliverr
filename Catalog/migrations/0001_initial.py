# Generated by Django 3.2.5 on 2021-07-18 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('sku', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=100)),
                ('isDigital', models.BooleanField()),
                ('color', models.CharField(choices=[('RED', 'RED'), ('BLUE', 'BLUE')], max_length=50)),
            ],
            options={
                'ordering': ['product_id'],
            },
        ),
    ]
