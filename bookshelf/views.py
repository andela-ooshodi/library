from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, View
from django.core.exceptions import ObjectDoesNotExist
from .models import Category, Book


class IndexView(TemplateView):
    # Base view
    template_name = 'bookshelf/base.html'


class ResultView(View):
    # Result view
    # Function that handles the get request received in this view
    def get(self, request):
        name = request.GET.get('name')

        try:
            if not name:
                raise ObjectDoesNotExist

            # query both tables for similar names
            category = Category.objects.filter(name__icontains=name)
            book = Book.objects.filter(name__icontains=name)

            if any([category, book]):
                # payload
                payload = {'categories': category,
                           'books': book}
                return render(request, 'bookshelf/result.html', payload)
            else:
                raise ObjectDoesNotExist
        except ObjectDoesNotExist:
            return redirect(reverse('404'))


class NotFoundView(TemplateView):
    # 404 view
    template_name = 'bookshelf/404.html'
