from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import StudentSerializer,StandardSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Student,Standard
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

# Create your views here.
class StudentAPIView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data})
        else:
            return Response({'error': serializer.errors},status=status.HTTP_400_BAD_REQUEST)


    def get(self,request,*args,**kwargs):
        qs=Student.objects.all()
        serializer=StudentSerializer(qs,many=True)
        return Response({'data':serializer.data})


    def put(self,request,*args,**kwargs):
        pk=kwargs.get('pk')
        instance=Student.objects.get(id=pk)
        serializer=StudentSerializer(instance=instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data})
        else:
            return Response({'error': serializer.errors},status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,*args,**kwargs):
        pk=kwargs.get('pk')
        instance=Student.objects.get(id=pk)
        instance.delete()
        return Response({'message':'The object has been deleted'})



class StandardAPIView(CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    serializer_class = StandardSerializer
    queryset = Standard.objects.all()
