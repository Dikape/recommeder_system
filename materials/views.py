from django.views.generic import ListView, DetailView
from django.http import Http404
from materials import models


class LettersListView(ListView):
    model = models.Material
    template_name = 'materials/list.html'
    paginate_by = 20

    def get_queryset(self):
        qs = super().get_queryset()
        return qs
        # return qs.filter(thread__account__owner=self.request.user, thread__account__is_active=True)


index = LettersListView.as_view()


class LetterDetailView(DetailView):
    model = models.Material
    template_name = 'materials/details.html'

    # def get_object(self, queryset=None):
    #     obj = super().get_object()
    #     if obj.thread.account.owner == self.request.user:
    #         return obj
    #     else:
    #         raise Http404('Letter does not exist!')


material_details = LetterDetailView.as_view()
