import random
from django.db import transaction
from django.core.management.base import BaseCommand

from materials.models import Material, UserMark
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Set random marks for materials'

    def get_users(self):
        all_users = User.objects.all().order_by('id')
        all_materials = Material.objects.all().order_by('id')
        for material in all_materials[4000:]:
            print(f'material - {material.id}')
            with transaction.atomic():
                for user in all_users:
                    user_mark = random.randint(2, 5)
                    set_mark = random.randint(0, 1)
                    is_from_fb = random.randint(0, 1)
                    if set_mark:
                        UserMark.objects.create(
                            material=material,
                            user=user,
                            mark=int((material.redactor_mark+user_mark)/2),
                            is_from_fb=is_from_fb,
                        )


    def handle(self, *args, **options):
        # self.get_materials()
        self.get_users()
        self.stdout.write(self.style.SUCCESS('Script successfully finished!'))
