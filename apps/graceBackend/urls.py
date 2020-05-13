from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import EntryViewSet, PublicEntries, PublicEntriesDetail

router = DefaultRouter()
router.register('entries', EntryViewSet, basename='entries')

custom_urlpatterns = [
    url(r'^public-entries/$', PublicEntries.as_view(), name='public-entries'),
    url(r'^public-entries/(?P<pk>\d+)/$', PublicEntriesDetail.as_view(), name='public-entry-detail'),
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns
