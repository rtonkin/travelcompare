from django.shortcuts import render, get_object_or_404
from .models import Site, Article, Feature, SiteProduct, Product, DestinationGeo, OtaDestinationScore, qAndA, qAndATag
from dal import autocomplete
from django.http import JsonResponse
from django.db.models import Q


def index(request):

    bookingsites = Site.objects.all()
    articles = Article.objects.all()
    questions = qAndA.objects.all().order_by('?')[:9]
    tags = qAndATag.objects.all()

    return render(request, 'main/templates/index.html', {'bookingsites': bookingsites, 'articles': articles, 'questions': questions, 'tags': tags})


def index2(request):

    bookingsites = Site.objects.all()
    articles = Article.objects.all()

    products = Product.objects.all()
    prods = []
    for p in products:
        prods.append(p.name)

    otas = Site.objects.all()
    sites = []
    for s in otas:
        sites.append(s.name)

    return render(request, 'main/templates/index2.html', {'bookingsites': bookingsites, 'articles': articles, 'prods': prods, 'sites': sites})


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


def rec_beijing(request):

    trip = Site.objects.get(slug='tripcom')
    expedia = Site.objects.get(slug='expedia')
    hotels = Site.objects.get(slug='hotelscom')
    booking = Site.objects.get(slug='booking')
    agoda = Site.objects.get(slug='agoda')

    return render(request, 'main/templates/rec_beijing.html', {'trip': trip, 'expedia': expedia, 'hotels': hotels, 'booking': booking, 'agoda': agoda})


def rec_shanghai(request):

    trip = Site.objects.get(slug='tripcom')
    expedia = Site.objects.get(slug='expedia')
    hotels = Site.objects.get(slug='hotelscom')
    booking = Site.objects.get(slug='booking')
    agoda = Site.objects.get(slug='agoda')

    return render(request, 'main/templates/rec_shanghai.html', {'trip': trip, 'expedia': expedia, 'hotels': hotels, 'booking': booking, 'agoda': agoda})


def rec_guangzhou(request):

    trip = Site.objects.get(slug='tripcom')
    expedia = Site.objects.get(slug='expedia')
    hotels = Site.objects.get(slug='hotelscom')
    booking = Site.objects.get(slug='booking')
    agoda = Site.objects.get(slug='agoda')

    return render(request, 'main/templates/rec_guangzhou.html', {'trip': trip, 'expedia': expedia, 'hotels': hotels, 'booking': booking, 'agoda': agoda})


def rec_shenzhen(request):

    trip = Site.objects.get(slug='tripcom')
    expedia = Site.objects.get(slug='expedia')
    hotels = Site.objects.get(slug='hotelscom')
    booking = Site.objects.get(slug='booking')
    agoda = Site.objects.get(slug='agoda')

    return render(request, 'main/templates/rec_shenzhen.html', {'trip': trip, 'expedia': expedia, 'hotels': hotels, 'booking': booking, 'agoda': agoda})


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


class MainPageAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = SiteProduct.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


def userPanel(request):
    places = DestinationGeo.objects.all().values("name")
    return render(request, "user.html", {"places": places})


def getUserInfo(request):
    if request.method == "GET" and request.is_ajax():
        place = request.GET.get("selection")
        try:
            place = OtaDestinationScore.objects.filter(destination__name=place)
        except:
            return JsonResponse({"success": False}, status=400)
        data = list(place.values())
        print(data)
        return JsonResponse({"data": data}, status=200)
    return JsonResponse({"success": False}, status=400)


def questionAnswer(request, slug):
    data = qAndA.objects.get(slug=slug)
    ota = data.ota
    otherquestions = qAndA.objects.filter(Q(ota=ota), ~Q(slug=slug))
    tags = data.tags.all()

    return render(request, 'main/templates/questionanswer.html', {'data': data, 'otherquestions': otherquestions, 'tags': tags})


def questionAnswerTag(request, slug):
    data = qAndA.objects.filter(tags__slug=slug)
    tag = qAndATag.objects.get(slug=slug)

    return render(request, 'main/templates/questionanswer-tag.html', {'data': data, 'tag': tag})
