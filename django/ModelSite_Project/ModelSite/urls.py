"""ModelSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from ModelSitePort import views as ModelSitePortViews

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1.0/modelSite/', include('ModelSitePort.urls')),
    path('api/v1.0/testCelery/', ModelSitePortViews.GetUsersCeleryView.as_view(), name='test_celery'),
    path('api/v1.0/testCelery/<str:id>', ModelSitePortViews.CheckTask.as_view(), name='check_celery'),
]
