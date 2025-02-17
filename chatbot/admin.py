from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ChatHistory

class ChatHistoryAdmin(admin.ModelAdmin):
    list_display = ("user", "question", "response", "timestamp")  # Display fields in admin panel
    search_fields = ("user__username", "question", "response")  # Enable search
    list_filter = ("timestamp",)  # Add filtering by date

admin.site.register(ChatHistory, ChatHistoryAdmin)
