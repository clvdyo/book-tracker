from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'A. Nurcahaya Tampubolon',
        'class': 'PBP Genap'
    }

    return render(request, "main.html", context)