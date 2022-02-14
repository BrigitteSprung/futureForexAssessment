from django.db import models


# Create your models here.
class RelationshipManager(models.Model):
    """
    RelationshipManager Object
    """
    name = models.CharField(max_length=1028)
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=254, default='brigittesprung@gmail.com')

    def __str__(self):
        return self.name


class Client(models.Model):
    """
    Client Object

    Attributes:
    ----------
    """
    name = models.CharField(max_length=1028)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=254, default='brigittesprung@gmail.com')
    relationshipManager = models.ForeignKey(RelationshipManager, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    def getDocuments(self):
        return Document.objects.filter(client=self)

    def getOutstandingDocuments(self):
        # Get all the outstanding requests
        return DocumentRequest.objects.filter(client=self, submitted=False)


    def getNumOutstandingDocuments(self):
        # Get the number of requests outstanding
        return len(DocumentRequest.objects.filter(client=self, submitted=False))


class DocumentRequest(models.Model):
    """
      Document Request Object
      Document Request created by RM

      Attributes:
      ----------
      name : CharField
          name of the file
      email : EmailField
          where to send the request
      upload_date: DateTimeField
          date the file was uploaded
      client:
          user who uploaded the file
      """
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    relationshipManager = models.ForeignKey(RelationshipManager, on_delete=models.DO_NOTHING)
    email = models.EmailField(max_length=254, default='brigittesprung@gmail.com')
    type = models.CharField(max_length=1028)
    submitted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def getDocument(self):
        return Document.objects.filter(documentRequest=self)


class Document(models.Model):
    """
    Document Object
    Document Request created by RM

    Attributes:
    ----------
    name : CharField
        name of the file
    file : FileField
        file uploaded
    upload_date: DateTimeField
        date the file was uploaded
    """
    name = models.CharField(max_length=1028)
    file = models.FileField(upload_to='tmp/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    documentRequest = models.ForeignKey(DocumentRequest, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
