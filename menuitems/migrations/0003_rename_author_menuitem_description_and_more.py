# Generated by Django 4.1.2 on 2022-10-12 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuitems', '0002_menuitem_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='author',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='menuitem',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='price',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(null=True, upload_to='menuitems'),
        ),
    ]