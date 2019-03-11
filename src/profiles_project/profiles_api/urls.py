from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,base_name = 'hello-viewset') #base name since not modelviewset
router.register('profile', views.UserProfileViewSet) #not have base name since not modelviewset
router.register('login', views.LoginViewSet,base_name = 'login') #base name since not modelviewset
router.register('feed', views.UserProfileFeedViewSet)#not have base name since not modelviewset
urlpatterns = [
    url(r'^hello-view/',views.HelloApiView.as_view()),
    url(r'',include(router.urls))

]
