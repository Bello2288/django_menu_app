# Generated by Django 4.1.2 on 2022-10-13 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuitems', '0008_alter_menuitem_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('phone', models.TextField()),
                ('order', models.JSONField()),
            ],
        ),
    ]