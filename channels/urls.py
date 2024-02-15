from django.urls import path
from channels.views import CreateChannelView, MyChannelsListView

app_name = "channels"

urlpatterns = [
    path('create/', CreateChannelView.as_view(), name="create"),
    path('my-channels-list/', MyChannelsListView.as_view(), name="my_channels"),
]
