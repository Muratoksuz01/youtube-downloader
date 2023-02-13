from django.shortcuts import render
from pytube import YouTube
# Create your views here.
def Index(request):
    if request.method=="POST":
        link=request.POST["input"]
        yt= YouTube(link)
        ys=yt.streams.get_highest_resolution()
        ys.download("~/Desktop/","video.mp4")

    return render(request,"index.html") 






