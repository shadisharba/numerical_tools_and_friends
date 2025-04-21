# pymupdf supports PDF, XPS, EPUB, MOBI, FB2, CBZ, SVG, text and image files
# https://pymupdf.readthedocs.io/en/latest/the-basics.html

import pymupdf

doc = pymupdf.open("../../../data_repo/loremIpsum.pdf")

print(doc.page_count)
print(doc.metadata)

out = open("loremIpsum.txt", "wb")  # create a text output
for page in doc:  # iterate the document pages
    text = page.get_text().encode("utf8")  # get plain text (is in UTF-8)
    out.write(text)  # write text of page
    out.write(bytes((12,)))  # write page delimiter (form feed 0x0C)
out.close()
