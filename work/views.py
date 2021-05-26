from django.shortcuts import render

# Create your views here.
def work(request):
    categories = Category.objects.all()
    return render(request, template_name='work/work.html', context={'categories': categories})
