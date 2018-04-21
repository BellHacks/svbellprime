# -*- coding: utf-8 -*-
from random import shuffle, randint
from itertools import islice
from django.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _

from chartjs.colors import next_color, COLORS
from chartjs.views.columns import BaseColumnsHighChartsView
from chartjs.views.lines import BaseLineChartView, HighchartPlotLineChartView
from chartjs.views.pie import HighChartPieView, HighChartDonutView


class ColorsView(TemplateView):
    template_name = 'colors.html'

    def get_context_data(self, **kwargs):
        data = super(ColorsView, self).get_context_data(**kwargs)
        data['colors'] = islice(next_color(), 0, 50)
        return data


class ChartMixin(object):
    def get_providers(self):
        """Return names of datasets."""
        return ["Central", "Eastside", "Westside"]

    def get_labels(self):
        """Return 7 labels."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_data(self):
        """Return 3 random dataset to plot."""
        def data():
            """Return 7 randint between 0 and 100."""
            return [randint(0, 100) for x in range(7)]

        return [data() for x in range(3)]

    def get_colors(self):
        """Return a new shuffle list of color so we change the color
        each time."""
        colors = COLORS[:]
        shuffle(colors)
        return next_color(colors)


class ColumnHighChartJSONView(ChartMixin, BaseColumnsHighChartsView):
    title = _('Column Highchart test')
    yUnit = '%'
    providers = ['All']
    credits = {"enabled": False}

    def get_data(self):
        return [super(ColumnHighChartJSONView, self).get_data()]


class LineChartJSONView(ChartMixin, BaseLineChartView):
    pass


class LineHighChartJSONView(ChartMixin, HighchartPlotLineChartView):
    title = _('Line HighChart Test')
    y_axis_title = _('Kangaroos')

    # special - line charts credits are personalized
    credits = {
        'enabled': True,
        'href': 'http://example.com',
        'text': 'Novapost Team',
    }


class PieHighChartJSONView(ChartMixin, HighChartPieView):
    pass


class DonutHighChartJSONView(ChartMixin, HighChartDonutView):
    pass


# Pre-configured views.
colors = ColorsView.as_view()

column_highchart_json = ColumnHighChartJSONView.as_view()
line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()
line_highchart_json = LineHighChartJSONView.as_view()
pie_highchart_json = PieHighChartJSONView.as_view()
donut_highchart_json = DonutHighChartJSONView.as_view()
