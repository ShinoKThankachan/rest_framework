from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser # type: ignore
from rest_framework.decorators import api_view # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status

# Create your views here.
# def fun(request):
#     return JsonResponse({'name':'riju'})

# def fun1(request):
#     if request.method=='GET':
#         data=student.objects.all()
#         s=studserializer(data,many=True)
#         return JsonResponse(s.data,safe=False)

# @csrf_exempt
# def fun1(request):
#     if request.method=='GET':
#         data=student.objects.all()
#         s=studmodelserializer(data,many=True)
#         return JsonResponse(s.data,safe=False)
#     elif request.method=='POST':
#         d=JSONParser().parse(request)
#         s=studmodelserializer(data=d)
#         print(s)
#         if s.is_valid():
#             s.save()
#             return JsonResponse(s.data,safe=False)
#         else:
#             return JsonResponse(s.errors)


# @csrf_exempt
# def fun1(request,pk):
#     try:
#         demo=student.objects.get(pk=pk)
#         print("helo")
#     except:
#         return HttpResponse("invalid")
#     if request.method=='GET':
#         s=studmodelserializer(demo)
#         return JsonResponse(s.data)
#     elif request.method=='PUT':
#         d=JSONParser().parse(request)
#         s=studmodelserializer(demo,data=d)
#         if s.is_valid():
#             s.save()
#             return JsonResponse(s.data)
#         else:
#             return JsonResponse(s.errors)
#     elif request.method=='DELETE':
#         demo.delete()
#         return HttpResponse("Deleted")

# @api_view(['GET','POST'])
# def fun1(req):
#     if req.method=='GET':
#         d=student.objects.all()
#         s=studmodelserializer(d,many=True)
#         return Response(s.data)

#     elif req.method=='POST':
#         s=studmodelserializer(data=req.data)
#         if s.is_valid():
#             s.save()
#             return JsonResponse(s.data,status=status.HTTP_201_CREATED)
#         else:
#             return JsonResponse(s.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
def fun1(req,pk):
    try:
        demo=student.objects.get(pk=pk)
    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if req.method=='GET':
        s=studmodelserializer(demo)
        return Response(s.data)
    elif req.method=='PUT':
        s=studmodelserializer(demo,data=req.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif req.method=='DELETE':
        demo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



        
