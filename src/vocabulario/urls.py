from django.urls import path

from .views import VocabularioViewSet,VocabularioList

from rest_framework import routers

router = routers.DefaultRouter()
router.register('', VocabularioViewSet)
router.urls.append(path('vocabulario/search', VocabularioList.as_view()))