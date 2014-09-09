from django.conf.urls import patterns, url

from views import UploadView

urlpatterns = patterns('',
    url('^simple-upload/$', UploadView.as_view(), name='simpleupload-view'),
)
    
