from django.urls import path
from channels.views import WelcomeView
from channels.views import CreateChannelView
from channels.views import ChannelDetailView
from channels.views import MyChannelsListView
from channels.views import ChannelsListView


app_name = "channels"

urlpatterns = [
    path("", WelcomeView.as_view(), name="home"),
    path('channels/create/', CreateChannelView.as_view(), name="create"),
    path('channels/detail/<int:pk>/', ChannelDetailView.as_view(), name='channel_detail'),
    path('channels/my-channels-list/', MyChannelsListView.as_view(), name="my_channels"),
    path('channels/', ChannelsListView.as_view(), name="all_channels"),

]
