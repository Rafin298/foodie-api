from rest_framework import serializers

from foodrecipe.models import Recipe, Tag, Ingredient

# from core.models import Tag, Ingredient, Recipe


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for ingredient objects"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)


# class RecipeSerializer(serializers.ModelSerializer):
#     """Serialize a recipe"""
#     # ingredients = serializers.PrimaryKeyRelatedField(
#     #     many=True,
#     #     queryset=Ingredient.objects.all()
#     # )
#     # tags = serializers.PrimaryKeyRelatedField(
#     #     many=True,
#     #     queryset=Tag.objects.all()
#     # )

#     class Meta:
#         model = Recipe
#         # fields = (
#         #     'id', 'title', 'ingredients', 'tags', 'time_minutes',
#         #     'price', 'link'
#         # )
#         fields = (
#             'id', 'title', 'time_minutes',
#             'price', 'link'
#         )
#         read_only_fields = ('id',)

class RecipeSerializer(serializers.ModelSerializer):
    """Serialize a recipe"""
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingredient.objects.all()
    )
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Recipe
        fields = (
            'id', 'title', 'ingredients', 'tags', 'time_minutes',
            'price', 'link'
        )
        read_only_fields = ('id',)

# class RecipeDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Recipe
#         # fields = (
#         #     'id', 'title', 'ingredients', 'tags', 'time_minutes',
#         #     'price', 'link'
#         # )
#         fields = (
#             'id', 'title', 'time_minutes',
#             'price', 'link'
#         )
#         read_only_fields = ('id',)
# #     """Serialize a recipe detail"""
# #     ingredients = IngredientSerializer(many=True, read_only=True)
# #     tags = TagSerializer(many=True, read_only=True)


class RecipeDetailSerializer(RecipeSerializer):
    """Serialize a recipe detail"""
    ingredients = IngredientSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)


class RecipeImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images to recipes"""

    class Meta:
        model = Recipe
        fields = ('id', 'image')
        read_only_fields = ('id',)

# class TagSerializer(serializers.ModelSerializer):
#     """Serializer for tag objects"""

#     class Meta:
#         model = Tag
#         fields = ('id', 'name')
#         read_only_fields = ('id',)
