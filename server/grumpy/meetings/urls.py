from django.urls import path

from grumpy.meetings.views import MeetingListView, MeetingCreateView

urlpatterns = [
    path("", MeetingListView.as_view(), name="meeting-list"),
    path("add/", MeetingCreateView.as_view(), name="meeting-add"),
    # path("<int:pk>/", MeetingUpdateView.as_view(), name="meeting-update"),
    # path("<int:pk>/delete/", MeetingDeleteView.as_view(), name="meeting-delete"),
]
