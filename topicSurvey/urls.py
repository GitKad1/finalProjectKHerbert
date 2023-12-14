from django.urls import path
from .views import register, user_login, user_logout, dashboard, addTopic, topic_detail, remove_topic

urlpatterns = [
    path('register/', register, name='register'),
    path('logout', user_logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('accounts/login/', user_login, name='login'),
    path('', dashboard, name='dashboard'),
    path('addTopic/', addTopic, name='addTopic'),
    path('topic_detail/<int:topic_id>', topic_detail, name='topic_detail'),
    path('remove_topic/<int:topic_id>/', remove_topic, name='remove_topic'),
    # Add other URL patterns as needed
]