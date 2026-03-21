from django.db import models


class Record26SpDbA2(models.Model):

    class Meta:
        verbose_name = '[26SpDbA2]Record'
        verbose_name_plural = '[26SpDbA2]Records'

    sid = models.CharField(max_length=8)  # type: ignore
    similarity = models.IntegerField(null=True)  # type: ignore
    latency = models.IntegerField(null=True)  # type: ignore
    created_at = models.DateTimeField(auto_now_add=True)  # type: ignore
    updated_at = models.DateTimeField(auto_now=True)  # type: ignore
