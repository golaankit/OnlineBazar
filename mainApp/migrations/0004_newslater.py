# Generated by Django 4.1.1 on 2022-10-08 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_checkout_checkoutproducts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newslater',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=50, unique=True)),
            ],
        ),
    ]