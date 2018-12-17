import csv
import random
import datetime
import pickle
from django.db import transaction
from django.core.management.base import BaseCommand

from materials.models import Material, MaterialType, UserMark
from users.models import FbInfo
from django.contrib.auth.models import User
from clustering.updated_affinity import CustomAffinityPropagation

import numpy as np

from sklearn import metrics
from sklearn import preprocessing


class Command(BaseCommand):
    help = 'Load datasets of users, movies and users info from facebook'

    def get_users(self):
        users = User.objects.all().order_by('id')
        materials = Material.objects.filter(material_type=1).order_by('id')[:10]
        user_vectors = []
        for user in users:
            if hasattr(user, 'fbinfo'):
                user_vector = user.fbinfo.get_vector(materials)
                user_vectors.append(user_vector)
        print('\n\n')
        print(user_vectors)
        print('\n\n')
        return user_vectors
        #     username=username,
        #     first_name=row["first_name"],
        #     last_name=row["last_name"],
        #     email=email,
        #     date_joined=datetime.datetime.now(),
        #     password='kryakryapass'
        # )
        # FbInfo.objects.create(
        #     home_address=town_row['home_towm_name'],
        #     home_address_lat=row['home_town_lat'],
        #     home_address_lng=row['home_town_lng'],
        #     location=town_row['location_name'],
        #     location_lat=row['location_lat'],
        #     location_lng=row['location_lng'],
        #     age=row['age_range'],
        #     gender=row['gender'],
        #     friends_count=random.randint(5, 200),
        #     user=user
        # )

    def train(self, data):
        self.stdout.write(self.style.SUCCESS('Start training'))
        data = np.asarray(data)
        # min_max_scaler = preprocessing.MinMaxScaler()
        # new_data = min_max_scaler.fit_transform(data)
        clustering = CustomAffinityPropagation(max_iter=1000).fit(data)

        labels = clustering.labels_
        cluster_centers = clustering.cluster_centers_

        labels_unique = np.unique(labels)
        cluster_centers_indices = clustering.cluster_centers_indices_
        n_clusters_ = len(cluster_centers_indices)
        print(f'\n\n\nCluster Numbers = {n_clusters_}\n')
        for k in range(n_clusters_):
            class_members = labels == k

            cluster_center = data[cluster_centers_indices[k]]
            print(f'Cluster center({k})={cluster_center}')
            for i, obj in enumerate(data):
                if class_members[i]:
                    print(obj)
            print('\n')
        return clustering

    def save_model(self, trained_model):
        with open('trained_model.pkl', 'wb') as output:
            pickle.dump(trained_model, output, pickle.HIGHEST_PROTOCOL)

        self.stdout.write(self.style.SUCCESS('Saving model!'))

    def handle(self, *args, **options):
        # self.get_materials()
        vector = self.get_users()
        trained_model = self.train(vector)
        self.save_model(trained_model)
        self.stdout.write(self.style.SUCCESS('Script successfully finished!'))
