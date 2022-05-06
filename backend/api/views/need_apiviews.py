from django.shortcuts import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ..serializers import OrderSerializer
from ..models import Order
import rest_framework.exceptions as exceptions
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from api.serializers import UserSerializer


class OrderListAPIView(APIView):
    def get(self, request):
        # if not IsAuthenticated.has_permission(self,request,APIView):
        #     raise exceptions.NotAuthenticated
        # else:
        orders = Order.objects.all()
        serializer = OrderSerializer(orders , many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderListByUserAPIView(APIView):
    def get(self,request,pk):
        orders = Order.objects.all().filter()
        needed = []
        for i in orders:
            if i.ordered_by.id == pk:
                needed.append(i)
        serializer = OrderSerializer(needed, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

            token_serializer = JSONWebTokenSerializer(data=serializer.data)
            token = token_serializer.validate(request.data).get('token')
            return Response({'token': token})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
