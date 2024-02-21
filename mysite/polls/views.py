# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, Http404, HttpResponseRedirect
# from django.template import loader
# from .models import Question, Choice
# from django.urls import reverse


# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {
#         "latest_question_list": latest_question_list
#     }
#     return render(request, "polls/index.html", context)

# def detail(request, question_id):
#     question= get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})

# def results(request, question_id):
#     response = "You're looking at the resulsts of questions %s."
#     return HttpResponse(response % question_id)

# def vote(request, question_id):
#     question = get_object_or_404(question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.post["choice"])
#     except (keyerror, choice.doesnotexist):
#         # redisplay the question voting form.
#         return render(
#             request,
#             "polls/detail.html",
#             {
#                 "question": question,
#                 "error_message": "you didn't select a choice.",
#             },
#         )
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # always return an httpresponseredirect after successfully dealing
#         # with post data. this prevents data from being posted twice if a
#         # user hits the back button.
#         return httpresponseredirect(reverse("polls:results", args=(question.id,)))


from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
import datetime
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        # print(time, future_question)
        now = timezone.now()
        for i in Question.objects.values("pub_date"):
            print(now - datetime.timedelta(days=1) <= i <= now)
        # print(Question.objects.filter("pub_date"))
        return Question.objects.order_by("-pub_date")[0:]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))