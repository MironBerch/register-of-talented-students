from django.views import View
from django.http import JsonResponse
from django.shortcuts import render


JSON_DUMPS_PARAMS = {'ensure_ascii': False}


class View(View):
    """Base view class for error processing"""

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


def bad_request_view(request, *args, **kwargs):
    response = render(request, 'misc/400.html')
    response.status_code = 400
    return response


def permission_denied_view(request, *args, **kwargs):
    response = render(request, 'misc/403.html')
    response.status_code = 403
    return response


def page_not_found_view(request, *args, **kwargs):
    response = render(request, 'misc/404.html')
    response.status_code = 404
    return response


def server_error_view(request, *args, **kwargs):
    response = render(request, 'misc/500.html')
    response.status_code = 500
    return response