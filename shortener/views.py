from django.shortcuts import render,get_object_or_404,redirect
from .models import Url
from django.contrib import messages
def index(request):
    if request.method == "POST":
        url=request.POST["url"]
        slug=request.POST["slug"]
        try:
            Url.objects.get(slug=slug)
            messages.error(request,"لینک کوتاه شده نمیتواند تکراری باشد")
            return render(request,"index.html")
        except Url.DoesNotExist:
            pass

        new_url= Url(url=url,slug=slug)
        new_url.save()
        messages.success(request,"با موفقیت ساخته شد.")
        return render(request,"index.html")
    return render(request,"index.html")

    

def list(request):
    list=Url.objects.all()

    return render(request,"list.html",{"list":list}) 


def url_redirect(request,slug):
    url=get_object_or_404(Url,slug=slug)
    url.visit+=1
    url.save()
    return redirect(url.url)

    