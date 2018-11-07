import sys

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from .models import UserMessage
print(sys.path)


@csrf_exempt
def getform(request):
    message = None
    all_message = UserMessage.objects.filter(name='xiaolan1', address='hangzhou')

    if all_message:
        message = all_message[0]
        return render_to_response('message_form.html', {"my_message": message})

    if request.method == "POST":
        # 就是取字典里key对应value值而已。取name，取不到默认空
        name = request.POST.get('name', '')
        message = request.POST.get('message', '')
        address = request.POST.get('address', '')
        email = request.POST.get('email', '')
        print(name)
        print(message)
        print(address)
        print(email)
        # 实例化对象
        user_message = UserMessage()

        # 将html的值传入我们实例化的对象.
        user_message.name = name
        user_message.message = message
        user_message.address = address
        user_message.email = email
        user_message.object_id = "ijkl"

        # 调用save方法进行保存，写入数据库
        user_message.save()


    return render_to_response('message_form.html', {"my_message": message})
