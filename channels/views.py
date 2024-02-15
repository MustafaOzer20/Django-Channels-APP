from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from channels.models import Channels, ChannelsMembership
from channels.forms import CreateChannelForm, MessageForm
# Create your views here.


class CreateChannelView(LoginRequiredMixin, CreateView):
    model = Channels
    form_class = CreateChannelForm
    template_name = 'channels/create.html'
    success_url = '/channels/my-channels-list'

    def form_valid(self, form):
        channel = form.save(commit=False)
        channel.admin_user = self.request.user
        channel.save()

        ChannelsMembership.objects.create(user=self.request.user, channel=channel)

        return super().form_valid(form)


def get_memberships(paginator, page):
    try:
        memberships = paginator.page(page)
    except PageNotAnInteger:
        memberships = paginator.page(1)
    except EmptyPage:
        memberships = paginator.page(paginator.num_pages)
    return memberships


class MyChannelsListView(ListView):
    model = ChannelsMembership
    template_name = 'channels/my_channels_list.html'
    context_object_name = 'memberships'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        memberships = context['memberships']
        paginator = Paginator(memberships, self.paginate_by)
        page = self.request.GET.get('page')
        memberships = get_memberships(paginator, page)
        
        context['memberships'] = memberships
        return context
    
class ChannelDetailView(DetailView):
    model = Channels
    template_name = 'channels/detail.html'
    context_object_name = 'channel'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MessageForm()
        return context

    def post(self, request, *args, **kwargs):
        form = MessageForm(request.POST)
        if form.is_valid():
            # Get the message from the form
            message = form.save(commit=False)
            message.user = request.user
            message.channel = self.get_object()
            message.save()
        return redirect(request.path_info) 