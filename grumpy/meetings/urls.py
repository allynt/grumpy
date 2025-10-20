from django.urls import path

from grumpy.meetings.views import MeetingListView, MeetingCreateView, MeetingDetailView

urlpatterns = [
    path("", MeetingListView.as_view(), name="meeting-list"),
    path("add/", MeetingCreateView.as_view(), name="meeting-add"),
    path("<uuid:pk>/", MeetingDetailView.as_view(), name="meeting-detail"),
]
