import json

from django.core.paginator import Paginator
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


# Create your views here.
from showdata import models
from users.views import check_login


def test22(request):
    res = models.house.objects.all()
    json_list = []
    dic = {}
    for i in res:
        json_dict = model_to_dict(i)
        json_list.append(json_dict)
    # dic['code'] = '0'
    # dic['msg'] = ''
    # dic['count'] = 420
    # dic['data'] = json_list
    # # return JsonResponse(json_list,safe=False)
    # return HttpResponse(json.dumps(dic, ensure_ascii=False))
    page_index = request.GET.get('page')
    # 前台传来的一页显示多少条数据
    page_limit = request.GET.get('limit')
    # 分页器进行分配
    paginator = Paginator(json_list, page_limit)
    # 前端传来页数的数据
    data = paginator.page(page_index)
    # 放在一个列表里
    house_info = [x for x in data]
    # students.count()总数据量，layui的table模块要接受的格式
    students = {"code": 0, "msg": "", "count": res.count(), "data": house_info}
    return JsonResponse(students)
@check_login
def test3(request):
    return render(request, 'table2.html')

def to_add(request):
    return render(request, 'add2.html')

def to_edit(request):
    return render(request, 'edit2.html')

@csrf_exempt
def editdata(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # print(data["msg"])
        # print(data["id"])
        per_meter = format(10000*float(data['price'])/float(data['size']),'.1f')
        models.house.objects.filter(id=data["id"]).update(title=data['title'], msg=data['msg'], price=data['price'], per_meter=per_meter,size=data['size'])
        data = {"code": 200, "msg": "cg", "count": 1, "status":200}
        return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
def adddata(request):
    if request.method == 'POST':
        house = models.house()
        # print(request.body)
        data = json.loads(request.body)
        # print(data["msg"])
        house.title = data["title"]
        house.msg = data["msg"]
        house.price = data["price"]
        house.size = data["size"]
        house.per_meter = format(10000*float(house.price)/float(house.size), '.2f')
        house.save()
        data = {"code": 200, "msg": "cg", "count": 1, "status":200}
        return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
def deletedata(request):
    if request.method == 'POST':
        # print(request.body)
        datas = json.loads(request.body)
        # print(datas)
        for i in datas:
            models.house.objects.filter(id=i["id"]).delete()
        data = {"code": 200, "msg": "cg", "count": 1, "status":200}
        return HttpResponse(json.dumps(data), content_type="application/json")


@csrf_exempt
def delete_one_data(request):
    if request.method == 'POST':
        # print(request.body)
        data = json.loads(request.body)
        # print(data)
        models.house.objects.filter(id=data["id"]).delete()
        data = {"code": 200, "msg": "cg", "count": 1, "status":200}
        return HttpResponse(json.dumps(data), content_type="application/json")









def all_page(request):
    datas = models.house.objects.all()
    content={'data': datas}
    for data in datas:
        print(data.id)
    return render(request, 'table.html', content)

@csrf_exempt
def addstu(request):
    if request.method == "GET":
        return render(request, 'add.html')
    elif request.method == "POST":
        stu = models.house()
        stu.name = request.POST.get("Name")
        stu.gender = True
        stu.stuclass = request.POST.get("Stuclass")
        stu.address = request.POST.get("Address")
        stu.save()
        return redirect('/showdata/all')

def  change_page(request):
    stuid = request.GET.get("id")
    content = {'data': stuid}
    return render(request, 'change.html',content)

# 修改学生信息
@csrf_exempt
def update_student(request):

    name=request.POST.get("Name")
    gender=request.POST.get("Gender")
    stuclass = request.POST.get("Stuclass")
    address = request.POST.get("Address")
    id = request.GET.get("id")
    models.house.objects.filter(id=id).update(name=name,gender=True,stuclass=stuclass,address=address)
    return redirect('/showdata/all')

# 删除后重定向到主页面
def delete_student(request):
    models.house.objects.filter(id=request.GET.get("id")).delete()
    print(models.house.objects.filter(name=request.GET.get("id")))
    return redirect('/showdata/all')




def add_orm(request):
    stu = models.house()
    if request.method == "POST":
        stu.name = request.POST.get("name")
        if(request.POST.get("gender")=='男'):
            stu.gender = True
        else:
            stu.gender = False
        stu.clas = request.POST.get("address")
        stu.save()
    # obj1 = models.house(name = "asas",gender = True,clas="5班")
    # obj2 = models.house(name="asasaas", gender=True, clas="5班")
    # obj1.save()
    # obj2.save()
    return HttpResponse("ok")

def delete_orm(request):
    if request.method == "GET":
        print(request.GET.get("id"))
        print( models.house.objects.filter(name=request.GET.get("id")))
        models.house.objects.filter(name=request.GET.get("id")).delete()
    # models.house.objects.filter(name = "asas").delete()  # 删除的是queryset对象，也就是查询出来的所有记录
    # models.UserInfo.objects.filter(id=3)[0].delete()  # 删除的是queryset对象里面的元素，也就是单条记录
    return HttpResponse("ok")

def change_orm(request):
    ret = models.house.objects.filter(name = "sas")[0]
    ret.name = "pl2"
    ret.save()
    return HttpResponse("ok")


def query_orm(request):
    # 2. filter
    # 查询所有符合筛选条件的对象:条件可以是：参数，字典，Q
    fil = models.house.objects.filter(name='pl2')
    print("*********************************")
    return HttpResponse("ok")
