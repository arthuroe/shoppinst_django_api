# Generated by Django 2.0.6 on 2018-06-09 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoppinglists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('shoppinglist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppinglists.ShoppingList')),
            ],
        ),
    ]
