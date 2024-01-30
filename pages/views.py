from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


from .models import Questions , Page
from .forms import QuestionForm

# Create your views here.
def page(request, slug):
    page = get_object_or_404(Page, slug=slug)

    if(not page.is_active):
        #not find
        
        b = 0

    context = {
        'page': page,
    }
    return render(request, 'pages/page.html', context)



@login_required()
def ask_question(request):
    questions = Questions.objects.all()

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question_object = form.save(commit=False)
            question_object.author = request.user
            try:
                question_object.parent = form.cleaned_data['parent']

            except:
                question_object.parent = None
            form.save()

        return render(request, 'pages/questions.html', {'form': form, 'questions': questions})

    else:
        form = QuestionForm()
        return render(request, 'pages/questions.html', {'form': form, 'questions': questions})


