from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from django.http import Http404
from django.utils.translation import ugettext as _
from django.views.generic.edit import FormMixin

from .models import Domain
from .forms import FilterDomainForm


class FormListView(FormMixin, ListView):
    def get(self, request, *args, **kwargs):
        # From ProcessFormMixin
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)

        # From BaseListView
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty and len(self.object_list) == 0:
            raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
                          % {'class_name': self.__class__.__name__})

        context = self.get_context_data(object_list=self.object_list, form=self.form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

class ListDomainView(FormListView):
    model = Domain
    paginate_by = 25
    template_name = 'domain_list.html'
    form_class = FilterDomainForm
    queryset = Domain.objects.all()
    context_object_name = "domains"


    def get_queryset(self):
        try:
            id = self.request.GET['id_tk']
            print(id)
            if id == "on":
                qs = Domain.objects.filter(tk=True)
        except:
            qs = Domain.objects.all()
        return qs



def index(request):
    return HttpResponse("Hello, world. You're at the domains index.")
