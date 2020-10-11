from django.shortcuts import render, get_object_or_404
from .models import Site, Article, Feature, SiteProduct, Product


def index(request):

    bookingsites = Site.objects.all()
    articles = Article.objects.all()

    return render(request, 'main/templates/index.html', {'bookingsites': bookingsites, 'articles': articles})


def site(request, product, slug):

    asite = get_object_or_404(Site, slug=slug)
    prod = get_object_or_404(Product, name=product)
    siteproduct = get_object_or_404(SiteProduct, product=prod, site=asite)
    compsites = SiteProduct.objects.filter(product=prod).exclude(pk=siteproduct.pk)
    allsites = Site.objects.all().exclude(slug=slug)

    return render(request, 'main/templates/site-details.html', {'site': asite, 'allsites': allsites, 'siteproduct': siteproduct, 'prod': prod, 'compsites': compsites})


def sitecomparison(request, product, sitea, siteb):

    prod = get_object_or_404(Product, name=product)
    sitea = get_object_or_404(Site, slug=sitea)
    siteaprod = get_object_or_404(SiteProduct, product=prod, site=sitea)
    siteb = get_object_or_404(Site, slug=siteb)
    sitebprod = get_object_or_404(SiteProduct, product=prod, site=siteb)

    return render(request, 'main/templates/site-comparison.html', {'sitea': sitea, 'siteaprod': siteaprod, 'siteb': siteb, 'sitebprod': sitebprod, 'prod': prod})


def article(request, slug):

    article = get_object_or_404(Article, slug=slug)
    allsites = Site.objects.all()

    return render(request, 'main/templates/article-details.html', {'article': article, 'allsites': allsites})


def featurecomparison(request, slug):

    feature = get_object_or_404(Feature, slug=slug)
    if feature.slug == "price":
        template = "main/templates/features/price-details.html"
    elif feature.slug == "features":
        template = "main/templates/features/feature-details.html"
    elif feature.slug == "availability":
        template = "main/templates/features/availability-details.html"
    elif feature.slug == "accessibility":
        template = "main/templates/features/accessibility-details.html"
    elif feature.slug == "payment":
        template = "main/templates/features/payment-details.html"
    elif feature.slug == "reputation":
        template = "main/templates/features/reputation-details.html"
    elif feature.slug == "service":
        template = "main/templates/features/service-details.html"
    else:
        template = "index.html"

    allsites = Site.objects.all()

    return render(request, template, {'feature': feature, 'allsites': allsites})


def allarticles(request):

    arts = Article.objects.all()
    allsites = Site.objects.all()

    return render(request, 'main/templates/article-list.html', {'arts': arts, 'allsites': allsites})


def about(request):

    return render(request, 'main/templates/about.html')