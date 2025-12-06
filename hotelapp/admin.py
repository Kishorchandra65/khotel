from django.contrib import admin
from .models import Hotel, Room, ContactMessage

admin.site.register(Hotel)
admin.site.register(ContactMessage)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price_per_night', 'capacity', 'available')
    list_filter = ('category', 'available')
