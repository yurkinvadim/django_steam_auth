from django.shortcuts import render


def authenticator(request):
    return render(request, 'authenticator/index.html')
