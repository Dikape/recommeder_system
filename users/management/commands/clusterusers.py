import csv
import random
import datetime
from django.db import transaction
from django.core.management.base import BaseCommand

from materials.models import Material, MaterialType
from users.models import FbInfo
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Load datasets of users, movies and users info from facebook'

    @transaction.atomic
    def get_materials(self):
        with open('movies.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for i, row in enumerate(reader):
                if row['IMDB Score'] and row['IMDB Score'].isdigit():
                    Material.objects.create(
                        image=row['Poster'],
                        title_original=row['Title'],
                        description='Awesome movie',
                        technical_description=row['Genre'],
                        material_type_id=1,
                        redactor_mark=int(int(row['IMDB Score'])/2),
                    )

    @transaction.atomic
    def get_users(self):
        with open('towns.csv', newline='') as csvfile_info:
            with open('users.csv', newline='') as csvfile_users:
                reader_info = csv.DictReader(csvfile_info, delimiter=',')
                reader_users = csv.DictReader(csvfile_users, delimiter=',')
                for i, row in enumerate(reader_users):
                    town_row = next(reader_info)
                    username = f'{row["first_name"]}_{row["last_name"]}{i}'
                    email = f'{username}@gmail.com'
                    user = User.objects.create(
                        username=username,
                        first_name=row["first_name"],
                        last_name=row["last_name"],
                        email=email,
                        date_joined=datetime.datetime.now(),
                        password='kryakryapass'
                    )
                    FbInfo.objects.create(
                        home_address=town_row['home_towm_name'],
                        home_address_lat=row['home_town_lat'],
                        home_address_lng=row['home_town_lng'],
                        location=town_row['location_name'],
                        location_lat=row['location_lat'],
                        location_lng=row['location_lng'],
                        age=row['age_range'],
                        gender=row['gender'],
                        friends_count=random.randint(5, 200),
                        user=user
                    )


    def handle(self, *args, **options):
        # self.get_materials()
        self.get_users()
        self.stdout.write(self.style.SUCCESS('Script successfully finished!'))
