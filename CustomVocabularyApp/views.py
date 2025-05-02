from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first(request):
   # return HttpResponse("Hello, world!")
   return render(request, 'CustomVocabularyApp/index.html')