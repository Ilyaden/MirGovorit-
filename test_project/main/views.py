from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, Recipe, Ingredient
from django.db.models import Q
def add_product_to_recipe(request):
	if request.method == 'GET':
		recipe_id = request.GET.get('recipe_id')
		product_id = request.GET.get('product_id')
		weight = request.GET.get('weight')

		try:
			recipe = get_object_or_404(Recipe, pk=recipe_id)
		except:
			return HttpResponse('Рецепт не найден')

		try:
			product = get_object_or_404(Product, pk=product_id)
		except:
			return HttpResponse('Продукт не найден')


		ingredient = Ingredient.objects.update_or_create(
			recipe=recipe, product=product, defaults={'weight': weight})
		
		return HttpResponse('продукт добавлен в рецепт')

def cook_recipe(request):
	if request.method == 'GET':
	    recipe_id = request.GET.get('recipe_id')
	    try:
	    	recipe = get_object_or_404(Recipe, pk=recipe_id)
	    except:
	    	return HttpResponse('Рецепт не найден')
	    for ingredient in recipe.ingredient_set.all():
	        ingredient.product.times_used += 1
	        ingredient.product.save()

	    return HttpResponse('количество приготовленных блюд увеличено')


def show_recipes_without_product(request):
	if request.method == 'GET':
	    product_id = request.GET.get('product_id')
	    try:
	    	product = get_object_or_404(Product, pk=product_id)
	    except:
	    	return HttpResponse('Продукт не найден')

	    recipes = Recipe.objects.filter(
	        Q(ingredient__product__isnull=True) | Q(ingredient__product__id=product_id, ingredient__weight__lte = 9)
	    )


	    return render(request, 'main/recipes_without_product.html', {'recipes': recipes})
