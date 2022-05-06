from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token
from api.views import *

urlpatterns = [
    path('login/',obtain_jwt_token),
    path('categories/', categories_list),
    path('categories/<int:pk>/dishes/',category_dishes_list),
    path('dishes/',dishes_list),
    path('categories/dishes/<int:pk>',one_dish),
    path('orders',OrderListAPIView.as_view()),
    path('<int:pk>/orders',OrderListByUserAPIView.as_view()),
    path('users',getUsers),
    path('register',RegistrationAPIView.as_view()),
    path('comments',comment_list),
    path('post_comment/',post_comment),
    path('post_order/',post_order)
]