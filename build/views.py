"""Django views for interacting with Build objects."""

from django.views.generic import DetailView, ListView

from .models import Build

from Vision_IMS.views import Vision_IMSRoleMixin
from Vision_IMS.status_codes import BuildStatus

from plugin.views import Vision_IMSPluginViewMixin


class BuildIndex(Vision_IMSRoleMixin, ListView):
    """View for displaying list of Builds."""
    model = Build
    template_name = 'build/index.html'
    context_object_name = 'builds'

    def get_queryset(self):
        """Return all Build objects (order by date, newest first)"""
        return Build.objects.order_by('status', '-completion_date')


class BuildDetail(Vision_IMSRoleMixin, Vision_IMSPluginViewMixin, DetailView):
    """Detail view of a single Build object."""

    model = Build
    template_name = 'build/detail.html'
    context_object_name = 'build'

    def get_context_data(self, **kwargs):
        """Return extra context information for the BuildDetail view"""
        ctx = super().get_context_data(**kwargs)

        build = self.get_object()

        ctx['BuildStatus'] = BuildStatus

        part = build.part

        ctx['part'] = part

        return ctx
