from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from .models import Question, Choice


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# http://localhost:8000/polls/

def part3_test_page(request):
    return render(request, "polls/part3.html")
# http://localhost:8000/polls/part3/ -> part3.html

# 질문 생성 함수(Create)
def create_question(request):
    q = Question.objects.create(
        question_text="당신의 취미는 무엇인가요?",
        pub_date=timezone.now()
    )
    return JsonResponse({'created_question_id': q.id})

# 질문 전체 조회 (Read - All)
# def list_questions(request):
#     questions = Question.objects.all()
#     data = [{'id': q.id, 'text': q.question_text, 'date': q.pub_date} for q in questions]
#     return JsonResponse({'questions': data})

# 리스트 템플릿 렌더링용 뷰
def question_list_view(request):
    questions = Question.objects.all()
    return render(request, "polls/question_list.html", {"questions": questions})
# http://localhost:8000/polls/list/ 


# 특정 질문 조회 (Read - One)
def get_question(request, question_id):
    q = get_object_or_404(Question, id=question_id)
    return JsonResponse({
        'id': q.id,
        'question_text': q.question_text,
        'pub_date': q.pub_date
    })

# 질문 수정 (Update)
def update_question(request, question_id):
    q = get_object_or_404(Question, id=question_id)
    q.question_text = "수정된 질문입니다."
    q.save()
    return JsonResponse({'updated_text': q.question_text})

# 질문 삭제 (Delete)
def delete_question(request, question_id):
    q = get_object_or_404(Question, id=question_id)
    q.delete()
    return JsonResponse({'status': 'deleted'})

# 선택지 추가 (Create Choice for Question)
def add_choices(request, question_id):
    q = get_object_or_404(Question, id=question_id)
    q.choice_set.create(choice_text="독서", votes=0)
    q.choice_set.create(choice_text="운동", votes=0)
    return JsonResponse({'status': 'choices added'})

# 선택지 조회 (Get choices for a question)
def get_choices(request, question_id):
    q = get_object_or_404(Question, id=question_id)
    choices = q.choice_set.all()
    data = [{'id': c.id, 'text': c.choice_text, 'votes': c.votes} for c in choices]
    return JsonResponse({'choices': data})