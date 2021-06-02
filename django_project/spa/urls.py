from django.urls import path
from .views import *

urlpatterns=[
    path('', homepage,name="home"),
    path('services/',services,name="services"),
    path('masters/',masters),
    path ('register/',register_page,name='register'),
    path ('login/',login_page,name='login'),
    path('master_detail/<int:master_id>/',master_detail,name='master_detail')

]

