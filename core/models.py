from decimal import Decimal, ROUND_UP

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.functional import cached_property
from measurement.measures import Weight, Volume
from measurement.utils import guess

SUPPORTING_MEASURES = [Weight, Volume]


def get_unit_choices(supporting_measures=None):
    supporting_measures = supporting_measures or SUPPORTING_MEASURES
    return (
        (short_unit, long_unit)
        for measure in supporting_measures
        for long_unit, short_unit in measure.get_aliases().items()
    )


class AbstractMeasurementModel(models.Model):
    # TODO: instead of a model, we can make this a MeasurementField to keep it more transparent.
    unit = models.CharField(max_length=32, choices=get_unit_choices())
    quantity = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])

    class Meta:
        abstract = True

    @property
    def measure_obj(self):
        # this may return wrong value if there is overlapping measures but for current use case it's fine.
        return guess(self.quantity, self.unit, measures=SUPPORTING_MEASURES)

    @property
    def quantity_in_si_unit(self):
        # SI units are better to understand than standard units. Assuming all measures will have SI_UNITS length >= 1
        measure_obj = self.measure_obj
        return getattr(measure_obj, measure_obj.SI_UNITS[0])


class Ingredient(AbstractMeasurementModel):
    name = models.CharField(max_length=256)
    article_number = models.CharField(max_length=256, unique=True)
    # this can be modified based on requirement - we can adjust decimal places
    # TODO: we can make this as MoneyField to support multiple currencies
    cost = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name

    @property
    def cost_per_si_unit(self):
        # measurements library use Float so we are converting to decimal
        return self.cost/Decimal(self.quantity_in_si_unit)


class Recipe(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    @cached_property
    def total(self):
        total_amount = Decimal(0)
        for recipe_ingredient in self.recipeingredient_set.all():
            # Get cost per standard unit and multiply by quantity in standard unit from recipe
            total_amount += (
                Decimal(recipe_ingredient.quantity_in_si_unit) * recipe_ingredient.ingredient.cost_per_si_unit
            )
        # we can modify as per requirement
        return total_amount.quantize(Decimal('.01'), rounding=ROUND_UP)


class RecipeIngredient(AbstractMeasurementModel):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)

    class Meta:
        unique_together = ("recipe", "ingredient",)
