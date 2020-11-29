from rest_framework import serializers
from product.models import Listing

class ListingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Listing
    fields = ['id', 'title', 'new_condition','description','category_id','brand_id']