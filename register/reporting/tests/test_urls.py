from django.test import SimpleTestCase
from django.urls import resolve, reverse

from reporting.views import (
    ContestCreateView,
    ContestDeleteView,
    ContestDetailView,
    ContestListView,
    ContestUpdateView,
    render_students_select,
)


class TestContestUrls(SimpleTestCase):

    def test_contest_create_view_is_resolved(self):
        url = reverse('create')
        self.assertEquals(
            resolve(url).func.view_class, ContestCreateView,
        )

    def test_contest_list_view_is_resolved(self):
        url = reverse('list')
        self.assertEquals(
            resolve(url).func.view_class, ContestListView,
        )

    def test_contest_update_view_is_resolved(self):
        url = reverse('update', args=[1, ])
        self.assertEquals(
            resolve(url).func.view_class, ContestUpdateView,
        )

    def test_contest_delete_view_is_resolved(self):
        url = reverse('delete', args=[1, ])
        self.assertEquals(
            resolve(url).func.view_class, ContestDeleteView,
        )

    def test_contest_detail_view_is_resolved(self):
        url = reverse('detail', args=[1, ])
        self.assertEquals(
            resolve(url).func.view_class, ContestDetailView,
        )

    def test_render_students_select_is_resolved(self):
        url = reverse('render_students_select')
        self.assertEquals(
            resolve(url).func, render_students_select,
        )
