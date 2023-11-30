from django.db import models
from django.conf import settings


class NewsArticle(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField()
    summary = models.CharField(max_length=255, null=False, blank=False)
    image_url = models.URLField(max_length=1024, blank=False)
    source_url = models.URLField(max_length=1024, blank=False)

    def __str__(self):
        return f"{self.title} - {self.name}"


class Event(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=255, null=False, blank=False)
    image_url = models.URLField(max_length=1024, blank=False)

    def __str__(self):
        return self.name


class EventNotification(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    notification = models.DateField()

    def __str__(self):
        return f"{self.user.name} - {self.event.name}"
