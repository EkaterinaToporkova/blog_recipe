from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse('''<html>
    <title>Рецепты</title>
    <img src="logo.png" alt>
    </html>''')