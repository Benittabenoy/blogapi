from django.shortcuts import render

# Create your views here.
from rest_framework.views import  APIView
from rest_framework.response import Response

class AddView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        n1=request.data.get("num1")
        n2 = request.data.get("num2")
        res=n1+n2
        return Response({"msg":res})


class subView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        n1 = request.data.get("num1")
        n2 = request.data.get("num2")
        res = n1 - n2
        return Response({"msg": res})
class mulView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        n1 = request.data.get("num1")
        n2 = request.data.get("num2")
        res = n1 * n2
        return Response({"msg": res})

class facView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        num1 = request.data.get("num1")
        fact=1
        for i in range(1,num1+1):
            fact=fact*i
        return Response({"msg": fact})
class wordView(APIView):
    def post(self,request,*args,**kwargs):
        text=request.data.get("text")
        words=text.split("")
        wc={}
        for w in words:
            if w in wc:
                wc[w]+=1
            else:
                wc[w]=1
                return Response(data=wc)