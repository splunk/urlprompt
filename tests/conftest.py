import pytest
from core.models import CustomUser, Prompt
import uuid
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token


@pytest.fixture
def api_user_client(api_user):
    token = Token.objects.create(user=api_user)
    api_client = APIClient()
    api_client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

    yield api_client
    token.delete()


@pytest.fixture
def api_user():
    username = "testuser"
    password = str(uuid.uuid4())

    user = CustomUser.objects.create_user(
        username=username, email="", password=password
    )
    yield user
    user.delete()


@pytest.fixture
def anon_user_client():
    api_client = APIClient()
    yield api_client


@pytest.fixture
def admin_user_client():
    username = "testadmin"
    password = str(uuid.uuid4())

    user = CustomUser.objects.create_superuser(
        username=username, email="", password=password
    )
    token = Token.objects.create(user=user)

    api_client = APIClient()
    api_client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

    yield api_client
    user.delete()
    token.delete()


@pytest.fixture
def new_prompt_schema():
    schema = {
        "title": "Convert Investigation 1223 into case",
        "description": "<supplemental information>",
        "type": "object",
        "required": ["approve"],
        "properties": {
            "approve": {"type": "boolean", "title": "Convert to case?"}
        }
    }
    yield schema

@pytest.fixture
def new_prompt(api_user, new_prompt_schema):

    prompt = Prompt.objects.create(schema=new_prompt_schema, created_by=api_user)
    yield prompt

@pytest.fixture
def new_prompt_response():
    response = {"response": {"approve": True}}
    yield response
