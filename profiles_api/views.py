from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets


from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class= serializers.HelloSerializer
    def get(self ,request , format = None):
        """Returns a list of APIView features"""
        an_apiview = [
        'Uses HTTP methods as function (get,post,put,patch,delete)',
        'Is similar to a traditional Django View',
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self,request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message,})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self , request , pk=None):
        return Response({'method' : 'PUT'})

    def patch(self , request , pk=None):
        return Response({'method' : 'PATCH'})

    def delete(self , request , pk=None):
        return Response({'method' : 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    serializer_class= serializers.HelloSerializer

    def list(self, request):
        a_viewset = [
        'Uses actions (list,create,retrieve,update,partial_update)',
        ]

        return Response({'message':'Hello!','an_apiview':a_viewset})

    def create(self,request):
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        return Response({"http method " : "GET"})

    def update(self,request,pk=None):
        return Response({"http method " : "PUT"})

    def partial_update(self,request,pk=None):
        return Response({"http method " : "PATCH"})

    def destroy(self,request,pk=None):
        return Response({"http method " : "DELETE"})
