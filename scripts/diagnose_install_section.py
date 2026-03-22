import re
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph


def main() -> None:
    doc = Document("Manual.docx")

    blocks = []
    body = doc.element.body
    for child in body.iterchildren():
        tag = child.tag
        if tag.endswith("}p"):
            blocks.append(Paragraph(child, doc))
        elif tag.endswith("}tbl"):
            blocks.append(Table(child, doc))

    heading1 = []
    for idx, b in enumerate(blocks):
        if isinstance(b, Paragraph):
            s = (b.style.name if b.style else "") or ""
            if re.match(r"^Heading\s+1\s*$", s, re.IGNORECASE):
                t = (b.text or "").strip()
                if t:
                    heading1.append((idx, t))

    print("heading1_count:", len(heading1))
    install_idx = None
    install_title = None
    next_idx = None
    next_title = None

    for i, t in heading1:
        if "Install" in t or "install" in t:
            install_idx = i
            install_title = t
            break

    if install_idx is None:
        raise SystemExit("未找到 Heading 1: Install")

    for i, t in heading1:
        if i > install_idx:
            next_idx = i
            next_title = t
            break

    if next_idx is None:
        raise SystemExit("Install 后未找到下一个 Heading 1")

    print("install:", install_idx, install_title)
    print("next:", next_idx, next_title)

    between = blocks[install_idx + 1 : next_idx]
    p_count = 0
    nonempty_p = 0
    blip_total = 0
    table_count = 0

    for b in between:
        if isinstance(b, Paragraph):
            p_count += 1
            t = (b.text or "").strip()
            if t:
                nonempty_p += 1
            blips = b._element.xpath(".//a:blip")
            blip_total += len(blips)
        elif isinstance(b, Table):
            table_count += 1
            blips = b._element.xpath(".//a:blip")
            blip_total += len(blips)

    print("between_blocks:", len(between))
    print("paragraphs:", p_count, "nonempty_paragraphs:", nonempty_p)
    print("tables:", table_count)
    print("total_blip_images_in_between:", blip_total)

    # 打印前若干个段落/表格的概况，便于判断图片是否在段落内/表格内/完全不在
    shown = 0
    for b in between:
        if shown >= 15:
            break
        if isinstance(b, Paragraph):
            t = (b.text or "").strip()
            blips = b._element.xpath(".//a:blip")
            if t or blips:
                print(
                    "P: style=",
                    (b.style.name if b.style else ""),
                    "text_len=",
                    len(t),
                    "blips=",
                    len(blips),
                    "text_snip=",
                    t[:80].replace("\n", " "),
                )
                shown += 1
        elif isinstance(b, Table):
            blips = b._element.xpath(".//a:blip")
            if blips:
                print("T: rows=", len(b.rows), "cols=", len(b.columns), "blips=", len(blips))
                shown += 1


if __name__ == "__main__":
    main()

