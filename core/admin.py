from django.contrib import admin
from django.db.models import Prefetch

from core.models import Ingredient, Recipe, RecipeIngredient


class CustomModelAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        super(CustomModelAdmin, self).__init__(model, admin_site)


@admin.register(Ingredient)
class IngredientAdmin(CustomModelAdmin):
    search_fields = ("name", "article_number")


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    autocomplete_fields = ("ingredient",)
    raw_id_fields = ("ingredient",)
    min_num = 1  # to make sure each recipe has at least one ingredient
    extra = 0
    fields = ["recipe", "ingredient", "quantity", "unit"]

    class Media:
        js = ("/static/core/units_by_ingredients.js",)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeIngredientInline,)
    list_display = ("name", "total")
    readonly_fields = ("total",)  # TODO: we can populate this dynamically later on while user is adding ingredients.
    search_fields = ("name",)

    def get_queryset(self, request):
        # To avoid more number of queries
        return super().get_queryset(request).prefetch_related(
            Prefetch(
                "recipeingredient_set",
                queryset=RecipeIngredient.objects.select_related('ingredient'),
            )
        )
