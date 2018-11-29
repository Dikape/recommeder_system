from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from django.contrib.auth.models import User as DefaultUser

class User(DefaultUser):
    """
      An abstract base class implementing a fully featured User model with
      admin-compliant permissions.

      Username and password are required. Other fields are optional.
      """


    username = models.CharField(
        'username',
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        error_messages={
            'unique':"A user with that username already exists.",
        },
    )
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=150, blank=True)
    email = models.EmailField(('email address'), blank=True)
    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text=('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        'active',
        default=True,
        help_text=
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ,
    )
    date_joined = models.DateTimeField(('date joined'))

    def __str__(self):
        pass

class Material(models.Model):
    title_original = models.CharField(max_length=255)
    description = models.CharField(max_length=5000)
    technical_description = models.CharField(max_length=2000)
    material_type = models.ForeignKey('MaterialType', on_delete=models.CASCADE)
    average_mark = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    redactor_mark = models.IntegerField(
        models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)]))

    def calculate_average(self):
        pass

    def get_all_translates(self):
        pass

    def __str__(self):
        pass
class MaterialTitleTranslate(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    language = models.CharField(max_length=32)
    translate = models.CharField(max_length=255)

    def krya(self):
        pass

    def __str__(self):
        pass

class MaterialType(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=5000)
    image = models.ImageField()
    counter = models.IntegerField()

    def calc_counter(self):
        pass
class RedactorReview(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    text = models.CharField(max_length=5000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_author_full_name(self):
        pass

    def __str__(self):
        pass

class Advertisement(models.Model):
    picture = models.ImageField()
    text = models.CharField(max_length=5000)
    reference = models.CharField(max_length=5000)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()

    def validate_dates(self):
        pass

    def __str__(self):
        pass

class UserMark(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    redactor_mark = models.IntegerField(
        models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)]))
    is_from_fb = models.BooleanField(default=False)

    def __str__(self):
        pass

class UserComment(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=5000)

    def __str__(self):
        pass

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

GENDER_CHOICE = (
    ('male', 'Male'),
    ('female', 'Female')
)

class FbInfo(models.Model):
    home_address = models.CharField(max_length=100)
    home_adderess_lat = models.CharField(max_length=100)
    home_address_lng = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    location_lat = models.CharField(max_length=100)
    location_lng = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(choices=GENDER_CHOICE)
    friends_count = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @classmethod
    def parse_fb(cls):
        pass

    def __str__(self):
        pass