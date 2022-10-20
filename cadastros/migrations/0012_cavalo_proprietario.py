# Generated by Django 4.0.4 on 2022-10-02 04:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cadastros', '0011_cavalo_cidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='cavalo',
            name='proprietario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='cavalo_proprietario', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
