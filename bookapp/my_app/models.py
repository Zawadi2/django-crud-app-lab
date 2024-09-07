from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


YES_NO_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No'),
    ]

# Create your models here.


class Review(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='review_set')
    review = models.TextField(max_length=250)
    rating = models.IntegerField()
    date = models.DateField('Review date')

    def __str__(self):
        return self.review
    
    def get_absolute_url(self):
        return reverse('review-detail', kwargs={'pk': self.id})

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    review = models.TextField(max_length=250)
    rate = models.IntegerField()
    reviews = models.ManyToManyField('Review', related_name='books')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'book_id': self.id})
    

class Recommendation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    recommends = models.CharField(max_length=1, choices=YES_NO_CHOICES, default=YES_NO_CHOICES[0][0])
    reason = models.TextField(blank=True, null=True)
    date = models.DateField('Recommendation date')


    def __str__(self):
        return f"{self.get_recommends_display()} recommendation for {self.book.title} on {self.date}"
   
    class Meta:
        ordering = ['-date'] 