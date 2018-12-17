import random
from django.db import transaction
from django.core.management.base import BaseCommand

from materials.models import Material, UserMark
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Set random marks for materials'

    @transaction.atomic()
    def get_users(self):
        all_materials = Material.objects.all().order_by('id')
        for material in all_materials:
            material_marks = material.usermark_set.all().values_list('mark', flat=True)
            if material_marks:
                material.average_mark = sum(material_marks)/len(material_marks) + 0.8
                if material.average_mark > 5:
                    material.average_mark -= 0.5
                print(material.average_mark)
                material.save()


    def handle(self, *args, **options):
        # self.get_materials()
        self.get_users()
        self.stdout.write(self.style.SUCCESS('Script successfully finished!'))
