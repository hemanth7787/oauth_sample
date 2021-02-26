from django.contrib import admin
from django.urls import path, include
from user_profile.views import ApiEndpoint


urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include(('user_profile.urls', 'profile'), namespace="oauth2_provider")),
    path('api/hello', ApiEndpoint.as_view()),  # an example resource endpoint
]