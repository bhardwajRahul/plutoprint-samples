import plutoprint

HTML_CONTENT = """
<div class="email">Email: contact@example.com</div>
<div class="tel">Tel: +1234567890</div>
<div class="website">Website: https://example.com</div>
"""

USER_STYLE = """
@page { @top-left-corner { content: -pluto-qrcode("https://github.com/plutoprint"); margin: 16px; } }
body { font-family: Arial, sans-serif; background-color: #f7f7f7; padding: 2em; }
div { margin-bottom: 2em; padding: 1em; background-color: #fff; border: 2px solid #ccc; border-radius: 8px; font-size: 1.2em; }
.email::before, .tel::before, .website::before { display: inline-block; vertical-align: middle; margin-right: 16px; width: 120px; height: 120px; }
.email::before { content: -pluto-qrcode("contact@example.com", green); }
.tel::before { content: -pluto-qrcode("+1234567890", blue); }
.website::before { content: -pluto-qrcode("https://example.com", red); }
"""

book = plutoprint.Book(plutoprint.PAGE_SIZE_LETTER)

book.load_html(HTML_CONTENT, USER_STYLE)
book.write_to_png("qrcodes.png")
book.write_to_pdf("qrcodes.pdf")
