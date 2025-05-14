from django.shortcuts import render
from .models import Vocabulary
from django.shortcuts import redirect 

# Create your views here.
from django.http import HttpResponse

def first(request):
   if request.method == 'POST':
       # Handle the form submission
       word = request.POST.get('englishWordTextbox')
       meaning = request.POST.get('bengaliMeaningTextbox')
       if word and meaning:
            Vocabulary.objects.create(word=word, meaning=meaning)
   vocab_list = Vocabulary.objects.all()
       # Here you would typically save the data to the database
       # For example: Vocabulary.objects.create(word=word, meaning=meaning)
       # return HttpResponse(f"Word: {word}, Meaning: {meaning}")
   # return HttpResponse("Hello, world!")
   return render(request, 'CustomVocabularyApp/index.html',{"vocab_list": vocab_list})