from charset_normalizer import models
from django.contrib.auth import get_user_model
from django.contrib.gis.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


#
# # Create your models here.
# from django.contrib.gis.db import models
#
#
# class WorldBorder(models.Model):
#     # Regular Django fields corresponding to the attributes in the
#     # world borders shapefile.
#     name = models.CharField(max_length=50)
#     area = models.IntegerField()
#     pop2005 = models.IntegerField('Population 2005')
#     fips = models.CharField('FIPS Code', max_length=2, null=True)
#     iso2 = models.CharField('2 Digit ISO', max_length=2)
#     iso3 = models.CharField('3 Digit ISO', max_length=3)
#     un = models.IntegerField('United Nations Code')
#     region = models.IntegerField('Region Code')
#     subregion = models.IntegerField('Sub-Region Code')
#     lon = models.FloatField()
#     lat = models.FloatField()
#
#     # GeoDjango-specific: a geometry field (MultiPolygonField)
#     mpoly = models.MultiPolygonField()
#
#     # Returns the string representation of the model.
#     def __str__(self):
#         return self.name

class Profile(models.Model):
    class Meta:
        verbose_name = "user profile"
        verbose_name_plural = "user profiles"

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    last_location = models.PointField(
        verbose_name="last location",
        editable=False,
        blank=True,
        null=True,
        default=None,
        help_text=(
            "Geographic coordinates (lon/lat) as Point. Can be serialised from WKT (well-known text) representation")
    )

    def __str__(self):
        return f"{self.user}"


@receiver(post_save, sender=get_user_model())
def manage_user_profile(sender, instance, created, **kwargs):
    try:
        my_profile = instance.profile
        my_profile.save()
    except Profile.DoesNotExist:
        Profile.objects.create(user=instance)
