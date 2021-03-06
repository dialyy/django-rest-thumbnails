from django.conf import settings
from django.conf.urls.defaults import patterns, url

from restthumbnails.defaults import URL_REGEX
from restthumbnails.views import ThumbnailView


urlpatterns = patterns('',
    url(regex=URL_REGEX,
        view=ThumbnailView.as_view(),
        name="get_thumbnail"))
