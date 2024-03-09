from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

''' G.....E.....T '''
""" Start office view """

@api_view(['GET'])
def get_office(request):
    office = Office.objects.all()
    ser = OficeSerializer(office, many=True)
    return Response(ser.data)

""" End office view """

""" Start get color view """

@api_view(['GET'])
def get_color(request):
    color = Color.objects.all()
    ser = ColorSerializer(color, many=True)
    return Response(ser.data)

""" End color view """


""" Start brend view """

@api_view(['GET'])
def get_brend(request):
    brend = Brand.objects.all()
    ser = BrandSerializer(brend)
    return Response(ser.data)

""" End brend view """

""" Start category view """

@api_view(['GET'])
def get_category(request):
    catory = Category.objects.all()
    ser = CategorySerializer(catory)
    return Response(ser.data)

""" End category view """

""" Start sub_category view """

@api_view(['GET'])
def get_sub_category(request):
    category = Sub_category.objects.all()
    ser = Sub_CategorySerializer(category)
    return Response(ser.data)

""" End sub_category view """



''' F.I.L.T.E.R '''

@api_view(['GET'])
def filter_sub_category_by_category(request,pk):
    category = Category.objects.get(pk=pk)
    sub_categories = Sub_category.objects.filter(category=category)
    ser = Sub_CategorySerializer(sub_categories,many=True)
    return Response(ser.data)



@api_view(['GET'])
def proudct_by_sub_category(request,pk):
    sub_catigory = Sub_category.objects.get(pk=pk)
    product = Product.objects.filter(sub_catigory=sub_catigory)
    ser = ProductSerializer(product)
    return Response(ser.data)


@api_view(['GET'])
def product_by_name(request):
    name = Product.objects.get()
    product = Product.objects.filter(name=name)
    ser = ProductSerializer(product)
    return Response(ser.data)


@api_view(['GET'])
def product_by_price(request):
    start_price = request.GET.get('s_price')
    end_price = request.GET.get('e_price')
    products = Product.objects.filter(price__gte=start_price,price__lte=end_price)
    ser = ProductSerializer(products,many=True)
    return Response(ser.data)





