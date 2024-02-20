from django.urls import path
from channels.views import WelcomeView
from channels.views import CreateChannelView
from channels.views import ChannelDetailView
from channels.views import MyChannelsListView
from channels.views import ChannelsListView
from channels.views import JoinChannelRequestView, ChannelJoinRequestListView, JoinRequestDecisionView
from channels.views import LeaveChannelView


app_name = "channels"

urlpatterns = [
    path("", WelcomeView.as_view(), name="home"),
    path('channels/create/', CreateChannelView.as_view(), name="create"),
    path('channels/detail/<int:pk>/', ChannelDetailView.as_view(), name='channel_detail'),
    path('channels/my-channels-list/', MyChannelsListView.as_view(), name="my_channels"),
    path('channels/', ChannelsListView.as_view(), name="all_channels"),

    path('channels/join-request/submit', JoinChannelRequestView.as_view(), name="join_request"),
    path('channels/detail/<int:channel_id>/requests', ChannelJoinRequestListView.as_view(), name="list_join_requests"),
    path('channels/join-request/decision', JoinRequestDecisionView.as_view(), name='join_request_decision'),

    path('channels/leave', LeaveChannelView.as_view(), name='leave'),

]
