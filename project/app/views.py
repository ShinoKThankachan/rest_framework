from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.
# def fun(request):
#     return JsonResponse({'name':'riju'})

# def fun1(request):
#     if request.method=='GET':
#         data=student.objects.all()
#         s=studserializer(data,many=True)
#         return JsonResponse(s.data,safe=False)

@csrf_exempt
def fun1(request):
    if request.method=='GET':
        data=student.objects.all()
        s=studmodelserializer(data,many=True)
        return JsonResponse(s.data,safe=False)
    elif request.method=='POST':
        d=JSONParser().parse(request)
        s=studmodelserializer(data=d)
        print(s)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data,safe=False)
        else:
            return JsonResponse(s.errors)