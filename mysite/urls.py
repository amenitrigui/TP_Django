"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
from . import views
from rest_framework import routers
from magasin.views import ProductViewset, CategoryAPIView
# Ici nous créons notre routeur
router = routers.SimpleRouter()
# Puis lui déclarons une url basée sur le mot clé ‘category’ et notre view
# afin que l’url générée soit celle que nous souhaitons ‘/api/category/’
router.register('produit', ProductViewset, basename='produit')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('magasin/', include('magasin.urls')),
    path('blog/', include('blog.urls')),
    path('jeux/', include('jeux.urls')),
    # path('jeux/',include('jeux.urls')),
    path('', views.home,name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'), name ='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='registration/logout.html'), name ='logout'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    # """ path('password_change/', views.PasswordChangeView.as_view(),name='password_change'),
    # path('password_change/done/', views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    # path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    # path('reset/done/', views.PasswordResetCompleteView.as_view(),name='password_reset_complete'), """
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

