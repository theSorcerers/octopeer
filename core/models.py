from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)

    class Meta:
        db_table = 'user'

class PullRequest(models.Model):
    created_at = models.DateTimeField()
    merged_at = models.DateTimeField()
    closed_at = models.DateTimeField()

    class Meta:
        db_table = 'pull_request'

class Session(models.Model):
    pull_request = models.ForeignKey(PullRequest, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.CharField(max_length=255, default='GitHub')

    class Meta:
        db_table = 'session'

class EventType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'event_type'

class Event(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    started_at = models.DateTimeField()
    duration = models.PositiveIntegerField()

    class Meta:
        db_table = 'event'

class EventPosition(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    filename = models.FileField(max_length=100)

    class Meta:
        db_table = 'event_position'
