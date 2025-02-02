# Generated by Django 5.1.5 on 2025-02-02 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('cantidad', models.PositiveIntegerField(default=0)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
