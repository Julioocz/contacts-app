# Generated by Django 2.0 on 2017-12-14 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'ordering': ('-primary',)},
        ),
        migrations.AlterModelOptions(
            name='email',
            options={'ordering': ('-primary',)},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ('-modified',)},
        ),
        migrations.AlterModelOptions(
            name='phonenumber',
            options={'ordering': ('-primary',)},
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='info_type',
            field=models.CharField(choices=[('movil', 'movil'), ('personal', 'personal'), ('home', 'home'), ('work', 'work'), ('other', 'other')], default='movil', max_length=255),
        ),
    ]
