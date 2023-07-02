from django.core.management import BaseCommand

from reserve.factories import ReserveFactory


class Command(BaseCommand):

    help="Create Reserve"

    def add_arguments(self, parser):
        parser.add_argument("number_of_resource", type=int, help="number of reserve to create in system")

    def handle(self, *args, **options):
        number_announcement = options['number_of_resource']
        reserves = ReserveFactory.create_batch(number_announcement)
        self.stdout.write(f" {len(reserves)} reserves created")