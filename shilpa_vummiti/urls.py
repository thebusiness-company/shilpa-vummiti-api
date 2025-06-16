"""
URL configuration for shilpa_vummiti project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# urls.py
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from core.views import JWTSocialLoginView
class GoogleLogin(JWTSocialLoginView):
    adapter_class = GoogleOAuth2Adapter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('product.urls')),
    path('api/', include('core.urls')),
    path('api/', include('order.urls')),
    path('rest-auth/', include('dj_rest_auth.urls')),
    path('rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('accounts/', include('allauth.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)