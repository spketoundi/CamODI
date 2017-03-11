from django.conf.urls import url

from waespk.core.feeds import BlogFeed, PlanetDrupalFeed
from waespk.core import views

urlpatterns = [
    url(r'^blog/feed/$', BlogFeed(), name='blog_feed'),
    url(r'^newsletter-subscribe', views.newsletter_subsribe),
    url(
        r'^blog/feed/planet_drupal/$',
        PlanetDrupalFeed(),
        name='planet_drupal_feed'
    ),
]
