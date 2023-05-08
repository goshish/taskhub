from django.shortcuts import render


def taskind(request):
    return render(request, 'webapp/taskind.html')