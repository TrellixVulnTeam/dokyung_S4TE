from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse

from .models import Portfolio


def portfolio_list(request):
    ctx = {
        'portfolio_list': Portfolio.objects.all(),
    }
    return render(request, 'core/portfolio_list.html', ctx)


def portfolio_detail(request, pk):
    ctx = {
        'portfolio': get_object_or_404(Portfolio, pk=pk),
    }
    return render(request, 'core/portfolio_detail.html', ctx)


def portfolio_create(request):
    ctx = {}
    if request.method == "POST":
        title = request.POST['title']
        image = request.FILES['image']
        description = request.POST['description']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']

        p = Portfolio.objects.create(
            title=title,
            image=image,
            description=description,
            start_date=start_date,
            end_date=end_date,
        )

        return redirect(reverse('portfolio_detail', kwargs={'pk': p.pk}))
    return render(request, 'core/portfolio_create.html', ctx)
