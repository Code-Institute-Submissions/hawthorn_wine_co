from django.shortcuts import render

# Create your views here.


def wineclub(request):
    """ A view to return the Wine Club page """

    return render(request, 'wineclub/wineclub.html')
