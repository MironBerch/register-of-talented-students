from django.views import View
from django.http import JsonResponse
from django.shortcuts import render


JSON_DUMPS_PARAMS = {'ensure_ascii': False}


class View(View):
    """Базовый класс для вьювсб обрабатывает исключения"""

    def dispatch(self, request, *args, **kwargs):
        try: 
            response = super().dispatch(request, *args, **kwargs)
        except Exception:
            return self._response({'errorMessage': 'Ошибка'}, status=400)

        if isinstance(response, (dict, list)):
            return self._response(response)
        else:
            return response

    @staticmethod
    def _response(data, *, status=200):
        return JsonResponse(
            data, status=status, safe=not isinstance(data, list), json_dumps_params=JSON_DUMPS_PARAMS
        )


def bad_request(request, exception):
    return render(request, "misc/400.html", status=400)


def access_denied_error(request, exception):
    return render(request, "misc/403.html", status=403)


def page_not_found(request, exception):
    return render(request, "misc/404.html", {"path": request.path}, status=404)


def server_error(request):
    return render(request, "misc/500.html", status=500)