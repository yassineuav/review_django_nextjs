from django.urls import include, path
from rest_framework import routers
from reviews import views
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'reviews', views.ReviewViewSet)
router.register(r'businesses', views.BusinessViewSet)
router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]