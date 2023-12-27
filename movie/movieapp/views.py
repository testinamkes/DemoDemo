from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import MovieForm
from .models import Movie


# Create your views here.


def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,"index.html",context)
def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movie})

def add(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        description=request.POST.get('description',)
        year=request.POST.get('year',)
        cast=request.POST.get('cast',)
        img=request.FILES['img']
        movie=Movie(name=name,description=description,year=year,cast=cast,img=img)
        movie.save()
    return render(request, "add.html")

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')

# def add_movie(request,id=None):
#     if id is not None:
#         pass
#     else:
#
#         if request.method == 'POST':
#             return render(request, 'addmovie.html')

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movieapp:index')
    else:
        form = MovieForm()

    return render(request, 'addmovie.html', {'form': form})