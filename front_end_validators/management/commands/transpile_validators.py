import subprocess
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):
    help = 'Transpiles Python model field validators to JS using Transcrypt'

    def handle(self, *args, **options):
        try:
            validators_file = settings.VALIDATORS_FILE
        except AttributeError as err:
            raise CommandError('VALIDATORS_FILE setting needs to be defined')
        subprocess.run(['transcrypt', '-b', '-m', validators_file])
        self.stdout.write(self.style.SUCCESS('Successfully transpiled validators'))
