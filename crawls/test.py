"""月ごとのカスタムカレンダーのhtmlを作成し、ブラウザで開く."""
import calendar
import webbrowser

BASE_HTML = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <!-- style -->
    {}
</head>
<body>
    <!-- ここにカレンダーを挿入する　-->
    {}
</body>
</html>
"""

STYLE = """
<style>
    .month-table {
        width: 100%;
        max-width: 100%;
        margin-bottom: 1rem;
        table-layout: fixed;
    }
 
    .month-table td, .month-table th {
        border: 1px solid #eceeef;
        padding: .75rem;
        vertical-align: top;
    }
 
    .month-table tr{
        height: 100px;
    }
</style>
"""


class MyCalendar(calendar.LocaleHTMLCalendar):
    """カスタムカレンダー."""


    def formatday(self, day, weekday):
        """tableタグの日付部分のhtmlを作成する<td>...</td>."""
        if day == 0:
            return '<td class="noday">&nbsp;</td>'  # day outside month
        else:
            base_html = '<td class="{}"><a href="#">{}</a></td>'
            return base_html.format(self.cssclasses[weekday], day)

    def formatmonth(self, theyear=None, themonth=None, withyear=True):
        """月のカレンダーを作成する."""
        if theyear is None:
            theyear = self.date.year
        if themonth is None:
            themonth = self.date.month
        v = []
        a = v.append
        # classにtableを足しただけ！
        a('<table class="month-table">')
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek(week))
            a('\n')
        a('</table>')
        a('\n')
        return ''.join(v)


my_calendar = MyCalendar()
my_calendar_html = my_calendar.formatmonth(2018, 4)
result_html = BASE_HTML.format(STYLE, my_calendar_html)
# with open('calendar.html', 'w') as file:
#     file.write(result_html)

