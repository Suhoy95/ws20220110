from django.http import JsonResponse
from django.contrib.staticfiles import finders


def maps(request):
    return JsonResponse({
        "name": "Мега-рогалик, всех времен и народов",
        "maps": [
            {
                "name": "первая карта",
                "img-source": "/static/blog/maps/map-1.png",
            },
            {
                "name": "вторая карта",
                "img-source": "/static/blog/maps/map-2.jpg",
            },
            {
                "name": "третья карта",
                "img-source": "/static/blog/maps/map-3.jpg",
            },
            {
                "name": "четвертая карта",
                "img-source": "/static/blog/maps/map-4.png",
            },
            {
                "name": "пятая карта",
                "img-source": "/static/blog/maps/map-5.jpg",
            },
            {
                "name": "шестая карта",
                "img-source": "/static/blog/maps/map-6.jpg",
            }
        ]
    })
