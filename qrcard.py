import plutoprint

HTML_CONTENT = """
<table>
  <tr>
    <th class="email">Email</th>
    <th class="tel">Tel</th>
  </tr>
  <tr>
    <th class="website">Website</th>
    <th class="github">GitHub</th>
  </tr>
</table>
"""

USER_STYLE = """
body {
  margin: 0;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #f7f7f7;
  font: 16px Arial;
}

table {
  border-spacing: 2rem;
  background: #fff;
  padding: 2rem;
  border: 1px solid #ccc;
  border-radius: 16px;
}

th::before {
  display: block;
  width: 130px;
  height: 130px;
  margin: 0 auto 0.8rem;
}

.email::before   { content: -pluto-qrcode('mailto:contact@example.com', #16a34a); }
.tel::before     { content: -pluto-qrcode('tel:+1234567890', #2563eb); }
.website::before { content: -pluto-qrcode('https://example.com', #ef4444); }
.github::before  { content: -pluto-qrcode('https://github.com/plutoprint', #f59e0b); }
"""

book = plutoprint.Book(plutoprint.PAGE_SIZE_LETTER.landscape())
book.load_html(HTML_CONTENT, USER_STYLE)
book.write_to_png("qrcard.png")
book.write_to_pdf("qrcard.pdf")
