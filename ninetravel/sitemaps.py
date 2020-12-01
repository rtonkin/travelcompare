from django.contrib.sitemaps import Sitemap
from main.models import SiteProduct, Article


class SiteProductSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5
    protocol = 'https'

    def items(self):
        return SiteProduct.objects.all()


class ArticleSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5
    protocol = 'https'

    def items(self):
        return Article.objects.all()


class SiteComparisonSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5
    protocol = 'https'

    def items(self):
        return Article.objects.all()
