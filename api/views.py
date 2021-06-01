import structlog
from core.models import Prompt
from core.permissions import IsAdminUser
from django.utils.decorators import method_decorator
from django_fsm import can_proceed
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import PromptResponseSerializer, PromptSerializer

logger = structlog.get_logger(__name__)


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_id="List Prompts",
        operation_description="Lists all Prompts. Requires admin-level permissions.",
    ),
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(operation_id="Get Prompt", security=[]),
)
@method_decorator(
    name="destroy", decorator=swagger_auto_schema(operation_id="Delete Prompt")
)
class PromptViewSet(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):

    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer
    permission_classes = []
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.action in ["partial_update", "retrieve"]:
            self.permission_classes = []

        elif self.action in ["list", "update", "destroy"]:
            self.permission_classes = [
                IsAuthenticated,
                IsAdminUser,
            ]

        elif self.action in ["create"]:
            self.permission_classes = [IsAuthenticated]

        return super(self.__class__, self).get_permissions()

    def get_serializer_class(self):
        if self.action in ["partial_update"]:
            return PromptResponseSerializer
        return PromptSerializer

    @swagger_auto_schema(operation_id="Create Prompt")
    def create(self, request, *args, **kwargs):
        """Create a new Prompt instance"""

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @swagger_auto_schema(operation_id="Patch Prompt", security=[])
    def partial_update(self, request, *args, **kwargs):
        """Patch an existing prompt instance"""

        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)

        if not can_proceed(instance.complete):
            raise ValidationError(
                "Cannot update prompt since it is already in completed state."
            )

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            instance.complete()
            instance.save()
            print(serializer.validated_data)
            return Response(serializer.data)


class TokenView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {"user": str(request.user), "auth": str(request.auth)}

        return Response(content)
