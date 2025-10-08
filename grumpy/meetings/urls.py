from django.urls import path

from grumpy.meetings.views import MeetingListView, MeetingCreateView

urlpatterns = [
    path("", MeetingListView.as_view(), name="meeting-list"),
    path("add/", MeetingCreateView.as_view(), name="meeting-add"),
    # path("<uuid:pk>/", MeetingUpdateView.as_view(), name="meeting-update"),
]
