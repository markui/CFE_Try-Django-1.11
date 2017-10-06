import random
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .models import RestaurantLocation
from .forms import RestaurantCreateForm


def restaurant_createview(request):
    if request.method == "POST":
        title = request.POST.get('title')
        location = request.POST.get('location')
        category = request.POST.get('category')
        obj = RestaurantLocation.objects.create(
            name=title,
            location=location,
            category=category
        )
        return HttpResponseRedirect('/restaurants/')
    template_name = 'restaurants/form.html'
    context = {}
    return render(request, template_name, context)



def restaurant_listview(request):
    template_name = 'restaurants/restaurantlocation_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list": queryset
    }
    print(context)
    return render(request, template_name, context)


class RestaurantListView(ListView):
    # queryset = RestaurantLocation.objects.all()
    # template_name = 'restaurants/restaurants_list.html'

    def get_queryset(self):
        print(self.kwargs)
        slug = self.kwargs.get('slug')
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset

        # def get_context_data(self, *args, **kwargs):
        #     print(self.args)
        #     print(self.kwargs)
        #     context = super(RestaurantListView, self).get_context_data(*args, **kwargs)
        #     print(context)
        #     return context


class RestaurantDetailView(DetailView):
    # you can filter it by user
    queryset = RestaurantLocation.objects.all()

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        obj = get_object_or_404(RestaurantLocation, slug=slug)
        return obj

    # def get_context_data(self, *args, **kwargs):
    #     print(self.args)
    #     print(self.kwargs)
    #     context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context



# Create your views here.
# function based view

# def home_old(request):
# 	html_var = 'f strings'
# 	html_ = f"""<!DOCTYPE html>
# 	<html lang=en>

# 	<head>
# 	</head>
# 	<body>
# 	<h1>Hello World!</h1>
# 	<p>This is {html_var} coming through</p>
# 	</body>
# 	</html>
# 	"""
# 	return HttpResponse(html_)

# def home(request):
# 	num = random.randint(0, 100000)
# 	some_list = [num, random.randint(0, 100000), random.randint(0, 10000)]
# 	context = {
# 		'html_var': 'context variable',
# 		'num': num,
# 		'some_list': some_list
# 	}
# 	return render(request, "home.html", context) # response

# def about(request):
# 	context = {
# 	}
# 	return render(request, "about.html", context) # response

# def contact(request):
# 	context = {
# 	}
# 	return render(request, "contact.html", context) # response




# class ContactView(View):
# 	def get(self, request, *args, **kwargs):
# 		print(kwargs)
# 		context = {}
# 		return render(request, "contact.html", context)



# class HomeView(TemplateView):
# 	template_name = 'home.html'
# 	def get_context_data(self, *args, **kwargs):
# 		context = super(HomeView, self).get_context_data(*args, **kwargs)
# 		num = None
# 		some_list = [
# 			random.randint(0, 100000000),
# 			random.randint(0, 100000000),
# 			random.randint(0, 100000000),
# 		]
# 		condition_bool_item = True
# 		if condition_bool_item:
# 			num = random.randint(0, 100000000)

# 		context = {
# 			"num": num,
# 			"some_list": some_list,
# 		}

# 		print(context)
# 		return context