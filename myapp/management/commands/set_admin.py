from django.core.management.base import BaseCommand
from myapp.models import Member
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class Command(BaseCommand):
    help = 'Sets a user as admin based on their email (for development purposes only)'

    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help='The email of the user to be set as admin')

    def handle(self, *args, **options):
        email = options['email']

        try:
            validate_email(email)
        except ValidationError:
            self.stdout.write(self.style.ERROR('Invalid email format'))
            return

        try:
            user = Member.objects.get(email=email)
            user.level = 'admin'
            user.is_staff = True
            user.is_superuser = True
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully set user {user.username} as admin'))
        except Member.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'User with email {email} does not exist'))

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('This command is for development purposes only. Do not use in production.'))
        super().handle(*args, **options)