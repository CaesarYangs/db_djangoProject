from django.http import HttpResponse
from django.shortcuts import render


def list(request):
    return HttpResponse("以下为数据库信息")


