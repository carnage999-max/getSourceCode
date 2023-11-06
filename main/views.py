from django.shortcuts import render
import requests
from django.contrib import messages


def index(request):
    if request.method == "POST":
        url = request.POST.get('url')
        output = ""
        try:
            r = requests.get(url)
            output = r.text
        except:
            messages.error(request, f"Could not generate Source code for {url}")
        return render(request, 'index.html', {'output': output, 'url': url})
    else:
        return render(request, 'index.html')
        
    