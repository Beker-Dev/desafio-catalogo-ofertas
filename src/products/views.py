from django.shortcuts import render
from django.views import View


class ProductView(View):
    template_name = 'products/index.html'    
    
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
