from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',views.index,name='index'),
    # path('about/',views.about,name='about'),
    # path('navigator/',views.navigator,name='navigator'),
    # path('removepunc/',views.removepunc,name='removepunc'),
    # path('capfirst/',views.capfirst,name='capfirst'),
    # path('newlineremove/',views.newlineremove,name='nlrem'),
    # path('spaceremove/',views.spaceremove,name='spaceremover'),
    # path('charcount/',views.charcount,name='chrcnt'),
    # path('assignment1/',views.assignment1,name='assignment1'),


    path('admin/',admin.site.urls),
    path('',views.index,name='index'),
    path('analyze',views.analyze,name='analyze'),
]