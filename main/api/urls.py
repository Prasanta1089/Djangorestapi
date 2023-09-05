from django.urls import path , include
from home.views import index , person , login, PersonAPI , PeopleViewSet , RegisterAPI , LoginApi
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'people' , PeopleViewSet , basename='people')

urlpatterns = [
    path('' , include(router.urls)),
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginApi.as_view()),
    path('index/', index),
    path('person/', person),
    path('login/', login),
    path('persons/', PersonAPI.as_view())
]
