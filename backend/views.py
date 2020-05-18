from .models import Product, News
from .serializers import ProductSerializer, NewsSerializer
from rest_framework import generics


class ProductListCreateView(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class NewsListCreateView(generics.ListCreateAPIView):

    # queryset = News.objects.all()
    serializer_class = NewsSerializer
    # paginate_by = 3

    def get_queryset(self):
        self.queryset = News.objects.all().order_by('arrival_date')
        self.queryset = [rs for rs in self.queryset if not rs._is_news_expired()]

        # return only top latest three news
        self.queryset = self.queryset[:3] if len(self.queryset) > 3 else self.queryset
        return self.queryset

