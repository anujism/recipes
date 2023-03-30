import factory

from core.models import Ingredient


class IngredientFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: f"Ingredient {n}")
    article_number = factory.Sequence(lambda n: f"Ingredient Number {n}")

    class Meta:
        model = Ingredient
