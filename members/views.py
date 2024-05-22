from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.shortcuts import redirect
import random
from .models import Member
from .forms import NewMemberForm


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def members(request):
    mymembers = Member.objects.all().values()
    for member in mymembers:
        member['bmi'] = round(
            member['weight'] / (member['height'] / 100) ** 2, 2)
        member['analysis'] = "過輕" if member['bmi'] < 18.5 else "正常" if member['bmi'] < 24 else "過重" if member[
            'bmi'] < 27 else "輕度肥胖" if member['bmi'] < 30 else "中度肥胖" if member['bmi'] < 35 else "重度肥胖"
    template = loader.get_template('members.html')
    return HttpResponse(template.render({'mymembers': mymembers}, request))


def create_random_members(request):
    family = "李王張劉陳楊黃趙周吳徐孫朱馬胡郭林何高梁鄭羅宋謝唐韓曹許鄧蕭馮曾程蔡彭潘袁於董餘蘇葉呂魏蔣田杜丁沈姜範江傅鐘盧汪戴崔任陸廖姚方金邱夏譚韋賈鄒石熊孟秦閻薛侯雷白龍段郝孔邵史毛常萬顧賴武康賀嚴尹錢施牛洪龔"
    given = "世中仁伶佩佳俊信倫偉傑儀元冠凱君哲嘉國士如娟婷子孟宇安宏宗宜家建弘強彥彬德心志忠怡惠慧慶憲成政敏文昌明智曉柏榮欣正民永淑玉玲珊珍珮琪瑋瑜瑞瑩盈真祥秀秋穎立維美翔翰聖育良芬芳英菁華萍蓉裕豪貞賢郁鈴銘雅雯霖青靜韻鴻麗龍"
    newMembers = []
    for i in range(10):
        name = f"{random.choice(
            [*family])}{random.choice([*given])}{random.choice([*given])}"
        height = random.randint(140, 190)
        weight = random.randint(45, 120)
        newOne = Member(name=name, height=height, weight=weight)
        newOne.save()
        newMembers.append(newOne)
    template = loader.get_template('add_result.html')
    return HttpResponse(template.render({'newMembers': newMembers, 'page': '隨機新增'}, request))


def new_member(request):
    if request.method == 'GET':
        new_member = loader.get_template('new_member.html')
        return HttpResponse(new_member.render({'form': NewMemberForm()}, request))
    elif request.method == 'POST':
        new_member_form = NewMemberForm(request.POST)
        if new_member_form.is_valid():
            new_member = new_member_form.save()
            template = loader.get_template('add_result.html')
            return HttpResponse(template.render({'newMembers': [new_member], 'page': '新增'}, request))
        else:
            template = loader.get_template('new_member.html')
            return HttpResponse(template.render({'form': new_member_form}, request))


def delete(request):
    Member.objects.all().delete()
    return redirect(reverse('members'))
