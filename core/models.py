import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django_fsm import FSMField, transition
from auditlog.registry import auditlog


class CustomUser(AbstractUser):
    pass

class Prompt(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    schema = models.JSONField()
    response = models.JSONField(null=True, blank=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)

    status = FSMField(default="pending")

    @transition(field=status, source="pending", target="complete")
    def complete(self):
        pass

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        self.clean()

        return super(Prompt, self).save(*args, **kwargs)

auditlog.register(Prompt)
