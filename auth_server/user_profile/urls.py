from django.urls import path
import oauth2_provider.views as oauth2_views


from django.conf import settings
from user_profile import views as p_views


# OAuth2 provider endpoints
urlpatterns = [
    path('authorize/', oauth2_views.AuthorizationView.as_view(), name="authorize"),
    path('token/', oauth2_views.TokenView.as_view(), name="token"),
    path('revoke-token/', oauth2_views.RevokeTokenView.as_view(), name="revoke-token"),
    path("introspect/", oauth2_views.IntrospectTokenView.as_view(), name="introspect"),
    # ----------
    path('users/', p_views.UserList.as_view()),
    path('users/<pk>/', p_views.UserDetails.as_view()),
    path('groups/', p_views.GroupList.as_view()),
]

if settings.DEBUG:
    # OAuth2 Application Management endpoints
    urlpatterns += [
        path('applications/', oauth2_views.ApplicationList.as_view(), name="list"),
        path('applications/register/', oauth2_views.ApplicationRegistration.as_view(), name="register"),
        path('applications/<pk>/', oauth2_views.ApplicationDetail.as_view(), name="detail"),
        path('applications/<pk>/delete/', oauth2_views.ApplicationDelete.as_view(), name="delete"),
        path('applications/<pk>/update/', oauth2_views.ApplicationUpdate.as_view(), name="update"),
    ]

    # OAuth2 Token Management endpoints
    urlpatterns += [
        path('authorized-tokens/', oauth2_views.AuthorizedTokensListView.as_view(), name="authorized-token-list"),
        path('authorized-tokens/<pk>/delete/', oauth2_views.AuthorizedTokenDeleteView.as_view(), name="authorized-token-delete"),
    ]
