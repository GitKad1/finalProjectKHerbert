from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import TopicForm
from .models import Topic
from datetime import datetime
from .news_api import fetch_news

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('../')  # Replace 'home' with the URL name of your home page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def addTopic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.user = request.user
            topic.date = datetime.now()
            topic.save()
            messages.success(request, 'Topic added successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please provide a valid topic name.')
    else:
        form = TopicForm()

    return render(request, 'addTopic.html', {'form': form})

@login_required
def dashboard(request):
    topics = Topic.objects.filter(user=request.user).order_by('-date')
    return render(request, 'dashboard.html', {'topics': topics})

def user_logout(request):
    logout(request)
    return redirect('../')

@login_required
def topic_detail(request, topic_id):
    currentTopic = get_object_or_404(Topic, id=topic_id)
    news_list = fetch_news(currentTopic.name)  # Assuming you have a function to fetch news based on the topic name
    return render(request, 'topicDetails.html', {'topic': currentTopic, 'news_list': news_list})

@login_required
def remove_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id, user=request.user)
    topic.delete()

    return redirect('dashboard')