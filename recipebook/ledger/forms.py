from django import forms
from .models import Recipe, RecipeImage


class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["name"]


class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ["image", "description"]
