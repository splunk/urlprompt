import io
from django.core.management import call_command
from django.test import TestCase


class CreateAPITokenTest(TestCase):
    # TODO: This test currently doesn't really do anything
    def test_command_output(self):
        out = io.StringIO()
        call_command('createapitoken', 'phantom', stdout=out)
        self.assertEqual(out.getvalue(), '')
