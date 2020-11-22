from django.http import JsonResponse
from product.models import Listing, Category
import json
from mptt.templatetags.mptt_tags import cache_tree_children

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

def category(request):
  root_nodes = cache_tree_children(Category.objects.all())
  dicts = []
  for n in root_nodes:
      dicts.append(recursive_node_to_dict(n))
  return JsonResponse(dicts, safe=False)
