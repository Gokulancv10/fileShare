from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from django.conf import settings


APP_STORAGE = default_storage


class Attachment(models.Model):

    thumbnail = models.ImageField(
        null=True, blank=True, height_field=100, width_field=100,
        upload_to="attachment_thumnails"
    )
    name = models.CharField(max_length=200)
    file = models.FileField(storage=APP_STORAGE, upload_to="attachments")
    file_size_kb = models.IntegerField(default=1)
    shareable_url = models.CharField(max_length=200)
    created_by = models.ForeignKey(
        User, null=True, blank=True, related_name="attachments",
        on_delete=models.SET_NULL
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    deleted_on = models.DateTimeField(null=True, blank=True)

    class Meta:
        app_label = "api"
        db_table = "attachment"
        verbose_name = "attachment"
        verbose_name_plural = "attachments"
    
    def __str__(self) -> str:
        return self.name


class AttachmentGroup(models.Model):

    title = models.CharField(max_length=200)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="attachment_groups"
    )
    attachments = models.ManyToManyField(
        Attachment, blank=True, related_name="attachment_group"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = "api"
        db_table = "attachment_group"
        verbose_name = "attachment_group"
        verbose_name_plural = "attachment_groups"
