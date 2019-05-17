import pdfkit

import utils
from make_html import make_html


def make_pdf(file):
    htmltext = make_html(file)
    with open(file.replace(".fit", ".html"), "w") as f:
        f.write(htmltext)
    pdfkit.from_file(file.replace(".fit", ".html"), file.replace(".fit", ".pdf"))


if __name__ == "__main__":
    utils.apply_to_fitfile(make_pdf, all=True)
