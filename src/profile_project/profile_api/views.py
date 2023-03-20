from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
# Create your views here.
class HelloApiView(APIView):
    """Test Api View"""

    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        """Return a list of APiview features"""

        an_apiview=[
        'Uses HTTP method as function(get,post,patch,put,delete)',
        'It is similar to a traditional Django view',
        'Gives ypu the most control over your logic',
        'Is mapped manually to URLS'
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self,request):
        """Create a hello meassage with our name"""
        serializer=serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            message="Hello {0}".format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Handles updating an object"""
        return Response({'method':'put'})

    def patch(self,request,pk=None):
        """Patch request,only updates fields provided in the request"""
        return Response({'method':'patch'})

    def delete(self,request,pk=None):
        """deletes an object"""
        return Response({'method':'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""

    serializer_class=serializers.HelloSerializer

    def list(self,request):
        """return a hello message"""
        a_viewset=[
            'uses action(list,create,retrieve,update,partial_update)',
            'automatically maps to urls using routers',
            'provides more functionality with less code'
        ]
        return Response({'message':'hello','a_viewset':a_viewset})

    def create(self,request):
        """Create new hello message"""
        serializer=serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            message='Hello {0}'.format(name)
            return Response({'message':message})

        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        """handles getting an object by its id"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """handles updating an object"""
        return Response({'http_method':"PUT"})

    def partial_update(self,request,pk=None):
        """handles updating part of an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """Deleting an object"""
        return Response({'http_method':'DELETE'})
