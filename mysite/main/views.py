from django.shortcuts import get_object_or_404, render, redirect
from .models import Google, Write, Category
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse
import random
import json
# Create your views here.
def index(request):

    all_boards = Google.objects.all()
    paginator = Paginator(all_boards, 9)
    page = int(request.GET.get('page', 1))
    board_list = paginator.get_page(page)
    # context = {
    #     'destinations' : destinations
    # }
    return render(request, 'main/index.html', {'title':'Board List', 'board_list':board_list})

def search(request):
    search_list = Google.objects.all()
    q = request.POST.get('q', '') 

    if q:
        search_list = search_list.filter(name__icontains=q)
        return render(request, 'main/search.html', {'search_list' : search_list, 'q' : q})
    else:
        return render(request, 'main/search.html')

def result_full(request):
    result_full_list = Google.objects.all()
    paginator = Paginator(result_full_list, 9)
    page = int(request.GET.get('page', 1))
    result_full_list = paginator.get_page(page)
    return render(request, 'main/result_full.html', {'result_full_list':result_full_list})

def result_in(request):
    result_in_list = Google.objects.filter(inout='in')
    paginator = Paginator(result_in_list, 9)
    page = int(request.GET.get('page', 1))
    result_in_list = paginator.get_page(page)
    return render(request, 'main/result_in.html', {'result_in_list':result_in_list})

def result_out(request):
    result_out_list = Google.objects.filter(inout='out')
    paginator = Paginator(result_out_list, 9)
    page = int(request.GET.get('page', 1))
    result_out_list = paginator.get_page(page)
    return render(request, 'main/result_out.html', {'result_out_list':result_out_list})

def result_free(request):
    result_free_list = Google.objects.filter(charge='free')
    paginator = Paginator(result_free_list, 9)
    page = int(request.GET.get('page', 1))
    result_free_list = paginator.get_page(page)
    return render(request, 'main/result_free.html', {'result_free_list':result_free_list})

def result_charge(request):
    result_charge_list = Google.objects.filter(charge='charge')
    paginator = Paginator(result_charge_list, 9)
    page = int(request.GET.get('page', 1))
    result_charge_list = paginator.get_page(page)
    return render(request, 'main/result_charge.html', {'result_charge_list':result_charge_list})

# 테마파크
def result_theme_park(request):
    result_theme_park_list = Google.objects.filter(theme='theme park')
    paginator = Paginator(result_theme_park_list, 9)
    page = int(request.GET.get('page', 1))
    result_theme_park_list = paginator.get_page(page)
    return render(request, 'main/result_theme_park.html', {'result_theme_park_list':result_theme_park_list})

# 빌딩 & 타워
def result_building_tower(request):
    result_building_tower_list = Google.objects.filter(theme='building') | Google.objects.filter(theme='tower')
    paginator = Paginator(result_building_tower_list, 9)
    page = int(request.GET.get('page', 1))
    result_building_tower_list = paginator.get_page(page)
    return render(request, 'main/result_building_tower.html', {'result_building_tower_list':result_building_tower_list})

# 산
def result_mountain(request):
    result_mountain_list = Google.objects.filter(theme='mountain')
    paginator = Paginator(result_mountain_list, 9)
    page = int(request.GET.get('page', 1))
    result_mountain_list = paginator.get_page(page)
    return render(request, 'main/result_mountain.html', {'result_mountain_list':result_mountain_list})

# 역사 유적지
def result_historical_site(request):
    result_historical_site_list = Google.objects.filter(theme='historical site')
    paginator = Paginator(result_historical_site_list, 9)
    page = int(request.GET.get('page', 1))
    result_historical_site_list = paginator.get_page(page)
    return render(request, 'main/result_historical_site.html', {'result_historical_site_list':result_historical_site_list})

# 공원
def result_park(request):
    result_park_list = Google.objects.filter(theme='park')
    paginator = Paginator(result_park_list, 9)
    page = int(request.GET.get('page', 1))
    result_park_list = paginator.get_page(page)
    return render(request, 'main/result_park.html', {'result_park_list':result_park_list})

# 쇼핑
def result_shopping(request):
    result_shopping_list = Google.objects.filter(theme='shopping')
    paginator = Paginator(result_shopping_list, 9)
    page = int(request.GET.get('page', 1))
    result_shopping_list = paginator.get_page(page)
    return render(request, 'main/result_shopping.html', {'result_shopping_list':result_shopping_list})

def list(request):
    return render(request, 'main/list.html')

def details(request, pk):
    destination = Google.objects.get(pk=pk)
    context = {
        'destination':destination,
    }
    print(context)
    return render(request, 'main/details.html', context)
    


def write(request):
    if request.method == 'POST':
        data = {
            'name':request.POST.get('name'),
            'contents' : request.POST.get('contents'),
        }
        destination = Write.objects.create(**data)
        
        return redirect(f'/details/{destination.pk}')
    context = {
            'locations' : Write.google,
        }
    return render(request, 'main/write.html', context)


# def result_in(request):
#     store_list_in = []
#     for store in Google.objects.all():
#         if request['inout'] == 'in':
#             continue
#         store_list_in.append(store)
#     if len(store_list_in) == 0:
#         for store in Google.objects.all():
#             if request['inout'] == 'in':
#                 continue

#     return render(request, 'main/result_in.html', {'store_list_in':store_list_in})


# def get_in(info_dict):
#     store_list_in = []
#     for store in Google.objects.all():
#         if info_dict['inout'] == 'in':
#             store_list_in.append(store)
#     if len(store_list_in) == 0:
#         for store in Google.objects.all():
#             if info_dict['inout'] == 'in':
#                 continue
#     return store_list_in

# def result_in(request):
#     # try:
#     #     inout = request.GET['inout']
#     #     charge = request.GET['charge']
#     #     info_dict = {'inout':inout, 'charge':charge}
#     #     store_in = get_in(info_dict)

#     # except (KeyError):
#     #     print("ERROR")


#     inout = request.GET['inout']
#     charge = request.GET['charge']
#     info_dict = {'inout':inout, 'charge':charge}
#     store_in = get_in(info_dict)
#     # else:
#     #     return HttpResponseRedirect(reverse('result_in', args=(store_in.name,)))
        
#     return render(request, 'main/result_in.html', {'store_in':store_in})



# def vote_in(request):
#     try:
#         inout = request.GET['inout']
#         charge = request.GET['charge']
#         info_dict = {'inout': inout, 'charge': charge}
#         store = get_store_in(info_dict)
#     except (KeyError):
#         print("ERROR")
#     else:
#         return HttpResponseRedirect(reverse('result_in', args=(store.name,)))
        
#     return render(request, 'result_in.html')


# def result(request, store_name):
#     try:
#         store = get_object_or_404(Google, pk=store_name)
#     except (KeyError):
#         print('ERROR')
#         return render(request, 'result.html')
#     else:
#         return render(request, 'result.html', {'store': store})



def result(request):

    destination_list = []

    for destination in Google.objects.all():
        destination_list.append(destination)

    # restaurant_answer_list = filter(restaurant_list)
    # cafe_answer_list = filter(cafe_list)

    # 이거는 랜덤이라 무조건 넣어야됨
    destination_answer = destination_list[random.randrange(0, len(destination_list))]
    #destination_answer = destination_list
    # for restaurant in Write.objects.all():
    #     if str(restaurant.category) == '카페':
    #         continue
    #     if str(restaurant.google) != 'destination_answer':
    #         continue
    #     restaurant_list.append(restaurant)


    # for cafe in Write.objects.all():
    #     if str(cafe.category) != '식당':
    #         continue
    #     if str(cafe.google) != 'destination_answer':
    #         continue
    #     cafe_list.append(cafe)
    #     print(cafe_list)

    # restaurant_answer = restaurant_list
    # cafe_answer = cafe_list
    # restaurant_answer = restaurant_list[random.randrange(0, len(restaurant_list))]
    # cafe_answer = cafe_list[random.randrange(0, len(cafe_list))]
    
    # if str(cafe_list.google) == str(destination_answer.name):
    #     cafe_answer_list = cafe_list
    # cafe_answer = cafe_answer_list [random.randrange(0, len(cafe_answer_list))]

    # if str(restaurant_list.google) == str(destination_answer.name):
    #     restaurant_answer_list = restaurant_list
    # restaurant_answer = restaurant_answer_list[random.randrange(0, len(restaurant_answer_list))]
    
    return render(request, 'main/result.html',
     {'destination_answer' : destination_answer})

# def filter(info_dict):
#     for destination in Google.objects.all():
#         if info_dict['google'] == destination.name:
#             return info_dict