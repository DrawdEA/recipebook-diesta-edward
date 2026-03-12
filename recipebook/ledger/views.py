from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RecipeCreateForm, RecipeImageForm
from .models import Recipe, RecipeImage


def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {"recipes": recipes}
    return render(request, "recipe_list.html", ctx)


@login_required
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    ctx = {"recipe": recipe}
    return render(request, "recipe_detail.html", ctx)


@login_required
def recipe_add(request):
    if request.method == "POST":
        form = RecipeCreateForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            if hasattr(request.user, "profile"):
                recipe.author = request.user.profile
            recipe.save()
            return redirect("ledger:recipe_list")
    else:
        form = RecipeCreateForm()
    return render(request, "recipe_form.html", {"form": form})


@login_required
def recipe_add_image(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            recipe_image = form.save(commit=False)
            recipe_image.recipe = recipe
            recipe_image.save()
            return redirect("ledger:recipe_detail", pk=recipe.pk)
    else:
        form = RecipeImageForm()
    return render(request, "image_form.html", {"form": form, "recipe": recipe})
