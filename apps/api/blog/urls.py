from django.urls import path
from apps.api.catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ImageViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter


urlpatterns = [

]

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns += router.urls