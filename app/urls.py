from django.urls import path
from .views import *

urlpatterns = [
    path('httpresponse/',httpresponse,name='httpresponse'),
    path('jsonresponse/',jsonresponse,name='jsonresponse'),
    path('',not_found_view,name='not_found_view')
]
