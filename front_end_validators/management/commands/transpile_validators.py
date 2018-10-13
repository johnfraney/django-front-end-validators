import os
import subprocess
from django.core.exceptions import ImproperlyConfigured
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):
    help = 'Transpiles Python model field validators to JS using Transcrypt'

    def handle(self, *args, **options):
        try:
            validators_file = settings.VALIDATORS_FILE
        except AttributeError as err:
            raise CommandError('VALIDATORS_FILE setting needs to be defined')

        validators_file_basename = os.path.basename(validators_file)

        if not validators_file_basename == 'validators.py':
            error_text = (
                'VALIDATORS_FILE setting must point to a file named validators.py. '
                'Your file:\n{}'.format(validators_file_basename)
            )
            raise CommandError(error_text)

        if not os.path.exists(validators_file):
            raise CommandError('validators.py file could not be found: {}'.format(
                validators_file
            ))

        subprocess.run(['transcrypt', '-b', '-m', validators_file])
        self.stdout.write(self.style.SUCCESS('Successfully transpiled validators'))
