from django.contrib import admin
from django.urls import path
from oauth2_provider.contrib.rest_framework import TokenHasScope
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.apis.r2_api import R2Api


class ApiEndpoint(APIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']

    def get(self, request, *args, **kwargs):
        # print(f"Token: {request.auth.token}, scopes: {str(request.auth.scope).split(' ')}")
        # return data from another microservice
        api = R2Api(token=request.auth.token)
        return Response(api.user_list())


urlpatterns = [
    path('api/hello', ApiEndpoint.as_view()),  # an example resource endpoint
    path('admin/', admin.site.urls),
]
