from django.urls import path, include
from rest_framework.routers import DefaultRouter

from foodrecipe import views


router = DefaultRouter()
# router.register('tags', views.TagViewSet)
# router.register('ingredients', views.IngredientViewSet)
router.register('recipes', views.RecipeViewSet)
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)

app_name = 'foodrecipe'

urlpatterns = [
    path('', include(router.urls))
]
