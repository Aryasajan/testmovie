from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import Movieform
from . models import Movie
# Create your views here.
def index(request):
    movies=Movie.objects.all()
    context={
        'movie_name':movies
    }
    return render(request,'index.html',context)

def details(request, movie_id):
    movie= Movie.objects.get(id=movie_id)
    return render(request,"details.html",{'movie':movie})

def add(request):
    if request.method=='POST':
        name = request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        movie=Movie(name=name,desc=desc,year=year,img=img)
        movie.save()
    return render(request,'add.html')

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=Movieform(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
