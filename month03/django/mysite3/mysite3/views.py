from django.shortcuts import render
from django.http import HttpResponse


def social_security(request):
    if request.method == 'GET':
        return render(request, 'social_security.html')
    elif request.method == 'POST':
        # 处理数据阶段
        base = request.POST.get('base', '0')
        base = float(base)
        is_city = request.POST.get('is_city', '1')
        # 计算社保
        yl_gr = base * 0.08
        yl_dw = base * 0.19

        sy_dw = base * 0.008
        if is_city:
            # 城镇户口
            sy_gr = base * 0.002
        else:
            sy_gr = 0
        # 此处省略
        return render(request, 'social_security.html', locals())

    return HttpResponse('---Please use GET or POST !---')
