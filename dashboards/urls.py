from django.urls import path
from . import views

urlpatterns = [
    path('dashboards/',views.dashboards,name="dashboards"),
    path('categories/',views.categories,name="categories"),
    path('categories/add/',views.categories_add,name="categories_add"),
    path('category/edit/<int:pk>/',views.edit_category,name="edit_category"),
    path('category/delete/<int:pk>/',views.delete_category,name="delete_category"),
]
