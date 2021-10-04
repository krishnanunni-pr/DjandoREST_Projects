from django.shortcuts import render
from rest_framework.views import APIView
from todo.models import Todo
from todo.serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins,generics
# Create your views here.

# api/v1/todos (use plurals)
#  api/v1/todos/{id}
# serializers
#  mixins => ListModelMixin =to list all objects
#  CreateModelMixin
#  UpdateModelMixins
#  DestroyModeMisin - delete


class TodoList(APIView):
    model= Todo
    serializer_class = TodoSerializer

    def get(self,request):
        todos = self.model.objects.all()
        serializer =self.serializer_class(todos,many=True)
        return Response(serializer.data,status.HTTP_200_OK)

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class TodoDetail(APIView):
    model = Todo
    serializer_class = TodoSerializer

    def get_object(self,id):
        return self.model.objects.get(id=id)

    def get(self,request,*args,**kwargs):
        todo=self.model.objects.get(id=kwargs['id'])
        # todo=self.modelobjects.get(kwargs["id"])
        serilizer = self.serializer_class(todo)
        return Response(serilizer.data,status=status.HTTP_200_OK)


    def put(self,request,*args,**kwargs):
        todo=self.get_object(kwargs['id'])
        serializer=self.serializer_class(todo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,*args,**kwargs):
        todo=self.get_object(kwargs['id'])
        todo.delete()
        return Response(status=status.HTTP_200_OK)



class TodoMixinList(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):

    model= Todo
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)



class TodoDetailsMixin(generics.GenericAPIView,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin):
    model = Todo
    serializer_class = TodoSerializer
    queryset = model.objects.all()
    lookup_field = "id"

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)