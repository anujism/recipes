from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse

from core.models import Ingredient, get_unit_choices


@staff_member_required
def units_by_ingredient(request, ingredient_id=None):
    # TODO: handle wrong ingredient_id
    ingredient = Ingredient.objects.get(id=ingredient_id)
    unit_choices = get_unit_choices(supporting_measures=[ingredient.measure_obj])
    return JsonResponse({
        "unit_choices": list(unit_choices),
    })
