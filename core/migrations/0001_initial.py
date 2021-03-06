# Generated by Django 3.2.5 on 2021-07-12 06:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(choices=[('ug', 'mcg'), ('g', 'gram'), ('short_ton', 'ton'), ('tonne', 'metric tonne'), ('tonne', 'metric ton'), ('oz', 'ounce'), ('lb', 'pound'), ('short_ton', 'short ton'), ('long_ton', 'long ton'), ('yg', 'yoctogram'), ('zg', 'zeptogram'), ('ag', 'attogram'), ('fg', 'femtogram'), ('pg', 'picogram'), ('ng', 'nanogram'), ('ug', 'microgram'), ('mg', 'milligram'), ('cg', 'centigram'), ('dg', 'decigram'), ('dag', 'decagram'), ('hg', 'hectogram'), ('kg', 'kilogram'), ('Mg', 'megagram'), ('Gg', 'gigagram'), ('Tg', 'teragram'), ('Pg', 'petagram'), ('Eg', 'exagram'), ('Zg', 'zetagram'), ('Yg', 'yottagram'), ('us_g', 'US Gallon'), ('mil_us_g', 'Million US Gallons'), ('us_qt', 'US Quart'), ('us_pint', 'US Pint'), ('us_cup', 'US Cup'), ('us_oz', 'US Ounce'), ('us_oz', 'US Fluid Ounce'), ('us_tbsp', 'US Tablespoon'), ('us_tsp', 'US Teaspoon'), ('cubic_millimeter', 'cubic millimeter'), ('cubic_centimeter', 'cubic centimeter'), ('cubic_decimeter', 'cubic decimeter'), ('cubic_meter', 'cubic meter'), ('l', 'liter'), ('l', 'litre'), ('cubic_foot', 'cubic foot'), ('cubic_inch', 'cubic inch'), ('cubic_yard', 'cubic yard'), ('imperial_g', 'Imperial Gram'), ('imperial_qt', 'Imperial Quart'), ('imperial_pint', 'Imperial Pint'), ('imperial_oz', 'Imperial Ounce'), ('imperial_tbsp', 'Imperial Tablespoon'), ('imperial_tsp', 'Imperial Teaspoon'), ('acre_in', 'acre-in'), ('acre_ft', 'acre-ft'), ('acre_ft', 'af'), ('yl', 'yoctoliter'), ('zl', 'zeptoliter'), ('al', 'attoliter'), ('fl', 'femtoliter'), ('pl', 'picoliter'), ('nl', 'nanoliter'), ('ul', 'microliter'), ('ml', 'milliliter'), ('cl', 'centiliter'), ('dl', 'deciliter'), ('dal', 'decaliter'), ('hl', 'hectoliter'), ('kl', 'kiloliter'), ('Ml', 'megaliter'), ('Gl', 'gigaliter'), ('Tl', 'teraliter'), ('Pl', 'petaliter'), ('El', 'exaliter'), ('Zl', 'zetaliter'), ('Yl', 'yottaliter'), ('yl', 'yoctolitre'), ('zl', 'zeptolitre'), ('al', 'attolitre'), ('fl', 'femtolitre'), ('pl', 'picolitre'), ('nl', 'nanolitre'), ('ul', 'microlitre'), ('ml', 'millilitre'), ('cl', 'centilitre'), ('dl', 'decilitre'), ('dal', 'decalitre'), ('hl', 'hectolitre'), ('kl', 'kilolitre'), ('Ml', 'megalitre'), ('Gl', 'gigalitre'), ('Tl', 'teralitre'), ('Pl', 'petalitre'), ('El', 'exalitre'), ('Zl', 'zetalitre'), ('Yl', 'yottalitre')], max_length=32)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(0)])),
                ('name', models.CharField(max_length=256)),
                ('article_number', models.CharField(max_length=256, unique=True)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(choices=[('ug', 'mcg'), ('g', 'gram'), ('short_ton', 'ton'), ('tonne', 'metric tonne'), ('tonne', 'metric ton'), ('oz', 'ounce'), ('lb', 'pound'), ('short_ton', 'short ton'), ('long_ton', 'long ton'), ('yg', 'yoctogram'), ('zg', 'zeptogram'), ('ag', 'attogram'), ('fg', 'femtogram'), ('pg', 'picogram'), ('ng', 'nanogram'), ('ug', 'microgram'), ('mg', 'milligram'), ('cg', 'centigram'), ('dg', 'decigram'), ('dag', 'decagram'), ('hg', 'hectogram'), ('kg', 'kilogram'), ('Mg', 'megagram'), ('Gg', 'gigagram'), ('Tg', 'teragram'), ('Pg', 'petagram'), ('Eg', 'exagram'), ('Zg', 'zetagram'), ('Yg', 'yottagram'), ('us_g', 'US Gallon'), ('mil_us_g', 'Million US Gallons'), ('us_qt', 'US Quart'), ('us_pint', 'US Pint'), ('us_cup', 'US Cup'), ('us_oz', 'US Ounce'), ('us_oz', 'US Fluid Ounce'), ('us_tbsp', 'US Tablespoon'), ('us_tsp', 'US Teaspoon'), ('cubic_millimeter', 'cubic millimeter'), ('cubic_centimeter', 'cubic centimeter'), ('cubic_decimeter', 'cubic decimeter'), ('cubic_meter', 'cubic meter'), ('l', 'liter'), ('l', 'litre'), ('cubic_foot', 'cubic foot'), ('cubic_inch', 'cubic inch'), ('cubic_yard', 'cubic yard'), ('imperial_g', 'Imperial Gram'), ('imperial_qt', 'Imperial Quart'), ('imperial_pint', 'Imperial Pint'), ('imperial_oz', 'Imperial Ounce'), ('imperial_tbsp', 'Imperial Tablespoon'), ('imperial_tsp', 'Imperial Teaspoon'), ('acre_in', 'acre-in'), ('acre_ft', 'acre-ft'), ('acre_ft', 'af'), ('yl', 'yoctoliter'), ('zl', 'zeptoliter'), ('al', 'attoliter'), ('fl', 'femtoliter'), ('pl', 'picoliter'), ('nl', 'nanoliter'), ('ul', 'microliter'), ('ml', 'milliliter'), ('cl', 'centiliter'), ('dl', 'deciliter'), ('dal', 'decaliter'), ('hl', 'hectoliter'), ('kl', 'kiloliter'), ('Ml', 'megaliter'), ('Gl', 'gigaliter'), ('Tl', 'teraliter'), ('Pl', 'petaliter'), ('El', 'exaliter'), ('Zl', 'zetaliter'), ('Yl', 'yottaliter'), ('yl', 'yoctolitre'), ('zl', 'zeptolitre'), ('al', 'attolitre'), ('fl', 'femtolitre'), ('pl', 'picolitre'), ('nl', 'nanolitre'), ('ul', 'microlitre'), ('ml', 'millilitre'), ('cl', 'centilitre'), ('dl', 'decilitre'), ('dal', 'decalitre'), ('hl', 'hectolitre'), ('kl', 'kilolitre'), ('Ml', 'megalitre'), ('Gl', 'gigalitre'), ('Tl', 'teralitre'), ('Pl', 'petalitre'), ('El', 'exalitre'), ('Zl', 'zetalitre'), ('Yl', 'yottalitre')], max_length=32)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(0)])),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.recipe')),
            ],
            options={
                'unique_together': {('recipe', 'ingredient')},
            },
        ),
    ]
