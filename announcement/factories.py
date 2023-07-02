import factory

from announcement.models import Announcement
from immobile.factories import ImmobileFactory


class AnnouncementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Announcement

    tax_platform = factory.Faker(
        "pydecimal", left_digits=3, right_digits=2, positive=True
    )
    name_platform = factory.Faker("company")
    created_at = factory.Faker("date_time_this_decade")
    updated_at = factory.Faker("date_time_this_month")
    immobile = factory.SubFactory(ImmobileFactory)
