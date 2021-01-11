from django.db import models
from datetime import date
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor_uploader.fields import RichTextUploadingField

class Site(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=32)
    owner = models.CharField(max_length=32, blank=True, null=True)
    displayURL = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    established = models.CharField(max_length=4)
    languages = models.IntegerField()
    sitelink = models.CharField(max_length=250)
    applink = models.CharField(max_length=250, blank=True, null=True)

    logofilename = models.CharField(max_length=50)
    bgimagefilename = models.CharField(max_length=50)

    attprice = models.IntegerField(default=50)
    attcoverage = models.IntegerField(default=50)
    atteaseofuse = models.IntegerField(default=50)
    attreputation = models.IntegerField(default=50)

    prodhotels = models.BooleanField(default=False)
    prodflights = models.BooleanField(default=False)
    prodcarrentals = models.BooleanField(default=False)
    prodtrains = models.BooleanField(default=False)
    prodcruises = models.BooleanField(default=False)
    prodtransfers = models.BooleanField(default=False)
    prodtickets = models.BooleanField(default=False)
    prodtours = models.BooleanField(default=False)

    genericlinkhotels = models.CharField(max_length=500)
    genericlinkflights = models.CharField(max_length=500)
    genericlinkcarrentals = models.CharField(max_length=500)
    genericlinktrains = models.CharField(max_length=500)
    genericlinkcruises = models.CharField(max_length=500)
    genericlinktransfers = models.CharField(max_length=500)
    genericlinktickets = models.CharField(max_length=500)
    genericlinktours = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class SiteProduct(models.Model):

    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name="sites")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products")
    descoverviewcontent = models.CharField(max_length=2000, default="")
    descfeaturescontent = models.CharField(max_length=2000, default="")
    descpricingcontent = models.CharField(max_length=2000, default="")
    descavailabilitycontent = models.CharField(max_length=2000, default="")
    descaccessibilitycontent = models.CharField(max_length=2000, default="")
    descpaymentcontent = models.CharField(max_length=2000, default="")
    descreputationcontent = models.CharField(max_length=2000, default="")
    descservicecontent = models.CharField(max_length=2000, default="")
    descsummarycontent = models.CharField(max_length=2000, default="")
    descsdealscontent = models.CharField(max_length=2000, default="")

    switchdeals = models.BooleanField(default=False)

    paymentvisa = models.BooleanField(default=False)
    paymentmastercard = models.BooleanField(default=False)
    paymentamex = models.BooleanField(default=False)
    paymentpaypal = models.BooleanField(default=False)
    paymentapplepay = models.BooleanField(default=False)
    paymentgooglepay = models.BooleanField(default=False)


    sppriceraw = models.FloatField(default=0)
    spprice = models.IntegerField(default=50)
    spcoverage = models.IntegerField(default=50)
    speaseofuse = models.IntegerField(default=50)
    spreputation = models.IntegerField(default=50)


    link = models.CharField(max_length=200)

    def get_absolute_url(self):
        return '/travelsites/' + self.product.name.lower() + '/' + self.site.slug + '/'

    def __str__(self):
        name = self.site.name + " " + self.product.name
        return name


class Article(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    text = models.TextField(max_length=5000)
    fulltext = RichTextUploadingField()
    sort = models.IntegerField()
    showonhomepage = models.BooleanField(default=False)
    thumbnailfilename = models.CharField(max_length=100)
    backgroundfilename = models.CharField(max_length=100)

    shopdestination = models.BooleanField(default=False)
    shopdestinationname = models.CharField(max_length=120)
    shopproduct = models.BooleanField(default=False)
    shopproductname = models.CharField(max_length=120)

    seokeywords = models.CharField(max_length=200)
    seodescription = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/articles/' + self.slug + '/'


class Feature(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=60)
    content = models.TextField(max_length=3000)

    def __str__(self):
        return self.name


class PricingRecord(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="prods")
    site = models.ForeignKey(SiteProduct, on_delete=models.CASCADE, related_name="st")
    productname = models.CharField(max_length=100)
    price7days = models.FloatField()

    def __str__(self):
        name = str(self.productname) + " " + str(self.site.site.name)
        return name


class Price(models.Model):
    pricingrecord = models.ForeignKey(PricingRecord, on_delete=models.CASCADE, related_name="pr")
    price = models.FloatField()
    daterecorded = models.DateField(default=date.today)

    def __str__(self):
        name = str(self.price) + " " + str(self.daterecorded)
        return name

    class Meta:
        unique_together = ('pricingrecord', 'daterecorded',)


@receiver(post_save, sender=Price)
def collect_transactions(sender, instance, **kwargs):
    pricingrecord = instance.pricingrecord
    latest7days = Price.objects.filter(pricingrecord=pricingrecord).order_by('-daterecorded')[:7]
    totalp = 0
    for p in latest7days:
        totalp += p.price
    avep = totalp/7
    pricingrecord.price7days = avep
    pricingrecord.save()
    productsite = instance.pricingrecord.site
    ps = instance.pricingrecord.site
    allrecords = PricingRecord.objects.filter(site=pricingrecord.site)
    tp = 0
    for i in allrecords:
        tp += i.price7days
    newprice = tp/len(allrecords)
    ps.sppriceraw = newprice
    ps.save()


class Redirect(models.Model):
    rid = models.IntegerField()
    link = models.CharField(max_length=400)
    description = models.CharField(max_length=200, default="")
    counter = models.IntegerField()

    def clickcount(self):
        r = Redirect.objects.all()
        t = TrackingClick.objects.all()
        rt = r.t_set.all()
        tempviews = rt.count()
        return tempviews


class TrackingClick(models.Model):
    redirect = models.ForeignKey(Redirect, related_name='redirects',  on_delete=models.CASCADE,)
    datetime = models.DateTimeField(auto_now_add=True, null=True)


class DestinationGeo(models.Model):
    name = models.CharField(max_length=60)
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class OtaDestinationScore(models.Model):
    ota = models.ForeignKey(Site, related_name='otas', on_delete=models.CASCADE,)
    destination = models.ForeignKey(DestinationGeo, related_name='geos', on_delete=models.CASCADE)
    price = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    range = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def totalscore(self):
        score = self.price + self.range
        return score

    def __str__(self):
        return self.destination.name + " " + self.ota.name


class qAndATag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name


class qAndA(models.Model):
    question = models.CharField(max_length=250)
    answer = models.TextField(max_length=4000)
    slug = models.SlugField(max_length=100)
    ota = models.ForeignKey(Site, related_name='qasites', on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, related_name='qaproducts', on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(qAndATag, blank=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return '/questions/' + self.slug + '/'
