from django.shortcuts import render, HttpResponseRedirect
from Ghost_App.forms import BoastOrRoastForm
from Ghost_App.models import BoastOrRoast

def index (request):
    data = BoastOrRoast.objects.order_by('-date')
    return render(request, 'index.html', {'data':data})


def add_post(request):
    if request.method == 'POST':
        form = BoastOrRoastForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            new_post = BoastOrRoast.objects.create(
                description = form.get('description'),
                is_boast = form.get('is_boast'),
                up_votes = 0,
                down_votes = 0
            )
            return HttpResponseRedirect('/')
    else:
        form = BoastOrRoastForm()
    return render(request, 'add_post.html',{'form': form})


def like_post(request, post_id):
    post_info = BoastOrRoast.objects.filter(id=post_id)
    post_info = post_info.first()
    post_info.up_votes += 1
    post_info.vote_score = post_info.up_votes - post_info.down_votes
    post_info.save()
    return HttpResponseRedirect('/')


def dislike_post(request, post_id):
    post_info = BoastOrRoast.objects.filter(id=post_id)
    post_info = post_info.first()
    post_info.down_votes += 1
    post_info.vote_score = post_info.up_votes - post_info.down_votes
    post_info.save()
    return HttpResponseRedirect('/')


def boasts(request):
    data = BoastOrRoast.objects.order_by('-date').filter(is_boast=True)
    # data = data.objects.filter(is_boast=True)
    return render(request, 'index.html', {'data':data})
# sort by time submitted

def roasts(request):
    data = BoastOrRoast.objects.order_by('-date').filter(is_boast=False)
    # data = data.objects.filter(is_boast=False)
    return render(request, 'index.html', {'data':data})
# sort by time submitted

def score_rank(request):
    data = BoastOrRoast.objects.order_by('vote_score').reverse()
    return render(request, 'index.html', {'data':data})