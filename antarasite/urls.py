from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.sitemaps.views import sitemap
from antarasite.sitemaps import StaticViewSitemap
from . import views

sitemaps = {
    'static': StaticViewSitemap,
    # Add more sitemaps if needed
}

urlpatterns = [
    path('', views.home, name="home"),
    path('about-us', views.aboutus, name="aboutus"),
    path('escapes', views.antaraescapes, name="antaraescapes"),
    path('yoga-club', views.yogaclub, name="yogaclub"),
    # path('our-specialised-cares/diabetes-consultation', views.servicedc, name="servicedc"),
    path('our-specialised-cares/men-health', views.servicehh, name="servicehh"),
    path('our-specialised-cares/women-wellness', views.serviceww, name="serviceww"),
    path('our-specialised-cares/weight-management-obesity', views.servicekw, name="servicekw"),
    path('our-specialities/naturopathic-consultations', views.servicenc, name="servicenc"),
    path('our-specialities/nutrition-and-diet-consultations', views.servicendc, name="servicendc"),
    path('our-specialities/senior-care', views.servicesc, name="servicesc"),
    path('our-specialities/yoga-consultations', views.serviceyt, name="serviceyt"),
    path('our-specialities/detoxification-programs', views.servicedp, name="servicedp"),
    path('contact-us', views.contactus, name="contactus"),
    path('thank-you', views.thankyou, name="thankyou"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    # Add the following lines for redirection
    path('our-specialities/', lambda request: redirect('home')),
    path('our-specialised-cares/', lambda request: redirect('home')),
]