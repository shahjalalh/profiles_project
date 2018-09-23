from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from profiles_api.views import HelloAPIView, HelloViewSet, UserProfileViewSet, LoginViewSet, UserProfileFeedViewSet

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, base_name='hello-viewset')
router.register('profile', UserProfileViewSet)
router.register('login', LoginViewSet, base_name='login')
router.register('feed', UserProfileFeedViewSet)

urlpatterns = [
    url(r'^hello-view/', HelloAPIView.as_view()),
    url(r'', include(router.urls))
]
