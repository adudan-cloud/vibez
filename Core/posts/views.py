from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from posts.forms import PostForm, EventForm, MessageForm
from posts.models import Post, Event, Message
from datetime import date

@login_required
def feed_view(request):
    messages_list = Message.objects.all().order_by('-created_at')
    message_form = MessageForm(request.POST or None)
    if request.method == 'POST' and message_form.is_valid():
        msg = message_form.save(commit=False)
        msg.user = request.user
        msg.save()
        return redirect('feed')

    posts = Post.objects.all().order_by("-created_at")  # show latest first

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect("feed")
    else:
        form = PostForm()

    return render(request, "posts/feed.html", {
        "form": message_form,
        "posts": [],  # replace with your actual posts queryset if needed
        "messages": messages_list
    })

@login_required
def calendar_view(request):
    events = Event.objects.all().order_by('date')
    form = EventForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        event = form.save(commit=False)
        event.user = request.user
        event.save()
        return redirect('calendar')
    return render(request, 'posts/calendar.html', {'events': events, 'form': form, 'today': date.today()})
