from django.urls import path
from channels.views import (
    WelcomeView,
    CreateChannelView,
    EditChannelView,
    DeleteChannelView,
    ChannelDetailView,
    MyChannelsListView,
    ChannelsListView,
    JoinChannelRequestView,
    ChannelJoinRequestListView,
    JoinRequestDecisionView,
    LeaveChannelView
)



app_name = "channels"

urlpatterns = [
    path("", WelcomeView.as_view(), name="home"),
    path('channels/create/', CreateChannelView.as_view(), name="create"),
    path('channels/edit/<int:channel_id>', EditChannelView.as_view(), name="edit"),
    path('channels/delete', DeleteChannelView.as_view(), name='delete'),
    path('channels/detail/<int:pk>/', ChannelDetailView.as_view(), name='channel_detail'),
    path('channels/my-channels-list/', MyChannelsListView.as_view(), name="my_channels"),
    path('channels/', ChannelsListView.as_view(), name="all_channels"),

    path('channels/join-request/submit', JoinChannelRequestView.as_view(), name="join_request"),
    path('channels/detail/<int:channel_id>/requests', ChannelJoinRequestListView.as_view(), name="list_join_requests"),
    path('channels/join-request/decision', JoinRequestDecisionView.as_view(), name='join_request_decision'),

    path('channels/leave', LeaveChannelView.as_view(), name='leave'),

]
