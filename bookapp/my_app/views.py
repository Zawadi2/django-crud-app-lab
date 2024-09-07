from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, Review
from .forms import RecommendationForm


# Create your views here.
class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def book_index(request):
    books = Book.objects.filter(user=request.user)  
    return render(request, 'books/index.html', {'books': books})

@login_required
def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    reviews_book_doesnt_have = Review.objects.exclude(id__in = book.reviews.all().values_list('id'))
    recommendation_form = RecommendationForm()
    return render(request, 'books/detail.html', {
        'book': book, 
        'recommendation_form': recommendation_form,
        'reviews': reviews_book_doesnt_have
        })

@login_required
def add_recommendation(request, book_id):
    form = RecommendationForm(request.POST)
    if form.is_valid():
        new_recommondation = form.save(commit=False)
        new_recommondation.book_id = book_id
        new_recommondation.save()
    return redirect('book-detail', book_id=book_id)

@login_required
def associate_review(request, book_id, review_id):
    Book.objects.get(id=book_id).reviews.add(review_id)
    return redirect('book-detail', book_id=book_id)

@login_required
def remove_review(request, book_id, review_id):
    book = Book.objects.get(id=book_id)
    book.reviewss.remove(review_id)
    return redirect('book-detail', book_id=book.id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)


class BookCreate(LoginRequiredMixin,CreateView):
    model = Book
    fields = ['title', 'author', 'review', 'rate']
    # success_url = '/books/'

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class BookUpdate(LoginRequiredMixin,UpdateView):
    model = Book
    fields = ['title', 'review', 'rate']

class BookDelete(LoginRequiredMixin,DeleteView):
    model = Book
    success_url = '/books/'

class ReviewCreate(LoginRequiredMixin,CreateView):
    model = Review
    fields = '__all__'

class ReviewList(LoginRequiredMixin,ListView):
    model = Review

class ReviewDetail(LoginRequiredMixin,DetailView):
    model = Review

class ReviewUpdate(LoginRequiredMixin,UpdateView):
    model = Review
    fields = ['book', 'reviw','rating','date']

class ReviewDelete(LoginRequiredMixin,DeleteView):
    model = Review
    success_url = '/reviews/'



