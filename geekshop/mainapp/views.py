from django.shortcuts import render


def main(request):
    return render(request, 'mainapp/index.html')


def about(request):
    return render(request, 'mainapp/about.html')


def contact(request):
    return render(request, 'mainapp/contact.html')

def pricelist(request):
    return render(request, 'mainapp/pricelist.html')

    # links_menu = [
    #     {'href': 'all', 'name': 'Все'},
    #     {'href': 'k', 'name': 'КОНУСНО-ЛУЧЕВАЯ КОМПЬЮТЕРНАЯ ТОМОГРАФИЯ'},
    #     {'href': 'c', 'name': 'ИССЛЕДОВАНИЕ ВИСОЧНО-НИЖНЕЧЕЛЮСТНЫХ СУСТАВОВ'},
    #     {'href': 'l', 'name': 'ИССЛЕДОВАНИЕ ЛОР-ОРГАНОВ'},
    #     {'href': 'o', 'name': 'ОРТОПАНТОМОГРАФИЯ'},
    #     {'href': 't', 'name': 'ТЕЛЕРЕНТГЕНОГРАФИЯ'},
    #     {'href': 'd', 'name': 'ДОПОЛНИТЕЛЬНЫЕ УСЛУГИ'},
    #     {'href': 'kompl', 'name': 'КОМПЛЕКСНЫЕ ПРЕДЛОЖЕНИЯ'}
    # ]
    #
    # content = {
    #     'title': title,
    #     'links_menu': links_menu,
    #    'same_products': same_products
    # }
    # return render(request, 'mainapp/pricelist.html', context=content)