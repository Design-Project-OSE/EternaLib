from django.http import JsonResponse
from myapp.models import MyModel

def get_data(request):
    data = list(MyModel.objects.all().values())  # Tüm verileri al
    return JsonResponse(data, safe=False)
