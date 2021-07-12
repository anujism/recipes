from django.urls import path

from core.views import units_by_ingredient

app_name = "core"
urlpatterns = [
    path("units-by-ingredient/<int:ingredient_id>", units_by_ingredient, name="units_by_ingredient"),
]
