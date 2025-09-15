from django.shortcuts import render

def library_view(request):
    context = {
        'title': 'Library Management',
    }
    return render(request,'library_management/books.html', context)
