from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """Test Api View"""
    def get(self,request,format=None):
        """Return a list of APiview features"""

        an_apiview=[
        'Uses HTTP method as function(get,post,patch,put,delete)',
        'It is similar to a traditional Django view',
        'Gives ypu the most control over your logic',
        'Is mapped manually to URLS'
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})
