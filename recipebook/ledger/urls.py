from django.urls import path

from . import views

app_name = 'ledger'

urlpatterns = [
    path("recipes/list/", views.recipe_list, name="recipe_list"),
    path("recipe/add/", views.recipe_add, name="recipe_add"),
    path("recipe/<int:pk>/", views.recipe_detail, name="recipe_detail"),
    path("recipe/<int:pk>/add_image/", views.recipe_add_image, name="recipe_add_image"),
]