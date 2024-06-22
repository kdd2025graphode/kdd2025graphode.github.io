from bs4 import BeautifulSoup as Soup


final_html = ""
cnt = 1
with open('index.html', 'r') as f:
    for line in f.readlines():
        if """<table class="imgtable"><tr><td>""" in line:
            if cnt == 1:
                final_html = final_html + """<div class="columns">\n"""
                final_html = final_html + """<div class="keeptogether">\n"""
            if cnt == 6:
                final_html = final_html + """</div>\n"""
                # final_html = final_html + """<div class="keeptogether">\n"""
            if cnt == 9:
                # final_html = final_html + """</div>\n"""
                final_html = final_html + """<div class="keeptogether">\n"""
            cnt += 1

        if """<div id="footer">""" in line:
            final_html = final_html + """</div></div>\n"""

        final_html = final_html + line


with open('index.html', 'w') as f:
    f.write(final_html)
