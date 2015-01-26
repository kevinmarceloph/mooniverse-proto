from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from vanilla import CreateView, DetailView

from .models import Page, Update

from django import forms
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Update
        fields = ('text', 'date_added')

    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs = {'class': 'form-control'}

class Home(CreateView):
    form_class = UpdateForm
    template_name = 'home.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['page_list'] = Page.objects.all()
        context['update_list'] = Update.objects.all()
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect(self.get_success_url())
home = Home.as_view()


class PageView(DetailView):
    model = Page

    def get_object(self):
        return get_object_or_404(Page, slug=self.kwargs['slug'])
page_view = PageView.as_view()
