from django.urls import path
from .views import test, recovery, counseling, routine


app_name = 'operation'

urlpatterns = [
    path('tests/', test.TestsView.as_view(), name='tests_list'),
    path('tests/<int:pk>/details/', test.TestDetailsView.as_view(), name='test_details'),
    path('tests/add/', test.AddTestView.as_view(), name='add_test'),
    path('test/<int:pk>/answer/', test.UpdateTestView.as_view(), name='answer_test'),

    path('recovery/list/', recovery.RecoveryProcessesView.as_view(), name='recoveries_list'),
    path('recovery/add/', recovery.AddRecoveryProcessView.as_view(), name='add_recovery_process'),
    path('recovery/<int:pk>/delete/', recovery.DeleteRecoveryProcessView.as_view(), name='delete_recovery_process'),
    path('recovery/<int:pk>/details/', recovery.RecoveryProcessDetailsView.as_view(), name='recovery_process_details'),
    path('recovery/add-image/', recovery.AddRecoveryProcessImageView.as_view(), name='add_recovery_process_image'),
    path('recovery/delete-image/', recovery.DeleteRecoveryProcessImageView.as_view(), name='delete_recovery_process_image'),

    path('counseling/list/', counseling.CounselingsListView.as_view(), name='counselings_list'),
    path('counseling/add/', counseling.AddCounselingView.as_view(), name='add_counseling'),
    path('counseling/<int:pk>/answer/', counseling.ToggleCounselingAnswerView.as_view(), name='counseling_answer'),
]
