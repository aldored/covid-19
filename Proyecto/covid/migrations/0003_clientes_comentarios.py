# Generated by Django 3.0.3 on 2020-07-09 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0002_remove_clientes_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='comentarios',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
