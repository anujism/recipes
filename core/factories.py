import factory

from core.models import Ingredient


class IngredientFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: f"Ingredient {n}")
    some_other_field = 10
    another_field = 20
    article_number = factory.Sequence(lambda n: f"Ingredient Number {n}")

    class Meta:
        model = Ingredient
