from django.conf.urls import url
from django.urls import path
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm

from .views import RegisterUser, LoginUser, UserDetails, ContactView, \
    ProviderUpdate, ProviderState, ProductView, CartView, OrderView, ProviderOrders, CategoryView, ShopView

from rest_framework.schemas import get_schema_view
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


app_name = 'api'

schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('order', OrderView.as_view(), name='order'),
    path('cart', CartView.as_view(), name='cart'),
    path('products', ProductView.as_view(), name='products'),
    path('categories', CategoryView.as_view(), name='categories'),
    path('shops', ShopView.as_view(), name='shops'),
    path('partner/update', ProviderUpdate.as_view(), name='partner-update'),
    path('partner/state', ProviderState.as_view(), name='partner-state'),
    path('partner/orders', ProviderOrders.as_view(), name='partner-orders'),
    path('user/contact', ContactView.as_view(), name='user-contact'),
    path('user/login', LoginUser.as_view(), name='user-login'),
    path('user/details', UserDetails.as_view(), name='user-details'),
    path('user/register', RegisterUser.as_view(), name='user-register'),
    path('user/password_reset', reset_password_request_token, name='password-reset'),
    path('user/password_reset/confirm', reset_password_confirm, name='password-reset-confirm'),
    # path('openapi', get_schema_view(title="Your Project",
    #                                 description="API for all things …",
    #                                 # version="1.0.0"
    #                                 ), name='openapi-schema'),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),

]

# router = DefaultRouter()
# router.register(r'shops', ShopViewSet, base_name='shops')
# router.register(r'categories', CategoryViewSet, base_name='categories')
# urlpatterns = router.urls