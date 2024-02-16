from django.urls import path
from rooms.views import CreateChannelView, MyChannelsListView, ChannelDetailView

app_name = "rooms"

urlpatterns = [
    path('create/', CreateChannelView.as_view(), name="create"),
    path('room/<int:pk>/', ChannelDetailView.as_view(), name='room_detail'),
    path('my-rooms-list/', MyChannelsListView.as_view(), name="my_rooms"),


]
