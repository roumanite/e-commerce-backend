from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse
from rest_framework.response import Response
from product.models import Listing, Category
import json
from mptt.templatetags.mptt_tags import cache_tree_children
from product.serializers import ListingSerializer

def recursive_node_to_dict(node):
  result = {
      'id': node.pk,
      'name': node.name,
  }
  children = [recursive_node_to_dict(c) for c in node.get_children()]
  if children:
      result['children'] = children
  return result

def index(request):
  return JsonResponse({'message':'This is index page'})

@api_view(['GET'])
def category(request):
  root_nodes = cache_tree_children(Category.objects.all())
  dicts = []
  for n in root_nodes:
    dicts.append(recursive_node_to_dict(n))
  return Response({'categories':dicts})

@api_view(['POST'])
def listing(request):
  valid_ser = ListingSerializer(data=request.data)
  if valid_ser.is_valid():
    valid_ser.save()
    return Response(valid_ser.data, status=status.HTTP_201_CREATED)
  else:
    return Response(valid_ser.errors)