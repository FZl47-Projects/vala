from django.urls import path
from . import views


app_name = 'program'

urlpatterns = [
    path('category/', views.ProgramCategoriesView.as_view(), name='categories'),

    path('exercises/list/', views.ExerciseProgramListView.as_view(), name='exercise_list'),
    path('exercises/<int:pk>/details/', views.ExerciseProgramDetailsView.as_view(), name='exercise_details'),

    path('diets/list/', views.DietProgramListView.as_view(), name='diet_list'),
    path('diet/<int:pk>/details/', views.DietProgramDetailsView.as_view(), name='diet_details'),

    path('list/', views.ProgramsListView.as_view(), name='list'),
    path('add/', views.AddProgramView.as_view(), name='add_program'),
]
