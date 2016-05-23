from django.db import models
from core.fields import UnixTimeStampField

class User(models.Model):
    username = models.CharField(max_length=255)

    class Meta:
        db_table = 'user'

class Repository(models.Model):
    owner = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)

    class Meta:
        db_table = 'repository'

class PullRequest(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE, null=True)
    pull_request_number = models.PositiveIntegerField()

    class Meta:
        db_table = 'pull_request'

class Session(models.Model):
    pull_request = models.ForeignKey(PullRequest, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'session'

class EventType(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'event_type'

class ElementType(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'element_type'

class SemanticEvent(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    element_type = models.ForeignKey(ElementType, on_delete=models.CASCADE)
    started_at = UnixTimeStampField(default=0.0)
    duration = models.PositiveIntegerField()

    class Meta:
        db_table = 'semantic_event'

class EventPosition(models.Model):
    event = models.ForeignKey(SemanticEvent, on_delete=models.CASCADE)
    filename = models.FileField(max_length=100)

    class Meta:
        db_table = 'event_position'

class RawEvent(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    created_at = UnixTimeStampField(default=0.0)

    class Meta:
        abstract = True

class KeystrokeEvent(RawEvent):
    keystroke = models.CharField(max_length=255)

    class Meta:
        db_table = 'keystroke_event'

class MousePositionEvent(RawEvent):
    position_x = models.IntegerField()
    position_y = models.IntegerField()
    viewport_x = models.IntegerField()
    viewport_y = models.IntegerField()

    class Meta:
        db_table = 'mouse_position_event'

class MouseClickEvent(RawEvent):

    class Meta:
        db_table = 'mouse_click_event'

class MouseScrollEvent(RawEvent):
    viewport_x = models.IntegerField()
    viewport_y = models.IntegerField()

    class Meta:
        db_table = 'mouse_scroll_event'

class WindowResolutionEvent(RawEvent):
    width = models.IntegerField()
    height = models.IntegerField()

    class Meta:
        db_table = 'window_resolution'
