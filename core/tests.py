from decimal import Decimal

import pytest

from core.factories import IngredientFactory
from core.models import Recipe, RecipeIngredient


class TestIngredient:
    @pytest.mark.django_db
    def test_ingredient_properties(self):
        # 1 kg of ingredient1 cost 100 euros
        ingredient_1 = IngredientFactory(cost=1000, unit="kg", quantity=1)
        # 1 litre of ingredient2 cost 10 euros
        ingredient_2 = IngredientFactory(cost=10, unit="l", quantity=1)
        assert ingredient_1.quantity_in_si_unit == Decimal(10000)
        assert ingredient_2.quantity_in_si_unit == Decimal(1)
        assert ingredient_1.cost_per_si_unit == Decimal('0.1')
        assert ingredient_2.cost_per_si_unit == Decimal(10)


class TestRecipe:
    @pytest.mark.django_db
    def test_total(self):
        # 1 kg of ingredient1 cost 100 euros
        ingredient_1 = IngredientFactory(cost=100, unit="kg", quantity=1)
        # 1 litre of ingredient2 cost 10 euros
        ingredient_2 = IngredientFactory(cost=10, unit="l", quantity=1)
        recipe = Recipe.objects.create(name="first_recipe")
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient_1, quantity=500, unit="g")
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient_2, quantity=50, unit="cl")

        assert recipe.total == Decimal(55)
