# coding:utf-8
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader

from .models import Question


# Create your views here.
def without_render_index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return HttpResponse(template.render(context, request))


# render() 载入模板，填充上下文，再返回由它生成的 HttpResponse 对象。不需要再导入 loader 和 httpResponse
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


def result(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

# 在Django中函数的执行如 detail(request=<HttpRequest object>, question_id=34)

# 每个视图必须要做的只有两件事：返回一个包含被请求页面内容的 HttpResponse 对象， 或者抛出一个异常，比如 Http404 。
