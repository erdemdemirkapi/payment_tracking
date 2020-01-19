from django.urls import include, path

from mails.views import Mails

urlpatterns = [
    path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('transactions/', include('transactions.urls')),
    path('transactions/', include('transactions.urls')),
    path('send-mail/', Mails.as_view(), name='mails'
]