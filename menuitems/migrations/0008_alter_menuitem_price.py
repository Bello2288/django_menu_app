# Generated by Django 4.1.2 on 2022-10-12 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuitems', '0007_alter_menuitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
