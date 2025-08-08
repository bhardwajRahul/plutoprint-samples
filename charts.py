import plutoprint

import matplotlib.pyplot as plt
import urllib.parse
import io

class CustomResourceFetcher(plutoprint.ResourceFetcher):
    def fetch_url(self, url):
        if not url.startswith('chart:'):
            return super().fetch_url(url)
        values = [float(v) for v in urllib.parse.unquote(url[6:]).split(',')]
        labels = [chr(65 + i) for i in range(len(values))]

        plt.bar(labels, values)
        plt.title('Bar Chart')
        plt.xlabel('Labels')
        plt.ylabel('Values')

        buffer = io.BytesIO()
        plt.savefig(buffer, format='svg', transparent=True)

        return plutoprint.ResourceData(buffer.getvalue(), "image/svg+xml", "utf-8")

book = plutoprint.Book(plutoprint.PAGE_SIZE_A4.landscape(), plutoprint.PAGE_MARGINS_NONE)

book.custom_resource_fetcher = CustomResourceFetcher()

HTML_CONTENT = """
<div>
    <img src='chart:23,45,12,36,28,50'>
    <img src='chart:5,15,25,35,45'>
    <img src='chart:50,40,30,20,10'>
    <img src='chart:10,20,30,40,50,60,70'>
</div>
"""

USER_STYLE = """
div { display: flex; flex-wrap: wrap; justify-content: center; height: 98vh }
img { flex: 0 0 45%; height: 50%; background: #fff; border: 1px solid #ccc; }
body { background: #f7f7f7 }
"""

book.load_html(HTML_CONTENT, USER_STYLE)
book.write_to_png("charts.png")
book.write_to_pdf("charts.pdf")
