from django.shortcuts import render
from django.views import generic
from scalendar.views import MonthCalendarMixin


class MonthCalendar(MonthCalendarMixin, generic.TemplateView):
    """月間カレンダーを表示するビュー"""
    template_name = 'sampleapp/month.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['month'] = self.get_month_calendar()
        return context
