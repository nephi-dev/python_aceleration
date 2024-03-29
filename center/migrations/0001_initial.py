# Generated by Django 3.0.7 on 2020-07-13 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=256)),
                ('password', models.CharField(max_length=256)),
                ('token', models.CharField(default='zobgH3PrWguNHmQ0UcPA1iwnu3wqTKdsoup15FlIkYT6rjcqAXHdKlTobaBJeufi5h14dloxQKUgulwZqPKSuAogup40LZk4XHQk9AD1JMvFGgS1smOXGdvswRJWmmUT', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('findWhere', models.CharField(choices=[('D', 'desenvolvimento'), ('H', 'homologação'), ('P', 'produção')], max_length=1)),
                ('level', models.CharField(choices=[('C', 'critical'), ('D', 'debug'), ('E', 'error'), ('I', 'information'), ('W', 'warning')], max_length=1)),
                ('address', models.GenericIPAddressField()),
                ('date', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=256)),
                ('details', models.CharField(max_length=512)),
                ('filed', models.BooleanField()),
                ('quantity', models.IntegerField(default=0)),
                ('findBy', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='center.User')),
            ],
        ),
    ]
