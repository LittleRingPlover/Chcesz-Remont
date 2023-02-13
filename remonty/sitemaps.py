from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ['remonty:index',
                'remonty:services',
                'remonty:about_me',
                'remonty:gallery',
                'remonty:contact',
                ]

    def location(self, item):
        return reverse(item)
