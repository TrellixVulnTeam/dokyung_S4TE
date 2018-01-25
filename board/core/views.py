from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse

from .models import Portfolio
from .forms import PortfolioForm


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
    form = PortfolioForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        p = Portfolio.objects.create(
            title=form.cleaned_data['title'],
            image=form.cleaned_data['image'],
            description=form.cleaned_data['description'],
            start_date=form.cleaned_data['start_date'],
            end_date=form.cleaned_data['end_date'],
        )
        return redirect(reverse('portfolio_detail', kwargs={'pk': p.pk}))

    ctx = {
        'form': form,
    }
    return render(request, 'core/portfolio_create.html', ctx)
