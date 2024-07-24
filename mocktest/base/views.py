from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from base.models import Question,Category
from base.forms import AddQustion
# # Create your views here.
def login (request):
    if request.method == 'POST':
        print("DONE")
        return render(request, 'modules.html')

    return(render(request, "login.html"))


def base(request):
    return render(request, "home.html",)


def modules(request):
    category_view = Category.objects.all()
    qstn=Question.objects.all()
    print(category_view)
    return render(request,"modules.html ",{'category_view':category_view,'qstn':qstn})

def create_question(request):
    if request.method == 'POST':
        form = AddQustion(request.POST)
        if form.is_valid():
            form.save()
        return redirect('base:home')

    else:
        form = AddQustion()
    return render(request,'create_question.html',{"form":form})


def exam(request, pk, name):
    questions = list(Question.objects.prefetch_related('question_answer').filter(category=pk))
    subject = name
    question_index = int(request.GET.get('question_index', 0))

    if question_index >= len(questions):
        return render(request,'home.html')  # Adjust this to your completion URL

    current_question = questions[question_index]
    next_question_index = question_index + 1 if question_index < len(questions) - 1 else None
    previous_question_index = question_index - 1 if question_index > 0 else None
    question_no = question_index + 1

    if request.method == 'POST':
        selected_answer_id = request.POST.get(str(current_question.id))
        if selected_answer_id:
            selected_answer = current_question.question_answer.get(id=selected_answer_id)
            print( selected_answer)
            if selected_answer.is_correct:
                total_marks = request.session.get('total_marks', 0) + 4
                request.session['total_marks'] = total_marks
                status = "correct"
            else:
                status = "wrong"
            print(status)

        if next_question_index is not None:
            return HttpResponseRedirect(f'?question_index={next_question_index}')
        else:
            total_marks = request.session.get('total_marks', 0)
            request.session.flush()
            return render(request, 'result.html', {'total_marks': total_marks, 'subject': subject})


    return render(request, 'exam.html', {
        'current_question': current_question,
        'question_index': question_index,
        'next_question_index': next_question_index,
        'previous_question_index': previous_question_index,
        'question_no': question_no,
        'subject': subject,
    })
def exam_complete(request):
    total_marks = request.session.get('total_marks', 0)
    return render(request, 'home.html', {'total_marks': total_marks})


