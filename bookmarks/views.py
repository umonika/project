from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.
def main_page(request):
    return HttpResponse ('welcome to Django bookmarks')
