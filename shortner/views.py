from django.shortcuts import render
from .models import ShortUrl
from .forms import ShortUrlForm
import random, string

def home(request):
    return render(request, 'home.html')

def create_short_url(request):
    if request.method == 'POST':
        form = ShortUrlForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            obj = ShortUrl.objects.get(original_url = original_url)
            if obj:
                return render(request, 'shorturl.html', {'short_url': obj.short_url})

            random_chars = list(string.ascii_letters)
            short_url = ''
            for i in range(5):
                short_url += random.choice(random_chars)
            while len(ShortUrl.objects.filter(short_url = short_url)) != 0:
                short_url += random.choice(random_chars)
            
            obj = ShortUrl(original_url = original_url, short_url = short_url)
            obj.save()
            return render(request, 'shorturl.html', {'short_url': short_url})
    elif request.method == 'GET':
        form = ShortUrlForm()
        return render(request, 'create.html', {'form': form})

def redirect_short_url(request, url):
    if url:
        url_obj = ShortUrl.objects.get(short_url = url)
        if not url_obj:
            return render(request, '404.html')
        return render(request, 'detail.html', {'url_obj': url_obj})
    else:
        return redirect('home')

