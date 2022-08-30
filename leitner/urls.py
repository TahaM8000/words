from django.urls import path
from .views import *




app_name = "leitner"

urlpatterns = [
    path('test/', test,name="test"),
    path('addLword/<int:id>/', addLword,name="addLword"),
    path('LwShow/', LwShow,name="LwShow"),
]
