from django.contrib import admin
from .models import NewsArticle, Event, EventNotification


admin.site.register(NewsArticle)
admin.site.register(Event)
admin.site.register(EventNotification)
