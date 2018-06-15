from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    return render(request, 'nnet/index.html')


def pricingbox(request):

    return render(request, 'nnet/pricingbox.html')

def blog(request):

    return render(request, 'nnet/blog.html')

def typography(request):

    return render(request, 'nnet/typography.html')

def contact(request):

    return render(request, 'nnet/contact.html')

def performance(request):

    return render(request, 'nnet/performance.html')

def portfolio(request):

    return render(request, 'nnet/portfolio.html')

def components(request):

    return render(request, 'nnet/components.html')