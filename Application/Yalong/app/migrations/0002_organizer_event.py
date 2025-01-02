import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('Organizer_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=120)),
                ('Contact_Information', models.CharField(max_length=120)),
                ('Role', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('Event_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Event_Name', models.CharField(max_length=120)),
                ('Description', models.TextField(max_length=500)),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('Location', models.CharField(max_length=200)),
                ('Category', models.CharField(max_length=200)),
                ('Status', models.CharField(max_length=200)),
                ('Budget', models.FloatField()),
                ('OrganizerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.organizer')),
            ],
        ),
    ]
