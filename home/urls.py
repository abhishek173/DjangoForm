from django.urls import path
from .views import index,thankyou


urlpatterns = [
    path('',index),
    path('thank-you/',thankyou),
]

