import uuid
from datetime import datetime

import factory

from announcement.factories import AnnouncementFactory
from reserve.models import Reserve


class ReserveFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reserve

    code = factory.LazyAttribute(lambda x: uuid.uuid4())
    quantity_guests = factory.Faker("random_int", min=1, max=10)
    total_price = factory.Faker(
        "pydecimal", left_digits=4, right_digits=2, positive=True
    )
    comment = factory.Faker("sentence", nb_words=6)
    check_in = factory.Faker("date_time_this_year", before_now=True, after_now=False)
    check_out = factory.Faker("date_time_this_year", before_now=False, after_now=True)
    created_at = factory.LazyFunction(datetime.now)
    updated_at = factory.LazyFunction(datetime.now)
    announcement = factory.SubFactory(AnnouncementFactory)
