from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models import Category,Dish,Comment
from ..serializers import CategorySerializer,DishSerializer , UserSerializer , CommentSerializer,OrderSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User

@api_view(['GET'])
def categories_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

@api_view(['GET','POST'])
def dishes_list(request):
    if request.method == 'GET':
        dishes = Dish.objects.all()
        serializer = DishSerializer(dishes,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def category_dishes_list(request,pk):
    if request.method == 'GET':
        dishes = Dish.objects.all()
        needed = []
        for i in dishes:
            if i.category.id == pk:
                needed.append(i)
        serializer = DishSerializer(needed,many=True)
        return Response(serializer.data)
@api_view(['GET'])
def one_dish(request,pk):
    if request.method == 'GET':
        dish = Dish.objects.get(id = pk)
        serializer = DishSerializer(dish)
        return Response(serializer.data)

@api_view(['GET'])
def getUsers(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def comment_list(request):
    if request.method =='GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments,many=True)
        return Response(serializer.data)

@api_view(['POST'])
def post_comment(request):
    if request.method == 'POST':
        request.data['author_id'] = request.user.pk
        serializer = CommentSerializer(data=request.data)
        print(request.user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def post_order(request):
    if request.method == 'POST':
        request.data['order_by_id'] = request.user.pk
        serializer = OrderSerializer(data=request.data)
        print(request.user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)