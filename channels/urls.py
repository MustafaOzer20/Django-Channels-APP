from django.urls import path
from channels.views import CreateChannelView, MyChannelsListView, ChannelDetailView

app_name = "channels"

urlpatterns = [
    path('create/', CreateChannelView.as_view(), name="create"),
    path('channels/<int:pk>/', ChannelDetailView.as_view(), name='channel_detail'),
    path('my-channels-list/', MyChannelsListView.as_view(), name="my_channels"),


]
