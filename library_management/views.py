import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import Book, Reservation, WaitingList


def books_list(request):
    if request.method == 'GET':
        data = []
        for book in Book.objects.all():
            data.append({
                'id': book.id,
                'title': book.title,
                'author': book.author,
                'pages': book.pages,
                'price': book.price,
                'is_reserved': book.is_reserved_now()
            })
        return JsonResponse(data, safe=False)


def reserve_book(request, book_id):
    if request.method == 'GET':
        book = get_object_or_404(Book, id=book_id)

        if not book.is_reserved_now():
            Reservation.objects.create(
                book=book,
                start_date=timezone.now(),
                end_date=timezone.now() + timedelta(days=7)
            )
            return JsonResponse({'message': 'Book reserved successfully'})
        else:
            WaitingList.objects.get_or_create(
                book=book,
                user=request.user
            )
            return JsonResponse({'message': 'Book is already reserved, you have been added to the waiting list'})
    return JsonResponse({'error': 'Method not allowed'}, status=405)


def reservations_list(request):
    if request.method == 'GET':
        data = []
        for res in Reservation.objects.select_related('book'):
            data.append({
                'id': res.id,
                'book_title': res.book.title,
                'start_date': res.start_date,
                'end_date': res.end_date
            })
        return JsonResponse(data, safe=False)

    return JsonResponse({'error': 'Method not allowed'}, status=405)
