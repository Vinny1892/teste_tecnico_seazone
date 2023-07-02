from django.core.management import BaseCommand

from announcement.factories import AnnouncementFactory
from immobile.factories import ImmobileFactory


class Command(BaseCommand):

    help="Create Announcement "

    def add_arguments(self, parser):
        parser.add_argument("number_of_resource", type=int, help="number of announcement to create in system")

    def handle(self, *args, **options):
        number_announcement = options['number_of_resource']
        announcements = AnnouncementFactory.create_batch(number_announcement)
        self.stdout.write(f" {len(announcements)} announcements created")