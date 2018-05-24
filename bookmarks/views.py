from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.
def main_page(request):
    output = '''
    <html>
    <head><title> %s </title></head>
    <body>
    <h1>%s</h1>
    <p> %s</p>
    </body>
    </html>''' % (
        'Django Bookmarks',
        'welcome to Django Bookmarks',
        'where you can store and share bookmarks')

    return HttpResponse (output)


