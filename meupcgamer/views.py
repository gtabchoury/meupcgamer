from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from product_store_price.models import ProductStorePrice
from product_store.models import ProductStore
from product.models import Product
from category.models import Category
from category.serializer import CategorySerializer
from product_store_price.serializer import ProductStorePriceSerializer
from product_store_price.web_scraping import WebScraping
from rest_framework import status, authentication, exceptions
import json 

# Create your views here.

class PriceAPIView(APIView):
    def get(self, request):
        query = request.query_params['query']
        products = Product.objects.filter(name__contains=query)
        
        json = []
        for product in products:
            print(product.name)
            prices_json = []

            product_store_list = ProductStore.objects.filter(product=product)
            for product_store in product_store_list:
                price = None
                if (product_store.store.name=="Kabum"):
                    price = WebScraping.get_price_kabum(product_store.url)
                elif (product_store.store.name=="Pichau"):
                    price = WebScraping.get_price_pichau(product_store.url)
                elif (product_store.store.name=="Americanas"):
                    price = WebScraping.get_price_pichau(product_store.url)
                elif (product_store.store.name=="Amazon"):
                    price = WebScraping.get_price_amazon(product_store.url)
                
                if (price != None):
                    prices_json.append({'store': product_store.store.name, 'brand': product_store.brand.name, 'url': product_store.url,
                    'price': price['price'], 'discount_price': price['price_discount']})
            json.append({'product': product.name, 'prices': prices_json})

        return Response({'results': json})

    def post(self, request):
        json_body = json.loads(request.body)
        
        json_response = []
        for item in json_body:
            category = Category.objects.get(id=item['category_id'])
            
            list_product_store_price = []

            product = Product.objects.get(id=item['product_id'])

            if (product.category.id!=category.id):
                return Response({'error': 'Produto '+product.name+' inválido para '+category.name}, status=status.HTTP_404_NOT_FOUND)

            product_store_list = ProductStore.objects.filter(product=product)
            lowest_price = None

            for product_store in product_store_list:
                price = None
                if (product_store.store.name=="Kabum"):
                    price = WebScraping.get_price_kabum(product_store.url)
                elif (product_store.store.name=="Pichau"):
                    price = WebScraping.get_price_pichau(product_store.url)
                elif (product_store.store.name=="Americanas"):
                    price = WebScraping.get_price_pichau(product_store.url)
                elif (product_store.store.name=="Amazon"):
                    price = WebScraping.get_price_amazon(product_store.url)
                
                real_price = price['price']
                discount_price = price['price_discount']

                if (real_price!=None):
                    product_store_price = ProductStorePrice()
                    product_store_price.product_store = product_store
                    product_store_price.price = real_price
                    product_store_price.promotional_price = discount_price
                    list_product_store_price.append(product_store_price)
                
                    if (lowest_price==None):
                        lowest_price = product_store_price
                    elif (real_price < lowest_price.price or real_price<lowest_price.promotional_price):
                        lowest_price = product_store_price  
                    elif (discount_price!=None and (discount_price<lowest_price.promotional_price or discount_price<lowest_price.promotional_price)):
                        lowest_price = product_store_price  

            if (lowest_price==None):
                json_response.append({'category':CategorySerializer(category).data, 
                'lowest_product_store_price': None,
                'product_store_prices': None})
            else:
                json_response.append({'category':CategorySerializer(category).data, 
                'lowest_product_store_price': ProductStorePriceSerializer(lowest_price).data,
                'product_store_prices': ProductStorePriceSerializer(list_product_store_price, many=True).data})

        return Response(json_response, status=status.HTTP_200_OK)