from django.shortcuts import render, HttpResponseRedirect
from Ghost_App.forms import BoastOrRoastForm
from Ghost_App.models import BoastOrRoast

def index (request):
    data = BoastOrRoast.objects.order_by('id').reverse()
    return render(request, 'index.html', {'data':data})


def add_post(request):
    if request.method == 'POST':
        form = BoastOrRoastForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            new_post = BoastOrRoast.objects.create(
                description = form.get('description'),
                is_boast = form.get('is_boast'),
                # date = form.get('date'),
                score = 0
            )
            return HttpResponseRedirect('/')
    else:
        form = BoastOrRoastForm()
    return render(request, 'add_post.html',{'form': form})


def like_post(request, post_id):
    post_info = BoastOrRoast.objects.filter(id=post_id)
    post_info = post_info.first()
    post_info.score += 1
    post_info.save()
    return HttpResponseRedirect('/')


def dislike_post(request, post_id):
    post_info = BoastOrRoast.objects.filter(id=post_id)
    post_info = post_info.first()
    post_info.score -= 1
    post_info.save()
    return HttpResponseRedirect('/')


def boasts(request):
    data = BoastOrRoast.objects.filter(is_boast=True)
    return render(request, 'index.html', {'data':data})


def roasts(request):
    data = BoastOrRoast.objects.filter(is_boast=False)
    return render(request, 'index.html', {'data':data})


def score_rank(request):
    data = BoastOrRoast.objects.order_by('score').reverse()
    return render(request, 'index.html', {'data':data})