from rest_framework.routers import DefaultRouter
from domains.views import ClientViewSet, DomainViewSet


routes = DefaultRouter()
routes.register('clients', ClientViewSet)
routes.register('domains', DomainViewSet)

urlpatterns = routes.urls