from django.contrib import admin
from .models import Book, Reservation, WaitingList

admin.site.register(Book)
admin.site.register(Reservation)
admin.site.register(WaitingList)
