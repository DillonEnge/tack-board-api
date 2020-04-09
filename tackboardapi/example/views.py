from django.shortcuts import render
from django.http import HttpResponse
from oauth2_provider.views.generic import ProtectedResourceView

class TestEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello w/ OAuth2!')

def index(request):
    return HttpResponse("Welcome to the example index!")
