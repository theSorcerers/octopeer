from django.db import models
from unixtimestampfield.fields import UnixTimeStampField

class User(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=255)

    class Meta:
        db_table = 'user'

class Repository(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    owner = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)

    class Meta:
        db_table = 'repository'

class PullRequest(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE, null=True)
    pull_request_number = models.PositiveIntegerField()

    class Meta:
        db_table = 'pull_request'

class Session(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    pull_request = models.ForeignKey(PullRequest, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sessions')

    class Meta:
        db_table = 'session'

class EventType(models.Model):
    id = models.PositiveIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'event_type'

class ElementType(models.Model):
    id = models.PositiveIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'element_type'

class SemanticEvent(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='semantic_events')
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    element_type = models.ForeignKey(ElementType, on_delete=models.CASCADE)
    created_at = UnixTimeStampField(default=0.0)

    class Meta:
        db_table = 'semantic_event'

class EventPosition(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    event = models.ForeignKey(SemanticEvent, on_delete=models.CASCADE)
    filename = models.FileField(max_length=100)

    class Meta:
        db_table = 'event_position'

class RawEvent(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class KeystrokeEvent(RawEvent):
    keystroke = models.CharField(max_length=255)
    key_down_at = UnixTimeStampField(default=0.0, null=True)
    key_up_at = UnixTimeStampField(default=0.0, null=True)

    class Meta:
        db_table = 'keystroke_event'

class MousePositionEvent(RawEvent):
    position_x = models.IntegerField()
    position_y = models.IntegerField()
    viewport_x = models.IntegerField()
    viewport_y = models.IntegerField()
    created_at = UnixTimeStampField(default=0.0)

    class Meta:
        db_table = 'mouse_position_event'

class MouseClickEvent(RawEvent):
    created_at = UnixTimeStampField(default=0.0)

    class Meta:
        db_table = 'mouse_click_event'

class MouseScrollEvent(RawEvent):
    viewport_x = models.IntegerField()
    viewport_y = models.IntegerField()
    created_at = UnixTimeStampField(default=0.0)

    class Meta:
        db_table = 'mouse_scroll_event'

class WindowResolutionEvent(RawEvent):
    width = models.IntegerField()
    height = models.IntegerField()
    created_at = UnixTimeStampField(default=0.0)

    class Meta:
        db_table = 'window_resolution_event'

class ChangeTabEvent(RawEvent):
    url = models.URLField(max_length=255)
    created_at = UnixTimeStampField(default=0.0)

    class Meta:
        db_table = 'change_tab_event'
