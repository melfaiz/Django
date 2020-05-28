# Generated by Django 3.0.6 on 2020-05-26 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaussian', '0003_data'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Data',
        ),
        migrations.AddField(
            model_name='point',
            name='y',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
    ]