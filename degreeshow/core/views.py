from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import ArtWork

def work_list(request):
    ctx = {
        'work_list': ArtWork.objects.all()
    }
    return render(request, 'core/work_list.html', ctx)


def work_detail(request, pk):
    ctx = {
        'work': get_object_or_404(ArtWork, pk=pk)
    }
    return render(request, 'core/work_detail.html', ctx)
