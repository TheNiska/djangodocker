from django.shortcuts import render


def home(request):
    context = {
        'lines': ["Hello", "From", "Django"]
    }
    return render(request, "home.html", context)
