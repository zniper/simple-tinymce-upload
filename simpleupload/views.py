from datetime import datetime

from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.files.storage import default_storage
from django.conf import settings


class UploadView(TemplateView):

    template_name = 'simpleupload/dialog.html'

    def post(self, *args, **kwargs):
        file_url = ''
        if self.request.FILES:
            upload_file = self.request.FILES['uploadFile']
            path_prefix = datetime.now().strftime('%y/%m/')
            file_name = default_storage.get_available_name(
                path_prefix + upload_file.name)
            default_storage.save(file_name, upload_file)
            file_url = default_storage.url(file_name)
        return render_to_response(self.template_name, {'file_url': file_url})
