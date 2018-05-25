from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.
def main_page(request):
    template = loader.get_template('bookmarks/main_page.html')
    return HttpResponse(template.render({} , request))


 