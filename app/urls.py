from django.urls import path
from .views import *

urlpatterns = [
    # path('httpresponse/',httpresponse,name='httpresponse'),
    # path('jsonresponse/',jsonresponse,name='jsonresponse'),
    # path('',not_found_view,name='not_found_view')
    path('',index,name='index'),
    path('home_page/',home_page,name='home_page'),
    path('expense_register/',expense_register,name='expense_register'),
    path('delete_expense/',delete_expense,name='delete_expense'),

    path("register/", register, name="register"),
    path("login/", login_page, name="login"),
    path("logout/", logout, name="logout"),
        


]
