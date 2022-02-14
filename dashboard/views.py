from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from dashboard.models import *


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


class ClientsView(generic.DetailView):
    template_name = "dashboard/clients_list.html"

    def get(self, request, *args, **kwargs):
        context = {
            "clients": Client.objects.all()
        }
        return render(request, self.template_name, context)


class RequestView(generic.DetailView):
    template_name = "dashboard/send_request.html"

    def get(self, request, *args, **kwargs):
        # Get request ID from kwargs
        id = kwargs['client_id']
        client = Client.objects.get(id=id)
        context = {
            "client": client,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        id = kwargs['client_id']
        client = Client.objects.get(id=id)
        # Assume Manager ID is one, otherwise include authentication
        manager = RelationshipManager.objects.get(id=1)
        type = request.POST['type']
        email = request.POST['email']
        message = request.POST['message']
        docRequest = DocumentRequest(
            client=client,
            relationshipManager=manager,
            type=type,
            email=email
        )
        docRequest.save()
        url = reverse('upload', args=[docRequest.id])
        full_url = request.build_absolute_uri(url)
        print(full_url)
        upload_button = '<a href="' + url + '" >Upload Here</a>'
        message = message + '\n' + upload_button

        send_mail(
            subject='Document Request',
            message=message,
            html_message=message,
            from_email='brigitte.sprung.dev@gmail.com',
            recipient_list=[email],
            fail_silently=False,
        )
        return redirect(reverse('dashboard'))




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
        docRequest.submitted = True
        docRequest.save()

        message = "Hi {},\n\n A document has been submitted for {}.".format(
            docRequest.relationshipManager.name, docRequest.client.name)
        email = docRequest.relationshipManager.email

        send_mail(
            'Testing',
            message,
            'brigitte.sprung.dev@gmail.com',
            [email],
            fail_silently=False,
        )
        return HttpResponse("Your document has been uploaded successfully.")
