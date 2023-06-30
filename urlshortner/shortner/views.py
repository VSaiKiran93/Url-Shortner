from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def insert(request):
    if request.method == 'POST':
        url = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        shorten_url = Url(link=url, uuid=uid)
        shorten_url.save()
        return HttpResponse(uid)
    
def click(request, ok):
    url_details = Url.objects.get(uuid=ok)
    return redirect(url_details.link)
    