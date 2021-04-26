from rest_framework.authtoken.models import Token
from core.models import CustomUser
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
import uuid

class Command(BaseCommand):
    help = 'Create a new API token + user'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Name of the user to be created')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        try:
            user = CustomUser.objects.create_user(username=name, email='', password=str(uuid.uuid4()))
            token = Token.objects.create(user=user)
        except:
            user = CustomUser.objects.get(username=name)
            token = Token.objects.get(user=user)
        print(token)
