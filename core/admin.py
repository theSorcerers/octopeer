from django.contrib import admin

from .models import User, Session, KeystrokeEvent, TextSelectionEvent, MouseHoverEvent, MouseMovementEvent, MouseClickEvent, MouseScrollEvent

admin.site.register(User)
admin.site.register(Session)
admin.site.register(KeystrokeEvent)
admin.site.register(TextSelectionEvent)
admin.site.register(MouseHoverEvent)
admin.site.register(MouseMovementEvent)
admin.site.register(MouseClickEvent)
admin.site.register(MouseScrollEvent)
