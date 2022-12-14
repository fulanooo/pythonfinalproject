

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=40)),
                ('subtitle', models.CharField(max_length=40)),
                ('body', models.TextField()),
                ('author', models.CharField(max_length=40)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('image', models.ImageField(blank=True, null=True, upload_to='pictures')),
            ],
        ),
    ]
