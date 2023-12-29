from django.urls import path
from . import views

app_name = 'service'
urlpatterns = [
    # Operator Category
    path('operator/category/add', views.OperatorCategoryAddView.as_view(), name='operator_category__add'),
    path('operator/category/list', views.OperatorCategoryListView.as_view(), name='operator_category__list'),
    path('operator/category/delete/<int:category_id>', views.OperatorCategoryDeleteView.as_view(),
         name='operator_category__delete'),
    path('operator/category/detail/<int:category_id>', views.OperatorCategoryDetailView.as_view(),
         name='operator_category__detail'),
    # Operator
    path('operator/add', views.OperatorAddView.as_view(), name='operator__add'),
    path('operator/delete/<int:operator_id>', views.OperatorDeleteView.as_view(), name='operator__delete'),
    path('operator/detail/<int:operator_id>', views.OperatorDetailView.as_view(), name='operator__detail'),
]
