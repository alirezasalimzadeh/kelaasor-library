from django.db import models
from django.conf import settings
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pages = models.PositiveIntegerField()
    price = models.PositiveIntegerField()


    def __str__(self):
        return self.title

    def is_reserved_now(self):
        now = timezone.now()
        return self.reservations.filter(end_date__gte=now).exists()


class Reservation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reservations')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f"{self.book.title} ({self.start_date:%Y-%m-%d} → {self.end_date:%Y-%m-%d})"


class WaitingList(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"{self.user.username} waiting for {self.book.title}"
