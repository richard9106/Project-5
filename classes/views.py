from django.shortcuts import render



# Create your views here.
def classes_list(request):
    """ View for home page"""
    return render(request, "classes_list.html")
