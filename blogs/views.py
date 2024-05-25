from django.views.generic import TemplateView, ListView, DetailView

from blogs.models import BlogModel, BlogCategoryModel, BlogTagModel


class BlogsListViews(ListView):
    template_name = 'blog-list.html'
    context_object_name = 'blogs'
    model = BlogModel

    def get_context_data(self, *, object_list=None, **kwargs):
        blogs = BlogModel.objects.all().order_by('-created_at')
        cat = self.request.GET.get('cat')

        if cat:
            blogs = blogs.filter(category__in=cat)

        tags = BlogTagModel.objects.all()
        tag = self.request.GET.get('tag')

        if tag:
            tags = tags.filter(tags__in=tag)

        context = {
            'blogs': blogs,
            'categories': BlogCategoryModel.objects.all(),
            'tags': BlogTagModel.objects.all(),
            'famous_blogs': BlogModel.objects.all().order_by('-created_at'),
        }
        return context


class BlogsDetailViews(DetailView):
    template_name = 'blog-details.html'
    context_object_name = 'blog'
    model = BlogModel

    def get_context_data(self, *, object_list=None, **kwargs):


        context = {
            'categories': BlogCategoryModel.objects.all(),
            'blog': BlogModel.objects.get(pk=self.kwargs['pk']),
            'tags': BlogTagModel.objects.all(),
            'famous_blogs': BlogModel.objects.all().order_by('-created_at'),
        }
        return context
