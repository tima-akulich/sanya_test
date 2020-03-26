from django.urls import path

from my_app.views import SomeModelListAPIView
from my_app.views import SomeModelRetrieveAPIView

urlpatterns = [
    path('users', SomeModelListAPIView.as_view(), name='users.list'),
    path('users/<int:pk>', SomeModelRetrieveAPIView.as_view(), name='users.retrieve'),  # noqa
]
