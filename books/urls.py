from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, CategoryViewSet
router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'categories', CategoryViewSet)
urlpatterns = router.urls

