from django.conf import settings
from django.shortcuts import render

def all_chai(request):
    print("Template dirs:", settings.TEMPLATES[0]['DIRS'])
    return render(request, 'chai/all_chai.html')