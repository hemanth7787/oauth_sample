from django.urls import path
from django.http import HttpResponse
from rest_framework.views import APIView
from oauth2_provider.contrib.rest_framework import TokenHasScope
from rest_framework import permissions
from django.contrib import admin


class ApiEndpoint(APIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')


urlpatterns = [
    path('api/hello', ApiEndpoint.as_view()),  # an example resource endpoint
    path('admin/', admin.site.urls),
]
