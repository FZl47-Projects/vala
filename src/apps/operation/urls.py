from django.urls import path
from . import views


app_name = 'operation'

urlpatterns = [
    path('tests/', views.TestsView.as_view(), name='tests_list'),
    path('tests/<int:pk>/details/', views.TestDetailsView.as_view(), name='test_details'),
    path('tests/add/', views.AddTestView.as_view(), name='add_test'),
]
