import csv
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
        pass

    def handle(self, *args, **options):
        # self.get_materials()
        self.get_users()
        self.stdout.write(self.style.SUCCESS('Script successfully finished!'))
