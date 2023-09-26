# Generated by Django 4.2.3 on 2023-09-24 20:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_blog_views_nums'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipaddress', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP адрес')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='views_nums',
        ),
        migrations.DeleteModel(
            name='ViewNumber',
        ),
        migrations.AddField(
            model_name='blog',
            name='viewers',
            field=models.ManyToManyField(to='blog.viewcount'),
        ),
    ]