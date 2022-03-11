from django.contrib import messages
from django.shortcuts import render
from .models import Portfolio,Blog,Testimonals,Certificate


from django.views import generic

from .forms import ContactForm

from .models import Blog as BlogModel

class IndexView(generic.TemplateView):
    template_name ='main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        testimonals = Testimonals.objects.filter(is_active=True)
        certificate = Certificate.objects.filter(is_active=True)
        blogs = BlogModel.objects.filter(is_active=True)
        portfolio = Portfolio.objects.filter(is_active=True)

        context["testimonals"]=testimonals
        context["certificate"]=certificate
        context["blogs"]=blogs
        context["portfolio"]=portfolio
        return context

class ContactView(generic.TemplateView):
    template_name='main/contact.html'
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        messages.success(self.request,'Thank you. We will be in touch')
        return super().form_valid(form)

class PortfolioView(generic.TemplateView):
    model = Portfolio
    template_name='main/portfolio.html'
    paginate_by = 10

    def get_queryset(self):
        
        return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.TemplateView):
    model = Portfolio
    template_name ='main/portfolio-detail.html'


class Blog(generic.TemplateView):
    model = Blog
    template_name='main/blog.html'
    paginate_by = 10

    def get_queryset(self):
        
        return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.TemplateView):
    model = Blog
    template_name ='main/blog-detail.html'


  








