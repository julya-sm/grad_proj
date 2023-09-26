# Generated by Django 4.2.3 on 2023-09-15 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-time_created'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'verbose_name': 'Тема', 'verbose_name_plural': 'Темы'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Лого темы'),
        ),
        migrations.CreateModel(
            name='ViewNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP address')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]