from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PublicEntries, PublicEntriesDetail, CreateEntry

urlpatterns = [
    url(r'^create-entry/$', CreateEntry.as_view(), name='create-entry'),
    url(r'^public-entries/$', PublicEntries.as_view(), name='public-entries'),
    url(r'^public-entries/(?P<pk>\d+)/$', PublicEntriesDetail.as_view(), name='public-entry-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

