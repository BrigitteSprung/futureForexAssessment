from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from dashboard.models import *


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class DashboardView(generic.DetailView):
    template_name = "dashboard/index.html"

    def get(self, request, *args, **kwargs):
        # Relationship manager is hardset as the first one in the list
        clients = Client.objects.filter(relationshipManager_id=1)
        context = {
            "clients": clients
        }
        return render(request, self.template_name, context)

class ClientView(generic.DetailView):
    template_name = "dashboard/client_page.html"

    def get(self, request, *args, **kwargs):
        id = kwargs['client_id']
        client = Client.objects.get(id=id)
        docRequests = DocumentRequest.objects.filter(client=client)
        context = {
            "client": client,
            "requests": docRequests
        }
        return render(request, self.template_name, context)


class UploadFileView(generic.DetailView):
    template_name = "documents/upload_page.html"

    def get(self, request, *args, **kwargs):
        # Get request ID from kwargs
        id = kwargs['request_id']
        docRequest = DocumentRequest.objects.get(id=id)
        return render(request, self.template_name, {'request': docRequest})

    def post(self, request, *args, **kwargs):
        id = kwargs['request_id']
        docRequest = DocumentRequest.objects.get(id=id)
        docName = docRequest.client.name + " - " + docRequest.type
        document = Document(name=docName, file=request.FILES['filename'], documentRequest=docRequest)
        document.save()
        return HttpResponse("Successful")