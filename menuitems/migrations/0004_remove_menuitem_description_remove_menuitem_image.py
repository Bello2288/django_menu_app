# Generated by Django 4.1.2 on 2022-10-12 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuitems', '0003_rename_author_menuitem_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='description',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='image',
        ),
    ]
