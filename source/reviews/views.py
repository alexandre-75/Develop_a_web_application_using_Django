from django.shortcuts import render
from django.http import HttpResponse

# def main(request):

#     context = {}
#     return render(request, "blog/main.html", context)

def index(request):
    return render(request, "reviews/index.html")
