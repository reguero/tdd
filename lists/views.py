from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    response = render(request, 'home.html', {
            'new_item_text': request.POST.get('item_text', ''),
    })
    #print(repr(response.content))
    return response

