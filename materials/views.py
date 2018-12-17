import pickle
from django.db.models import Avg
from django.views.generic import ListView, DetailView
from django.http import Http404
from materials import models
from users.models import FbInfo
from django.contrib.auth.models import User
import numpy as np

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
        all_movies = []
        with open('trained_model.pkl', 'rb') as tr_model:
            model = pickle.load(tr_model)
            materials = models.Material.objects.filter(material_type=1).order_by('id')[:10]
            vector = self.request.user.fbinfo.get_vector(materials)
            prediction = model.predict([vector,])
            cluster_center = model.data[prediction]
            print(f'Cluster center({prediction})={cluster_center}')
            labels = model.labels_
            class_members = labels == prediction
            # for i, obj in enumerate(model.data):
            #     if class_members[i]:
            #         print(obj)
            indexes = np.where(class_members==True)
            for i in indexes[0]:
                n = int(i)
                print(model.data[n])
                fb_info = FbInfo.objects.all().order_by('id')[n]
                print(fb_info.get_vector(materials))
                movies = models.UserMark.objects.filter(mark__gte=2, user=fb_info.user).\
                    values_list('material__id', flat=True)
                all_movies.extend(movies)
        qs = qs.filter(id__in=all_movies,
            material_type__slug=self.kwargs.get('slug')
        ).exclude(image='').exclude(average_mark__isnull=True).order_by('?')[:30]
        return qs


recommendations = RecommendationsView.as_view()


class LetterDetailView(DetailView):
    pk_url_kwarg = 'id'
    model = models.Material
    template_name = 'materials/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            user_mark = models.UserMark.objects.get(user=self.request.user,
                                                    material=self.object.id)
        except models.UserMark.DoesNotExist:
            user_mark = None
        context.update({
            'user_mark': user_mark
        })
        return context
    # def get_object(self, queryset=None):
    #     obj = super().get_object()
    #     if obj.thread.account.owner == self.request.user:
    #         return obj
    #     else:
    #         raise Http404('Letter does not exist!')


material_details = LetterDetailView.as_view()
