from django.urls import path
from . import views


app_name = 'operation'

urlpatterns = [
    path('tests/', views.TestsView.as_view(), name='tests_list'),
    path('tests/<int:pk>/details/', views.TestDetailsView.as_view(), name='test_details'),
    path('tests/add/', views.AddTestView.as_view(), name='add_test'),
    path('test/<int:pk>/answer/', views.UpdateTestView.as_view(), name='answer_test'),

    path('recovery/list/', views.RecoveryProcessesView.as_view(), name='recoveries_list'),
    path('recovery/add/', views.AddRecoveryProcessView.as_view(), name='add_recovery_process'),
    path('recovery/<int:pk>/delete/', views.DeleteRecoveryProcessView.as_view(), name='delete_recovery_process'),
    path('recovery/<int:pk>/details/', views.RecoveryProcessDetailsView.as_view(), name='recovery_process_details'),
    path('recovery/add-image/', views.AddRecoveryProcessImageView.as_view(), name='add_recovery_process_image'),
    path('recovery/delete-image/', views.DeleteRecoveryProcessImageView.as_view(), name='delete_recovery_process_image'),

    path('counseling/list/', views.CounselingsListView.as_view(), name='counselings_list'),
    path('counseling/add/', views.AddCounselingView.as_view(), name='add_counseling'),
    path('counseling/<int:pk>/answer/', views.ToggleCounselingAnswerView.as_view(), name='counseling_answer'),
]
