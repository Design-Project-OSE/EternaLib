
from Djongo import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


from django.http import JsonResponse
from .models import MyModel

def get_data(request):
    data = MyModel.objects.all().values()
    return JsonResponse(list(data), safe=False) 
