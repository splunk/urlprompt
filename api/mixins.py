from django.db.models.signals import pre_save
from functools import partial as curry
from auditlog.middleware import threadlocal, AuditlogMiddleware
from auditlog.models import LogEntry
import structlog

logger = structlog.get_logger(__name__)


class DRFDjangoAuditModelMixin:
    """
    Mixin to integrate django-auditlog with Django Rest Framework.

    This is needed because DRF does not perform the authentication at middleware layer
    instead it performs the authentication at View layer.

    This mixin adds behavior to connect/disconnect the signals needed by django-auditlog to auto
    log changes on models.
    It assumes that AuditlogMiddleware is activated in settings.MIDDLEWARE_CLASSES
    """

    def should_connect_signals(self, request):
        """Determines if the signals should be connected for the incoming request."""
        # By default only makes sense to audit when the user is authenticated
        return True

    def initial(self, request, *args, **kwargs):
        """Overwritten to use django-auditlog if needed."""
        super().initial(request, *args, **kwargs)

        user = request.user
        if not user.is_authenticated:
            user = None

        if self.should_connect_signals(request):
            set_actor = curry(AuditlogMiddleware.set_actor, user=user,
                              signal_duid=threadlocal.auditlog['signal_duid'])
            pre_save.connect(set_actor, sender=LogEntry,
                             dispatch_uid=threadlocal.auditlog['signal_duid'], weak=False)

    def finalize_response(self, request, response, *args, **kwargs):
        """Overwritten to cleanup django-auditlog if needed."""
        response = super().finalize_response(request, response, *args, **kwargs)

        if hasattr(threadlocal, 'auditlog'):
            pre_save.disconnect(sender=LogEntry, dispatch_uid=threadlocal.auditlog['signal_duid'])
        return response
