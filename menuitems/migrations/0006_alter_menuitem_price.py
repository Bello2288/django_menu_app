# Generated by Django 4.1.2 on 2022-10-12 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuitems', '0005_menuitem_description_menuitem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.IntegerField(max_length=255, null=True),
        ),
    ]
