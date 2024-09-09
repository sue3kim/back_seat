# Generated by Django 5.0.3 on 2024-09-09 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stop_name', models.CharField(default='정류장이름', max_length=100)),
                ('location', models.CharField(default='위치', max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='bus',
            name='route',
        ),
        migrations.RemoveField(
            model_name='seat',
            name='is_occupied',
        ),
        migrations.AddField(
            model_name='bus',
            name='route_name',
            field=models.CharField(default='노선정보', max_length=100),
        ),
        migrations.AddField(
            model_name='seat',
            name='status',
            field=models.CharField(choices=[('available', 'Available'), ('occupied', 'Occupied')], default='available', max_length=10),
        ),
        migrations.AlterField(
            model_name='bus',
            name='bus_number',
            field=models.CharField(default='버스번호', max_length=10),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seat_number',
            field=models.CharField(default='좌석', max_length=10),
        ),
    ]
