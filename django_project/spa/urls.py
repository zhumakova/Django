from django.urls import path
from .views import *


urlpatterns=[
    path('', homepage,name="home"),
    path('services/',services),
    path('masters/',masters),
    path ('register/',register_page),
    path ('login/',login_page,name='login'),
    path('master_detail/<int:master_id>/',master_detail,name='master_detail')

]

