from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import  contactForm
from blog.models import BlogPost


def home_page(request):
	qs=BlogPost.objects.all()[:5]
	context = {"title":"Welcome to Ariful Website", "blog_list":qs}

	return render(request, "home.html", context)


def about_page(request):
	return render(request, "about.html", {"title":"About Us"})

def Contact_page(request):
	form =contactForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		form=contactForm()
	context={"title":"Contact Us", "form":form}
	return render(request, "form.html", context)


def example_page(request):
	context = {"title":"Example"}
	template_name= "hello_world.html"
	template_obj = get_template(template_name)
	rendered_item = template_obj.render(context)
	return HttpResponse(rendered_item)






