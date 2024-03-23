from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.urls import reverse
#from django.template import loader
#from django.http import Http404
from django.views import generic

from .models import Choice, Question

# Question “index” page – displays the latest few questions.
def index_old(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.html")
    # context = {"latest_question_list": latest_question_list}
    # return HttpResponse(template.render(context, request))
    # shortcut render
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


# Question “detail” page – displays a question text, with no results but with a form to vote.
# def detail(request, question_id):
#    return HttpResponse("You're looking at question %s." % question_id)

def detail_old(request, question_id):
    print("\n"+"absolute URL ", request.build_absolute_uri())
    print("session", request.session)
    print("user", request.user)
    print("get host", request.get_host())
    print("get port", request.get_port())
    print("full path", request.get_full_path())
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, "polls/detail.html", {"question": question})
    # shortcut version of try-get details
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

# Question “results” page – displays results for a particular question.
def results_old(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

# -----------------------------------------------------------------------------
# more generic with less code
# -----------------------------------------------------------------------------

class IndexView(generic.ListView):
    # default template name would be polls/question_list.html
    template_name = "polls/index.html"
    # in the template we want to use latest_question_list instead of automatically generated question_list
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    # default template name would be polls/<model>_detail.html
    template_name = "polls/detail.html"
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

# end of the improvement part

# Vote action – handles voting for a particular choice in a particular question.
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
    
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

