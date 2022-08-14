from django.urls import path, include

from .views import BlacklistTokenView

urlpatterns = [
    path('', include('djoser.urls.jwt')),
    path('', include('djoser.urls')),
    path('jwt/blacklist/', BlacklistTokenView.as_view(), name="blacklist_token")
]