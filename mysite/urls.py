from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()


urlpatterns = patterns('',
    (r'^hiphopathy/$', 'hiphopathy.views.index'),
    (r'^hiphopathy/(?P<artistid>\d+)/song_view/$', 'hiphopathy.views.song_view'),
    (r'^hiphopathy/(?P<songid>\d+)/snippet_view/$', 'hiphopathy.views.snippet_view'),
    (r'^hiphopathy/post/$', 'post'),
    (r'^hiphopathy/search_form/$', 'hiphopathy.views.search_form'),
    (r'^hiphopathy/search/$', 'hiphopathy.views.search'),
    (r'^hiphopathy/contact/$', 'hiphopathy.views.contact'),
    (r'^admin/', include(admin.site.urls)),
    (r'^hiphopathy/about/$', 'hiphopathy.views.about'),
    (r'^hiphopathy/tutorial_1/$', 'hiphopathy.views.tutorial_1'),
    (r'^hiphopathy/tutorial_2/$', 'hiphopathy.views.tutorial_2'),
    (r'^hiphopathy/(?P<snippetid>\d+)/manage_snippets/$', 'hiphopathy.views.manage_snippets'),
    (r'^hiphopathy/visual_score/$', 'hiphopathy.views.visual_score'),
)
if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )