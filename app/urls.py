from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
#from .views import Index, ContactPageView
from .views import index, contact

urlpatterns = [
    #path('', Index.as_view(), name='home')   
    path('', index, name='home'),
    path('home/', index, name='home'),    
    path('contact/', contact, name='contact'),
 ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
