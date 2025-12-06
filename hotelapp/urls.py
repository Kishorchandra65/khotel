from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('rooms/', views.rooms, name='rooms'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('menu/', views.menu, name='menu'),
    path('continue/', views.continue_page, name='continue'),
    path('booking/',views.booking, name='booking'),
    path('payment/', views.payment_view, name='payment'),
    path("thankyou/", views.thankyou, name="thankyou"),

]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
