from django.conf.urls import url, include

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from blog.views import UserViewSet, EntryViewSet, BlogViewSet, StatusView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet)
router.register(r'entries', EntryViewSet)
router.register(r'blogs', BlogViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^status', StatusView.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'xml'])