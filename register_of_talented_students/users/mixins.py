from django.shortcuts import redirect


class SuperUserRequiredMixin:
    """Verify that user is superuser"""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('list')
        return super(SuperUserRequiredMixin, self).dispatch(request, *args, **kwargs)