from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'user'

class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()

    class Meta:
        db_table = 'session'

class Event(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

class KeystrokeEvent(Event):
    keystroke = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'keystroke_event'

class TextSelectionEvent(Event):
    selection = models.TextField()
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()

    class Meta:
        db_table = 'text_selection_event'

class MouseHoverEvent(Event):
    html_element = models.TextField()
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()

    class Meta:
        db_table = 'mouse_hover_event'

class MouseMovementEvent(Event):
    start_x_position = models.PositiveSmallIntegerField()
    start_y_position = models.PositiveSmallIntegerField()
    start_html_element = models.TextField()
    end_x_position = models.PositiveSmallIntegerField()
    end_y_position = models.PositiveSmallIntegerField()
    end_html_element = models.TextField()
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()

    class Meta:
        db_table = 'mouse_movement_event'

class MouseClickEvent(Event):
    x_position = models.PositiveSmallIntegerField()
    y_position = models.PositiveSmallIntegerField()
    html_element = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'mouse_click_event'

class MouseScrollEvent(Event):
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()

    class Meta:
        db_table = 'mouse_scroll_event'
