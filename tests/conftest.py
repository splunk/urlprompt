from rest_framework.test import APIRequestFactory
import pytest
from core.models import CustomUser
import uuid
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

@pytest.fixture
def api_user_client():
    username = "testuser"
    password = str(uuid.uuid4())

    user = CustomUser.objects.create_user(username=username, email='', password=password)
    token = Token.objects.create(user=user)
    api_client = APIClient()
    api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    yield api_client
    user.delete()
    token.delete()

@pytest.fixture
def anon_user_client():
    api_client = APIClient()
    yield api_client

@pytest.fixture
def admin_user_client():
    username = "testadmin"
    password = str(uuid.uuid4())

    user = CustomUser.objects.create_superuser(username=username, email='', password=password)
    token = Token.objects.create(user=user)

    api_client = APIClient()
    api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    yield api_client
    user.delete()
    token.delete()
