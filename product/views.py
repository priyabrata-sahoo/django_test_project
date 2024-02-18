from django.shortcuts import render
from urllib import response
from django.shortcuts import render,redirect
from rest_framework.response import Response
from .models import Product
from rest_framework.views import APIView
from  .serializers import ProductSerializer
from rest_framework import status
from django.contrib.auth.decorators import login_required
from authentication.permission import IsAuthenticated,IsAdmin

class ProductApi(APIView):
    permission_classes = [IsAdmin]
    def get(self,request,format=None):
        data=Product.objects.all()
        serializer = ProductSerializer(data,many = True)
        serialized_data = serializer.data
        return Response(serialized_data)
    
    def post(self, request, format=None):
        if not request.user.is_staff:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        request.data['user'] = request.user.id
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def test(self):
        pass