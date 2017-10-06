from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator


# Create your models here.
class RestaurantLocation(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=120, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name


# pre_save signal receiver function
# DB에 저장되기 전 unique slug를 generate하기
def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    print('saving...')
    print(instance.timestamp)
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

# let's always avoid saving in post_save => loop error 날 가능성 높음
# post_save signal receiver function
def rl_post_save_receiver(sender, instance, created, *args, **kwargs):
    print('saved')
    print(instance.timestamp)


# now that we made receiver functions, we need to map them in
pre_save.connect(rl_pre_save_receiver, sender=RestaurantLocation)
post_save.connect(rl_post_save_receiver, sender=RestaurantLocation)
