from django.shortcuts import render

def show_main(request):
    context = {
        'sign' : 'Hello World!',
    }

    return render(request, "main.html", context)