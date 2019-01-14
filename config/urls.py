from django.contrib import admin
from django.urls import path

from apps.account.views import SubscribeAddView, ThanksSignupView

urlpatterns = [
    path('', SubscribeAddView.as_view()),
    path('thanks/', ThanksSignupView.as_view()),
    path('admin/', admin.site.urls),
]
