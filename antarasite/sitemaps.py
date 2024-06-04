from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.9
    changefreq = 'weekly'

    def items(self):
        return ['home', 'aboutus', 'serviceyt', 'servicenc', 'servicendc', 'servicedc', 'servicehh', 'serviceww', 'servicekw', 'servicesc', 'servicedp', 'contactus']  # Add the names of your views

    def location(self, item):
        return reverse(item)
