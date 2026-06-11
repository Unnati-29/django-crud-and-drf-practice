
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import ChaiViewSet, ReviewViewSet

router = DefaultRouter()
router.register('chais', ChaiViewSet)
router.register('reviews',ReviewViewSet)  


urlpatterns = [
    path('', views.all_chai, name='all_chai'),
    path('<int:chai_id>/', views.chai_detail, name='chai_detail'),
    path('chai_stores/', views.chai_store_view, name='chai_stores'),
    # path('api/chais/',views.chai_api,name='chai_api'),
    # path('api/chais/<int:chai_id>/',views.chai_detail_api,name='chai_detail_api'),

    # path('api/chais/',views.ChaiListCreateAPIView.as_view()),
    # path('api/chais/<int:pk>/',views.ChaiDetailAPIView.as_view()),
]

urlpatterns += router.urls