from django.db.models import Avg
from django.views.generic import ListView, DetailView
from django.http import Http404
from materials import models


class MaterialTypesListView(ListView):
    model = models.MaterialType
    template_name = 'materials/types-list.html'
    paginate_by = 20

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.order_by('id')
        # return qs.filter(thread__account__owner=self.request.user, thread__account__is_active=True)


index = MaterialTypesListView.as_view()


class MaterialsListView(ListView):
    model = models.Material
    template_name = 'materials/list.html'
    paginate_by = 20

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(
            material_type__slug=self.kwargs.get('slug'),
        ).exclude(image='').exclude(average_mark__isnull=True)
        # print(qs[0].users_mark)
        return qs.order_by('-average_mark')


materials = MaterialsListView.as_view()


class RecommendationsView(ListView):
    model = models.Material
    template_name = 'materials/recomendations.html'
    paginate_by = 20

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(
            material_type__slug=self.kwargs.get('slug')
        ).exclude(image='').exclude(average_mark__isnull=True)
        return qs.order_by('-average_mark')


recommendations = RecommendationsView.as_view()


class LetterDetailView(DetailView):
    pk_url_kwarg = 'id'
    model = models.Material
    template_name = 'materials/details.html'

    # def get_object(self, queryset=None):
    #     obj = super().get_object()
    #     if obj.thread.account.owner == self.request.user:
    #         return obj
    #     else:
    #         raise Http404('Letter does not exist!')


material_details = LetterDetailView.as_view()
