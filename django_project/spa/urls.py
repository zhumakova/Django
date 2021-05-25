from django.urls import path
from .views import homepage,services,masters


urlpatterns=[
    path('', homepage),
    path('services/',services),
    path('masters/',masters)
]

