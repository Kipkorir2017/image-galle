from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    url('^$',views.displayhome,name = 'welcome'),
    url(r'^search/', views.search_category, name='search_category'),
    url('^image/(?P<image_id>\d+)/$',views.image_properties, name='image'),
    url(r'^location/(?P<location_name>\w+)',views.image_location,name = 'location'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
