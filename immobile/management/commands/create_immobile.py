from django.core.management import BaseCommand

from immobile.factories import ImmobileFactory


class Command(BaseCommand):

    help="Create immobile "

    def add_arguments(self, parser):
        parser.add_argument("number_of_resource", type=int, help="number of immobile to create in system")

    def handle(self, *args, **options):
        number_immobile = options['number_of_resource']
        immobile = ImmobileFactory.create_batch(number_immobile)
        self.stdout.write(f" {len(immobile)} immobile created")