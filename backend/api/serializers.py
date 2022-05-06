from rest_framework import serializers
from .models import Category,Dish,Comment,Order
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    img = serializers.CharField(max_length=255)

    def create(self, validated_data):
        category = Category.objects.create(id = validated_data.get('id'),name = validated_data.get('name'),img = validated_data.get('img'))

    def update(self, instance, validated_data):
        setattr(instance, 'name', validated_data['name'])
        setattr(instance, 'img', validated_data['img'])
        instance.save()

class DishSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Dish
        fields = ('id','name','cost','description','img','category')

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id','cost','ordered_by','date')

class CommentSerializer(serializers.ModelSerializer):
    # author = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('id','info','author','date')