# Generated by Django 4.0.6 on 2022-07-07 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(blank=True, height_field=100, null=True, upload_to='attachment_thumnails', width_field=100)),
                ('name', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='attachments')),
                ('file_size_kb', models.IntegerField(default=1)),
                ('shareable_url', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deleted_on', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attachments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'attachment',
                'verbose_name_plural': 'attachments',
                'db_table': 'attachment',
            },
        ),
        migrations.CreateModel(
            name='AttachmentGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('attachments', models.ManyToManyField(blank=True, related_name='attachment_group', to='api.attachment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachment_groups', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'attachment_group',
                'verbose_name_plural': 'attachment_groups',
                'db_table': 'attachment_group',
            },
        ),
    ]
