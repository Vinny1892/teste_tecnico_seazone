from decimal import Decimal
import random
import factory
from factory.faker import Faker

from immobile.models import Immobile


class ImmobileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Immobile

    @classmethod
    def generate_random_number(cls):
        while True:
            valor = random.randint(1, 500)
            if not Immobile.objects.filter(code=valor).exists():
                return valor

    code = factory.LazyAttribute(lambda o: ImmobileFactory.generate_random_number())
    quantity_toilet = factory.Faker("random_int", min=1, max=10)
    accept_pet = factory.Faker("pybool")
    activation_date = factory.Faker("date_time_this_decade")
    amount_clean = factory.Faker(
        "pydecimal", left_digits=4, right_digits=2, positive=True
    )
    created_at = factory.Faker("date_time_this_decade")
    updated_at = factory.Faker("date_time_this_month")
