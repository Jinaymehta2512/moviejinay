from django.shortcuts import render,get_object_or_404,redirect
from .models import Movie, Review, Email
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies=Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render (request,'home.html',{'searchTerm':searchTerm, 'movies':movies})

def signup(request):
    email = request.GET.get('email')
    em = Email(emailid = email)
    em.save()
    return render(request, 'signup.html', {'email':email})

def detail(request,movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    reviews = Review.objects.filter(movie=movie)
    return render(request,'detail.html',{'movie':movie,'reviews':reviews})

@login_required
def createreview(request, movie_id):
    # sourcery skip: extract-method, remove-unnecessary-else
    movie = get_object_or_404(Movie,pk=movie_id)
    if request.method == 'GET':
        return render(request,'createreview.html',{'movie':movie})
    else:
        try:
            myreview=request.POST.get('myreview')
            newReview=Review()
            newReview.user = request.user
            newReview.movie = movie
            newReview.text = myreview
            newReview.save()
            return redirect('detail',newReview.movie.id)
        except ValueError:
            return render(request,'createreview.html',{'error':'bad data passed in'})

@login_required        
def updatereview(request, review_id):
    review = get_object_or_404(Review,pk=review_id,user=request.user) 
    if request.method == 'GET': 
        return render(request, 'updatereview.html', {'review': review}) 
    else: 
        try: 
            review.text = request.POST.get('myreview') 
            review.save() 
            return redirect('detail', review.movie.id) 
        except ValueError: 
            return render(request, 'updatereview.html', {'review': review, 'error':'Bad data in form'})
        
@login_required        
def deletereview(request, review_id):
    review = get_object_or_404(Review,pk=review_id,user=request.user)
    review.delete()
    return redirect('detail', review.movie.id)