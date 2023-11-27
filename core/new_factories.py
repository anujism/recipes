import factory

from core.models import Ingredient


class SomeOtherFactory(factory.django.DjangoModelFactory):
    some_change_added = factory.Sequence(lambda n: f"Some Change {n}")
    name = factory.Sequence(lambda n: f"Ingredient {n}")
    article_number = factory.Sequence(lambda n: f"Ingredient Number {n}")

    class Meta:
        model = Ingredient


class Ingredient2Factory(factory.django.DjangoModelFactory):
    some_change_added = factory.Sequence(lambda n: f"Some Change {n}")
    name = factory.Sequence(lambda n: f"Ingredient {n}")
    article_number = factory.Sequence(lambda n: f"Ingredient Number {n}")

    class Meta:
        model = Ingredient
