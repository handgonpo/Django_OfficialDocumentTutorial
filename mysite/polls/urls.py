from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    # part3 API 사용하기 연습
    path('create/', views.create_question),
    # path('list/', views.list_questions),
    path('get/<int:question_id>/', views.get_question),
    path('update/<int:question_id>/', views.update_question),
    path('delete/<int:question_id>/', views.delete_question),
    path('add_choices/<int:question_id>/', views.add_choices),
    path('get_choices/<int:question_id>/', views.get_choices),
    path("part3/", views.part3_test_page),            # 전체페이지
    path("list/", views.question_list_view),     # 리스트 출력페이지
]