from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from app.views import AccountViewSet, TransactionVieSet

router = routers.DefaultRouter()

router.register('v1/account', AccountViewSet)
router.register('v1/transaction', TransactionVieSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),
]
