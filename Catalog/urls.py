from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Catalog import views

urlpatterns = [
    path('prd_list/', views.Prod_List.as_view()),
    path('prd_detail/<int:pk>/', views.Prod_Detail.as_view()),
    path('prd_listp/', views.Prod_ListP.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)