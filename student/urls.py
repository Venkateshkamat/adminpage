from django.urls import path
from . import views

urlpatterns = [
    path('studentdata',views.studentdata, name='studentdata'),
]