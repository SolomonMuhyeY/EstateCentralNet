from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from requests import Response
User = get_user_model()
from rest_framework.views import APIView
from rest_framework import permissions

class SignupView(APIView):
  permissions_classes = (permissions.AllowAny,)
  

  def post(self,request,format = None):
    data = self.request.data
    
    name = data['name']
    email = data['email']
    password = data['password']
    password2 = data['password2']
    
    if password == password2:
      if User.objects.filter(email=email).exists():
        return HttpResponse({'error':'Email already exists'})
      else:
        if len(password) < 6:
          return Response({'error':'Password must be atleast 6 characters'})
        else:
          user = User.objects.create_user(email=email,password=password, name = name)
          user.save()
          return Response({'success':'User Created successfully!'})
    else:
      return HttpResponse({'error':'Password do not match'})