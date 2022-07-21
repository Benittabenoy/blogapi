from django.shortcuts import render


from blogapi.models import posts
from rest_framework.views import APIView
from rest_framework.response import Response

class PostView(APIView):
    def get(self,request,*args,**kwargs):
        return Response(data=posts)
    def post(self,request,*args,**kwargs):
        data=request.data
        posts.append(data)
        return Response(data=data)