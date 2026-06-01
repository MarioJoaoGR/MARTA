"""Build the MARTA presentation deck."""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from lxml import etree

# ---------- Palette (Midnight Executive + warm accent) ----------
NAVY = RGBColor(0x0D, 0x1B, 0x3D)
NAVY_SOFT = RGBColor(0x1E, 0x3A, 0x6F)
STEEL = RGBColor(0x6E, 0x8C, 0xB8)
ICE = RGBColor(0xE6, 0xEC, 0xF5)
PAPER = RGBColor(0xFA, 0xFB, 0xFD)
INK = RGBColor(0x14, 0x1B, 0x2C)
MUTED = RGBColor(0x5C, 0x6B, 0x7A)
CORAL = RGBColor(0xE0, 0x6B, 0x5C)

HEADER_FONT = "Cambria"
BODY_FONT = "Calibri"
MONO_FONT = "Consolas"

# ---------- Setup ----------
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
SW, SH = prs.slide_width, prs.slide_height
BLANK = prs.slide_layouts[6]


# ---------- Helpers ----------
def add_rect(slide, x, y, w, h, fill, line=None):
    shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    if line is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = line
        shp.line.width = Pt(1)
    shp.shadow.inherit = False
    return shp


def add_rounded(slide, x, y, w, h, fill, line=None):
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
    shp.adjustments[0] = 0.06
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    if line is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = line
        shp.line.width = Pt(1)
    shp.shadow.inherit = False
    return shp


def add_oval(slide, x, y, w, h, fill, line=None):
    shp = slide.shapes.add_shape(MSO_SHAPE.OVAL, x, y, w, h)
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    if line is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = line
        shp.line.width = Pt(1)
    shp.shadow.inherit = False
    return shp


def add_text(slide, x, y, w, h, text, *, font=BODY_FONT, size=14, bold=False,
             color=INK, align=PP_ALIGN.LEFT, valign=MSO_ANCHOR.TOP, italic=False,
             line_spacing=1.15):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = Emu(0)
    tf.margin_right = Emu(0)
    tf.margin_top = Emu(0)
    tf.margin_bottom = Emu(0)
    tf.vertical_anchor = valign
    lines = text.split("\n") if isinstance(text, str) else text
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = line_spacing
        r = p.add_run()
        r.text = line
        r.font.name = font
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.italic = italic
        r.font.color.rgb = color
    return tb


def add_runs(slide, x, y, w, h, runs, *, align=PP_ALIGN.LEFT,
             valign=MSO_ANCHOR.TOP, line_spacing=1.2):
    """runs: list of dicts {text, font, size, bold, color, italic, br}"""
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = Emu(0)
    tf.margin_right = Emu(0)
    tf.margin_top = Emu(0)
    tf.margin_bottom = Emu(0)
    tf.vertical_anchor = valign
    p = tf.paragraphs[0]
    p.alignment = align
    p.line_spacing = line_spacing
    for spec in runs:
        if spec.get("br"):
            p = tf.add_paragraph()
            p.alignment = align
            p.line_spacing = line_spacing
            continue
        r = p.add_run()
        r.text = spec["text"]
        r.font.name = spec.get("font", BODY_FONT)
        r.font.size = Pt(spec.get("size", 14))
        r.font.bold = spec.get("bold", False)
        r.font.italic = spec.get("italic", False)
        r.font.color.rgb = spec.get("color", INK)
    return tb


def add_arrow(slide, x1, y1, x2, y2, color=STEEL, weight=2):
    line = slide.shapes.add_connector(1, x1, y1, x2, y2)
    line.line.color.rgb = color
    line.line.width = Pt(weight)
    # add arrowhead via xml
    ln = line.line._get_or_add_ln()
    tail = etree.SubElement(ln, qn("a:tailEnd"))
    tail.set("type", "triangle")
    tail.set("w", "med")
    tail.set("len", "med")
    return line


def slide_number(slide, n, total=11, on_dark=False):
    color = ICE if on_dark else MUTED
    add_text(slide, Inches(12.3), Inches(0.35), Inches(1.0), Inches(0.3),
             f"{n:02d} / {total:02d}", font=BODY_FONT, size=10,
             color=color, align=PP_ALIGN.RIGHT, bold=True)


def eyebrow(slide, text, on_dark=False):
    color = CORAL if not on_dark else CORAL
    add_text(slide, Inches(0.7), Inches(0.55), Inches(8), Inches(0.3),
             text.upper(), font=BODY_FONT, size=11, bold=True,
             color=color)


def title(slide, text, on_dark=False, y=Inches(0.95)):
    color = ICE if on_dark else INK
    add_text(slide, Inches(0.7), y, Inches(12), Inches(1.0),
             text, font=HEADER_FONT, size=36, bold=True, color=color,
             line_spacing=1.05)


# ---------- SLIDE 1: TITLE ----------
s = prs.slides.add_slide(BLANK)
add_rect(s, 0, 0, SW, SH, NAVY)

# accent block — small motif (single coral square in corner)
add_rect(s, Inches(0.7), Inches(0.7), Inches(0.25), Inches(0.25), CORAL)
add_text(s, Inches(1.05), Inches(0.7), Inches(6), Inches(0.3),
         "GECAD  ·  PYTHON TEST GENERATION", size=11, bold=True,
         color=ICE)

# Big title
add_text(s, Inches(0.7), Inches(2.5), Inches(12), Inches(1.4),
         "MARTA", font=HEADER_FONT, size=110, bold=True, color=ICE,
         line_spacing=0.95)

# tagline
add_text(s, Inches(0.75), Inches(4.0), Inches(11.5), Inches(0.8),
         "A decoupled multi-agent architecture", font=HEADER_FONT,
         size=28, color=STEEL, italic=True)
add_text(s, Inches(0.75), Inches(4.5), Inches(11.5), Inches(0.8),
         "for Python test generation.", font=HEADER_FONT,
         size=28, color=STEEL, italic=True)

# bottom strip
add_text(s, Inches(0.7), Inches(6.7), Inches(6), Inches(0.3),
         "Mário João Gomes Ribeiro", size=12, color=ICE, bold=True)
add_text(s, Inches(0.7), Inches(7.0), Inches(6), Inches(0.3),
         "Theoretical overview", size=11, color=STEEL)


# ---------- SLIDE 2: The boring half (hook) ----------
s = prs.slides.add_slide(BLANK)
add_rect(s, 0, 0, SW, SH, PAPER)
eyebrow(s, "The motivation")
slide_number(s, 2)

title(s, "Tests are the unglamorous half of shipping software.")

add_text(s, Inches(0.7), Inches(2.05), Inches(11.5), Inches(0.6),
         "Naturally, we'd love an LLM to do it for us.",
         font=HEADER_FONT, size=22, italic=True, color=MUTED)

# Three concern cards
cards = [
    ("Tedious", "Long, repetitive, low-creativity.\nExactly what LLMs should excel at."),
    ("High-volume", "Coverage matters. Edge cases multiply.\nHumans cut corners; models don't tire."),
    ("Critical", "A weak suite gives false confidence.\nSo the bar is real, not just throughput."),
]
card_w = Inches(3.85)
card_h = Inches(2.7)
gap = Inches(0.25)
total_w = card_w * 3 + gap * 2
start_x = (SW - total_w) // 2
y = Inches(3.7)
for i, (h, body) in enumerate(cards):
    x = start_x + i * (card_w + gap)
    add_rect(s, x, y, card_w, card_h, RGBColor(0xFF, 0xFF, 0xFF))
    # accent corner square
    add_rect(s, x + Inches(0.4), y + Inches(0.4), Inches(0.22), Inches(0.22), CORAL)
    add_text(s, x + Inches(0.4), y + Inches(0.75), card_w - Inches(0.8), Inches(0.5),
             h, font=HEADER_FONT, size=22, bold=True, color=INK)
    add_text(s, x + Inches(0.4), y + Inches(1.4), card_w - Inches(0.8), Inches(1.3),
             body, size=14, color=MUTED, line_spacing=1.35)


# ---------- SLIDE 3: Why Python is hard ----------
s = prs.slides.add_slide(BLANK)
add_rect(s, 0, 0, SW, SH, PAPER)
eyebrow(s, "The problem")
slide_number(s, 3)
title(s, "Python doesn't make it easy.")

# Big quote on the left
add_text(s, Inches(0.7), Inches(2.2), Inches(6.5), Inches(1.0),
         "“What type is this variable?”",
         font=HEADER_FONT, size=32, italic=True, color=NAVY, bold=True,
         line_spacing=1.1)
add_text(s, Inches(0.7), Inches(3.15), Inches(6.5), Inches(0.8),
         "— Run the code and find out.",
         font=HEADER_FONT, size=22, italic=True, color=CORAL)

add_text(s, Inches(0.7), Inches(4.4), Inches(6.5), Inches(2.5),
         "No static types at write-time. To write a test, "
         "the LLM has to guess what objects look like — their methods, "
         "their attributes, the exceptions they raise.\n\n"
         "Guess wrong → hallucinated calls, broken imports, "
         "asserts on attributes that don't exist.",
         size=15, color=INK, line_spacing=1.45)

# Right: tiny side-by-side comparison
rx = Inches(8.0)
ry = Inches(2.2)
rw = Inches(4.8)
add_rect(s, rx, ry, rw, Inches(4.7), RGBColor(0xFF, 0xFF, 0xFF))

add_text(s, rx + Inches(0.35), ry + Inches(0.25), rw - Inches(0.7), Inches(0.35),
         "WHAT THE LLM SEES", size=10, bold=True, color=MUTED)

# Java side
add_text(s, rx + Inches(0.35), ry + Inches(0.7), rw - Inches(0.7), Inches(0.4),
         "Statically-typed language", size=13, bold=True, color=NAVY)
add_text(s, rx + Inches(0.35), ry + Inches(1.1), rw - Inches(0.7), Inches(0.6),
         "public void send(User u, Message m)",
         font=MONO_FONT, size=12, color=INK)
add_text(s, rx + Inches(0.35), ry + Inches(1.55), rw - Inches(0.7), Inches(0.5),
         "Types pin down the shape of the world.",
         size=12, color=MUTED, italic=True)

# divider
add_rect(s, rx + Inches(0.35), ry + Inches(2.25), rw - Inches(0.7), Inches(0.02), ICE)

# Python side
add_text(s, rx + Inches(0.35), ry + Inches(2.45), rw - Inches(0.7), Inches(0.4),
         "Python", size=13, bold=True, color=CORAL)
add_text(s, rx + Inches(0.35), ry + Inches(2.85), rw - Inches(0.7), Inches(0.6),
         "def send(u, m):",
         font=MONO_FONT, size=12, color=INK)
add_text(s, rx + Inches(0.35), ry + Inches(3.3), rw - Inches(0.7), Inches(1.2),
         "u and m are… whatever the caller passes.\n"
         "Could be a User, a dict, a Mock, a string.",
         size=12, color=MUTED, italic=True, line_spacing=1.3)


# ---------- SLIDE 4: The naïve approach ----------
s = prs.slides.add_slide(BLANK)
add_rect(s, 0, 0, SW, SH, PAPER)
eyebrow(s, "The naïve approach")
slide_number(s, 4)
title(s, "One LLM. One giant prompt. Everything at once.")

# Left: pipeline diagram (compact, leaves room for right column)
lx = Inches(0.7)
ly = Inches(2.4)
box_w = Inches(1.6)
box_h = Inches(1.0)
gap_x = Inches(0.35)
items = [("Source\ncode", NAVY_SOFT), ("Context\n(types, docs)", NAVY_SOFT)]
y0 = ly + Inches(0.5)
for i, (txt, col) in enumerate(items):
    add_rounded(s, lx, y0 + i * (box_h + Inches(0.2)), box_w, box_h, col)
    add_text(s, lx, y0 + i * (box_h + Inches(0.2)) + Inches(0.16), box_w, box_h,
             txt, color=ICE, size=13, bold=True, align=PP_ALIGN.CENTER, line_spacing=1.2)

# arrows merging into LLM
llm_x = lx + box_w + Inches(0.7)
llm_y = ly + Inches(0.75)
llm_w = Inches(2.0)
llm_h = Inches(1.5)
add_rounded(s, llm_x, llm_y, llm_w, llm_h, CORAL)
add_text(s, llm_x, llm_y + Inches(0.4), llm_w, Inches(0.5),
         "BIG LLM", font=HEADER_FONT, size=20, bold=True, color=RGBColor(0xFF, 0xFF, 0xFF),
         align=PP_ALIGN.CENTER)
add_text(s, llm_x, llm_y + Inches(0.9), llm_w, Inches(0.4),
         "one shot, all roles",
         size=11, italic=True, color=RGBColor(0xFF, 0xFF, 0xFF),
         align=PP_ALIGN.CENTER)

# arrows from inputs into LLM
add_arrow(s, lx + box_w, y0 + Inches(0.5), llm_x, llm_y + Inches(0.5))
add_arrow(s, lx + box_w, y0 + box_h + Inches(0.2) + Inches(0.5),
          llm_x, llm_y + Inches(1.0))

# output box
out_x = llm_x + llm_w + Inches(0.45)
out_y = ly + Inches(1.05)
add_rounded(s, out_x, out_y, Inches(1.4), box_h, NAVY)
add_text(s, out_x, out_y + Inches(0.25), Inches(1.4), box_h,
         "Tests", color=ICE, size=16, bold=True, align=PP_ALIGN.CENTER)
add_arrow(s, llm_x + llm_w, llm_y + Inches(0.75), out_x, out_y + Inches(0.5))

# Right: failure modes (starts well clear of output box at x=7.55)
rx = Inches(7.8)
ry = Inches(2.3)
add_text(s, rx, ry, Inches(4.8), Inches(0.4),
         "FAILURE MODES", size=11, bold=True, color=MUTED)

failures = [
    ("Hallucination", "calls a method the class doesn't have"),
    ("Stub-asserts", "the test passes — because it asserts nothing"),
    ("Invalid syntax", "import fails before any assertion runs"),
]
for i, (h, body) in enumerate(failures):
    y = ry + Inches(0.55) + i * Inches(1.15)
    # bullet circle
    add_oval(s, rx, y + Inches(0.18), Inches(0.18), Inches(0.18), CORAL)
    add_text(s, rx + Inches(0.35), y, Inches(4.5), Inches(0.4),
             h, size=15, bold=True, color=INK)
    add_text(s, rx + Inches(0.35), y + Inches(0.42), Inches(4.5), Inches(0.7),
             body, size=13, color=MUTED, italic=True)

# bottom tagline
add_text(s, Inches(0.7), Inches(6.5), Inches(12), Inches(0.5),
         "Cognitive overload: one mind, too many concerns.",
         font=HEADER_FONT, size=20, italic=True, color=NAVY, align=PP_ALIGN.CENTER)


# ---------- SLIDE 5: The insight ----------
s = prs.slides.add_slide(BLANK)
add_rect(s, 0, 0, SW, SH, NAVY)
add_rect(s, Inches(0.7), Inches(0.7), Inches(0.25), Inches(0.25), CORAL)
add_text(s, Inches(1.05), Inches(0.7), Inches(8), Inches(0.3),
         "THE INSIGHT", size=11, bold=True, color=CORAL)
slide_number(s, 5, on_dark=True)

add_text(s, Inches(0.7), Inches(1.5), Inches(12), Inches(1.4),
         "Specialise. Like a real engineering team.",
         font=HEADER_FONT, size=40, bold=True, color=ICE, line_spacing=1.1)

add_text(s, Inches(0.7), Inches(2.7), Inches(12), Inches(0.6),
         "Three roles, each with a smaller job and less rope to hang itself with.",
         font=HEADER_FONT, size=20, italic=True, color=STEEL)

# three cards
card_w = Inches(3.85)
card_h = Inches(3.2)
gap = Inches(0.25)
total_w = card_w * 3 + gap * 2
start_x = (SW - total_w) // 2
y = Inches(3.8)

roles = [
    ("01", "The Planner", "Reads the code's intent.\n\nDecides WHAT to test:\nhappy paths, edges, errors."),
    ("02", "The Coder", "Takes one scenario at a time.\n\nWrites HOW to test it\nas plain pytest code."),
    ("03", "The Loops", "Runs the tests.\n\nReads failures, rewrites.\nChases missing coverage."),
]
for i, (num, h, body) in enumerate(roles):
    x = start_x + i * (card_w + gap)
    add_rect(s, x, y, card_w, card_h, NAVY_SOFT)
    add_text(s, x + Inches(0.4), y + Inches(0.35), Inches(1), Inches(0.5),
             num, font=HEADER_FONT, size=22, bold=True, color=CORAL)
    add_text(s, x + Inches(0.4), y + Inches(0.9), card_w - Inches(0.8), Inches(0.6),
             h, font=HEADER_FONT, size=22, bold=True, color=ICE)
    add_text(s, x + Inches(0.4), y + Inches(1.65), card_w - Inches(0.8), Inches(1.5),
             body, size=14, color=STEEL, line_spacing=1.4)


# ---------- SLIDE 6: Architecture ----------
s = prs.slides.add_slide(BLANK)
add_rect(s, 0, 0, SW, SH, PAPER)
eyebrow(s, "The architecture")
slide_number(s, 6)
title(s, "Two phases. One pipeline.")

add_text(s, Inches(0.7), Inches(2.0), Inches(12), Inches(0.5),
         "Build the right context first. Then let focused agents do the work.",
         font=HEADER_FONT, size=18, italic=True, color=MUTED)

# Two big phase boxes
phase_y = Inches(3.0)
phase_h = Inches(3.4)
phase_w = Inches(5.7)
gap_x = Inches(0.5)
total = phase_w * 2 + gap_x
start_x = (SW - total) // 2

# Phase 1
x1 = start_x
add_rect(s, x1, phase_y, phase_w, phase_h, RGBColor(0xFF, 0xFF, 0xFF))
add_rect(s, x1, phase_y, Inches(0.18), phase_h, NAVY)
add_text(s, x1 + Inches(0.5), phase_y + Inches(0.35), Inches(3), Inches(0.4),
         "PHASE 1", size=11, bold=True, color=CORAL)
add_text(s, x1 + Inches(0.5), phase_y + Inches(0.75), phase_w - Inches(1.0), Inches(0.6),
         "Build the context", font=HEADER_FONT, size=24, bold=True, color=INK)

bullets = [
    ("PyCG + AST", "static call graph and class structure"),
    ("3-pass function analysis", "what it does, what it should do, merged"),
    ("Per-class summary", "and a how-to-use guide for each class"),
    ("Parameter type inference", "syntactic filter + semantic RAG (Chroma)"),
]
by = phase_y + Inches(1.5)
for i, (k, v) in enumerate(bullets):
    yy = by + i * Inches(0.43)
    add_oval(s, x1 + Inches(0.5), yy + Inches(0.13), Inches(0.12), Inches(0.12), CORAL)
    add_runs(s, x1 + Inches(0.75), yy, phase_w - Inches(1.3), Inches(0.4),
             [
                 {"text": k, "size": 13, "bold": True, "color": INK},
                 {"text": "  —  " + v, "size": 13, "color": MUTED, "italic": True},
             ])

# Phase 2
x2 = start_x + phase_w + gap_x
add_rect(s, x2, phase_y, phase_w, phase_h, RGBColor(0xFF, 0xFF, 0xFF))
add_rect(s, x2, phase_y, Inches(0.18), phase_h, CORAL)
add_text(s, x2 + Inches(0.5), phase_y + Inches(0.35), Inches(3), Inches(0.4),
         "PHASE 2", size=11, bold=True, color=CORAL)
add_text(s, x2 + Inches(0.5), phase_y + Inches(0.75), phase_w - Inches(1.0), Inches(0.6),
         "Multi-agent ReAct", font=HEADER_FONT, size=24, bold=True, color=INK)

bullets2 = [
    ("Planner agent", "3-scenario plan + RAG-fetched related functions"),
    ("Assertion agent", "one pytest function per scenario, isolated"),
    ("Inner loop", "Pylint → Pytest, RAG-assisted retries, up to 3×"),
    ("Outer loop", "N rounds, replays Planner with coverage feedback"),
]
for i, (k, v) in enumerate(bullets2):
    yy = by + i * Inches(0.43)
    add_oval(s, x2 + Inches(0.5), yy + Inches(0.13), Inches(0.12), Inches(0.12), CORAL)
    add_runs(s, x2 + Inches(0.75), yy, phase_w - Inches(1.3), Inches(0.4),
             [
                 {"text": k, "size": 13, "bold": True, "color": INK},
                 {"text": "  —  " + v, "size": 13, "color": MUTED, "italic": True},
             ])

# Arrow between
arrow_y = phase_y + phase_h // 2
add_arrow(s, x1 + phase_w, arrow_y, x2, arrow_y, color=NAVY, weight=3)
add_text(s, x1 + phase_w + Inches(0.05), arrow_y - Inches(0.45),
         gap_x - Inches(0.1), Inches(0.4),
         "feeds", size=11, italic=True, color=MUTED, align=PP_ALIGN.CENTER)


# ---------- SLIDE 7: Phase 1 under the hood ----------
s = prs.slides.add_slide(BLANK)
add_rect(s, 0, 0, SW, SH, PAPER)
eyebrow(s, "Phase 1 — under the hood")
slide_number(s, 7)
title(s, "PyCG turns code into a graph the LLM can travel.")

add_text(s, Inches(0.7), Inches(2.0), Inches(12), Inches(0.5),
         "Summaries are built bottom-up — the model sees what every callee does first.",
         font=HEADER_FONT, size=18, italic=True, color=MUTED)

# Left: small call-graph visualization on a white card
gx = Inches(0.7)
gy = Inches(3.0)
gw = Inches(5.8)
gh = Inches(3.7)
add_rect(s, gx, gy, gw, gh, RGBColor(0xFF, 0xFF, 0xFF))

node_w = Inches(2.0)
node_h = Inches(0.65)

# Top node — caller
n1_x = gx + (gw - node_w) // 2
n1_y = gy + Inches(0.45)
add_rounded(s, n1_x, n1_y, node_w, node_h, NAVY)
add_text(s, n1_x, n1_y + Inches(0.13), node_w, node_h,
         "process_user()", color=ICE, size=13, bold=True,
         align=PP_ALIGN.CENTER, font=MONO_FONT)

# Bottom-left callee
n2_x = gx + Inches(0.4)
n2_y = gy + Inches(2.0)
add_rounded(s, n2_x, n2_y, node_w, node_h, NAVY_SOFT)
add_text(s, n2_x, n2_y + Inches(0.13), node_w, node_h,
         "validate_email()", color=ICE, size=13, bold=True,
         align=PP_ALIGN.CENTER, font=MONO_FONT)

# Bottom-right callee
n3_x = gx + gw - Inches(0.4) - node_w
n3_y = gy + Inches(2.0)
add_rounded(s, n3_x, n3_y, node_w, node_h, NAVY_SOFT)
add_text(s, n3_x, n3_y + Inches(0.13), node_w, node_h,
         "send_email()", color=ICE, size=13, bold=True,
         align=PP_ALIGN.CENTER, font=MONO_FONT)

# Down arrows (calls)
add_arrow(s, n1_x + Inches(0.5), n1_y + node_h,
          n2_x + node_w // 2, n2_y, color=STEEL, weight=2)
add_arrow(s, n1_x + Inches(1.5), n1_y + node_h,
          n3_x + node_w // 2, n3_y, color=STEEL, weight=2)
add_text(s, gx + Inches(0.4), n1_y + node_h + Inches(0.1),
         gw - Inches(0.8), Inches(0.3),
         "calls", size=10, italic=True, color=MUTED, align=PP_ALIGN.CENTER)

# Annotation under the diagram
add_text(s, gx + Inches(0.3), gy + Inches(3.0), gw - Inches(0.6), Inches(0.4),
         "Summary of process_user is built knowing what",
         size=12, color=INK, italic=True, align=PP_ALIGN.CENTER)
add_text(s, gx + Inches(0.3), gy + Inches(3.3), gw - Inches(0.6), Inches(0.4),
         "validate_email and send_email actually do.",
         size=12, color=INK, italic=True, align=PP_ALIGN.CENTER)

# Right: three benefit cards
rx = Inches(7.0)
ry = Inches(3.0)
cw = Inches(5.6)
ch = Inches(1.15)
gap = Inches(0.18)

benefits = [
    ("Recursive function summaries",
     "Each function's docstring is grounded in summaries of its "
     "callees — not just its own source."),
    ("Inherited members resolved",
     "Class MRO is walked, so a subclass with inherited methods "
     "looks complete to type inference."),
    ("Import-aware RAG",
     "Only classes reachable from this file become retrieval "
     "candidates — not the whole project."),
]
for i, (h, body) in enumerate(benefits):
    y = ry + i * (ch + gap)
    add_rect(s, rx, y, cw, ch, RGBColor(0xFF, 0xFF, 0xFF))
    add_rect(s, rx, y, Inches(0.08), ch, CORAL)
    add_text(s, rx + Inches(0.3), y + Inches(0.18), cw - Inches(0.5), Inches(0.4),
             h, size=14, bold=True, color=INK)
    add_text(s, rx + Inches(0.3), y + Inches(0.55), cw - Inches(0.5), Inches(0.55),
             body, size=12, color=MUTED, line_spacing=1.35)

# Attribution footnote
add_text(s, Inches(0.7), Inches(7.0), Inches(12), Inches(0.3),
         "PyCG: Salis et al., 2020 (Apache 2.0) — vendored static-analysis library.",
         size=10, color=MUTED, italic=True)


# ---------- SLIDE 8: The two agents ----------
s = prs.slides.add_slide(BLANK)
add_rect(s, 0, 0, SW, SH, PAPER)
eyebrow(s, "Phase 2 — the agents")
slide_number(s, 8)
title(s, "Two agents, two concerns.")

col_w = Inches(5.9)
col_h = Inches(4.2)
gap = Inches(0.5)
start_x = (SW - col_w * 2 - gap) // 2
y = Inches(2.3)

# Planner card
x1 = start_x
add_rect(s, x1, y, col_w, col_h, RGBColor(0xFF, 0xFF, 0xFF))
add_text(s, x1 + Inches(0.45), y + Inches(0.4), Inches(3), Inches(0.4),
         "PLANNER AGENT", size=11, bold=True, color=CORAL)
add_text(s, x1 + Inches(0.45), y + Inches(0.8), col_w - Inches(0.9), Inches(0.6),
         "What is worth testing?", font=HEADER_FONT, size=24, bold=True, color=INK)
add_text(s, x1 + Inches(0.45), y + Inches(1.55), col_w - Inches(0.9), Inches(0.6),
         "Reads the rich context. Thinks in scenarios.",
         size=14, color=MUTED, italic=True)

# IO panel
add_rect(s, x1 + Inches(0.45), y + Inches(2.25), col_w - Inches(0.9), Inches(0.05), ICE)
add_text(s, x1 + Inches(0.45), y + Inches(2.4), Inches(2), Inches(0.3),
         "INPUT", size=10, bold=True, color=MUTED)
add_text(s, x1 + Inches(0.45), y + Inches(2.7), col_w - Inches(0.9), Inches(0.4),
         "source + summary + inferred types + missing lines",
         size=13, color=INK, font=MONO_FONT)
add_text(s, x1 + Inches(0.45), y + Inches(3.0), col_w - Inches(0.9), Inches(0.4),
         "+ RAG: 3 related functions for scenario inspiration",
         size=12, color=CORAL, font=MONO_FONT, italic=True)
add_text(s, x1 + Inches(0.45), y + Inches(3.45), Inches(2), Inches(0.3),
         "OUTPUT", size=10, bold=True, color=MUTED)
add_text(s, x1 + Inches(0.45), y + Inches(3.75), col_w - Inches(0.9), Inches(0.4),
         "JSON: 3 scenarios — happy path, edges, errors",
         size=13, color=INK, font=MONO_FONT)

# Assertion card
x2 = start_x + col_w + gap
add_rect(s, x2, y, col_w, col_h, RGBColor(0xFF, 0xFF, 0xFF))
add_text(s, x2 + Inches(0.45), y + Inches(0.4), Inches(3), Inches(0.4),
         "ASSERTION AGENT", size=11, bold=True, color=CORAL)
add_text(s, x2 + Inches(0.45), y + Inches(0.8), col_w - Inches(0.9), Inches(0.6),
         "How do I write that test?", font=HEADER_FONT, size=24, bold=True, color=INK)
add_text(s, x2 + Inches(0.45), y + Inches(1.55), col_w - Inches(0.9), Inches(0.6),
         "Receives one scenario. Doesn't care about strategy.",
         size=14, color=MUTED, italic=True)

add_rect(s, x2 + Inches(0.45), y + Inches(2.25), col_w - Inches(0.9), Inches(0.05), ICE)
add_text(s, x2 + Inches(0.45), y + Inches(2.4), Inches(2), Inches(0.3),
         "INPUT", size=10, bold=True, color=MUTED)
add_text(s, x2 + Inches(0.45), y + Inches(2.7), col_w - Inches(0.9), Inches(0.4),
         "one scenario + strict mocking rules",
         size=13, color=INK, font=MONO_FONT)
add_text(s, x2 + Inches(0.45), y + Inches(3.0), col_w - Inches(0.9), Inches(0.4),
         "+ RAG on retry: 2 similar tests as examples",
         size=12, color=CORAL, font=MONO_FONT, italic=True)
add_text(s, x2 + Inches(0.45), y + Inches(3.45), Inches(2), Inches(0.3),
         "OUTPUT", size=10, bold=True, color=MUTED)
add_text(s, x2 + Inches(0.45), y + Inches(3.75), col_w - Inches(0.9), Inches(0.4),
         "one pytest function, in its own test file",
         size=13, color=INK, font=MONO_FONT)

# bottom note
add_text(s, Inches(0.7), Inches(6.8), Inches(12), Inches(0.5),
         "Plans don't worry about syntax. Code doesn't worry about strategy.",
         font=HEADER_FONT, size=18, italic=True, color=NAVY, align=PP_ALIGN.CENTER)


# ---------- SLIDE 8: Inner loop ----------
s = prs.slides.add_slide(BLANK)
add_rect(s, 0, 0, SW, SH, PAPER)
eyebrow(s, "Inner loop")
slide_number(s, 9)
title(s, "Self-healing. Listen to pytest.")

# 4-step loop diagram on the left
lx = Inches(0.7)
ly = Inches(2.4)
box_w = Inches(2.4)
box_h = Inches(1.0)
gap_x = Inches(0.4)
gap_y = Inches(0.6)

# Top row: WRITE -> RUN
add_rounded(s, lx, ly, box_w, box_h, NAVY)
add_text(s, lx, ly + Inches(0.3), box_w, box_h, "Write test",
         color=ICE, size=15, bold=True, align=PP_ALIGN.CENTER)

add_rounded(s, lx + box_w + gap_x, ly, box_w, box_h, NAVY_SOFT)
add_text(s, lx + box_w + gap_x, ly + Inches(0.18), box_w, box_h,
         "Pylint\n→ Pytest",
         color=ICE, size=14, bold=True, align=PP_ALIGN.CENTER, line_spacing=1.15)

# Bottom row: REWRITE <- READ ERROR
add_rounded(s, lx, ly + box_h + gap_y, box_w, box_h, NAVY)
add_text(s, lx, ly + box_h + gap_y + Inches(0.3), box_w, box_h, "Rewrite",
         color=ICE, size=15, bold=True, align=PP_ALIGN.CENTER)

add_rounded(s, lx + box_w + gap_x, ly + box_h + gap_y, box_w, box_h, CORAL)
add_text(s, lx + box_w + gap_x, ly + box_h + gap_y + Inches(0.3), box_w, box_h,
         "Read error", color=ICE, size=15, bold=True, align=PP_ALIGN.CENTER)

# Arrows: top-left -> top-right, top-right -> bottom-right, bottom-right -> bottom-left, bottom-left -> top-left
add_arrow(s, lx + box_w, ly + box_h // 2, lx + box_w + gap_x, ly + box_h // 2)
add_arrow(s, lx + box_w + gap_x + box_w // 2, ly + box_h,
          lx + box_w + gap_x + box_w // 2, ly + box_h + gap_y)
add_arrow(s, lx + box_w + gap_x, ly + box_h + gap_y + box_h // 2,
          lx + box_w, ly + box_h + gap_y + box_h // 2)
add_arrow(s, lx + box_w // 2, ly + box_h + gap_y, lx + box_w // 2, ly + box_h)

# label "pass -> done" exit arrow
exit_x = lx + box_w + gap_x + box_w
exit_y = ly + box_h // 2
add_arrow(s, exit_x, exit_y, exit_x + Inches(0.7), exit_y, color=NAVY_SOFT)
add_text(s, exit_x + Inches(0.75), exit_y - Inches(0.25),
         Inches(2), Inches(0.4),
         "pass → done",
         size=12, color=NAVY_SOFT, bold=True)

# Right column commentary
rx = Inches(8.0)
ry = Inches(2.3)
add_text(s, rx, ry, Inches(4.8), Inches(0.4),
         "THIS IS REACT",
         size=11, bold=True, color=CORAL)
add_text(s, rx, ry + Inches(0.5), Inches(4.8), Inches(0.6),
         "Reason + Act, in a tight loop.",
         font=HEADER_FONT, size=22, bold=True, color=INK)

add_text(s, rx, ry + Inches(1.5), Inches(4.8), Inches(2.9),
         "Pylint first (cheap), then pytest with JSON report.\n\n"
         "On failure, the agent gets the real error plus 2 similar tested "
         "functions retrieved via RAG. It rewrites against ground truth — "
         "not a guess. Up to 3 attempts.",
         size=14, color=INK, line_spacing=1.45)

# Quarantine note
add_rect(s, rx, Inches(6.0), Inches(4.8), Inches(0.9), ICE)
add_text(s, rx + Inches(0.25), Inches(6.1), Inches(4.5), Inches(0.4),
         "Quarantine", size=12, bold=True, color=CORAL)
add_text(s, rx + Inches(0.25), Inches(6.4), Inches(4.5), Inches(0.5),
         "After 3 failed repairs → move to test_quarantine/ with the\n"
         "error appended. Suite stays green, evidence is kept.",
         size=11, color=MUTED, italic=True, line_spacing=1.3)


# ---------- SLIDE 9: Outer loop ----------
s = prs.slides.add_slide(BLANK)
add_rect(s, 0, 0, SW, SH, PAPER)
eyebrow(s, "Outer loop")
slide_number(s, 10)
title(s, "Coverage-driven. Chase the dark corners.")

# horizontal pipeline diagram
boxes = [
    ("Suite passes", NAVY_SOFT),
    ("Run coverage.py", NAVY_SOFT),
    ("Find missed lines", CORAL),
    ("Augment Planner prompt", NAVY),
    ("New scenarios", NAVY),
]
bx = Inches(0.7)
by = Inches(2.7)
bw = Inches(2.3)
bh = Inches(1.1)
bgap = Inches(0.18)

for i, (label, col) in enumerate(boxes):
    x = bx + i * (bw + bgap)
    add_rounded(s, x, by, bw, bh, col)
    add_text(s, x, by + Inches(0.3), bw, bh,
             label, color=ICE, size=13, bold=True, align=PP_ALIGN.CENTER, line_spacing=1.2)
    if i > 0:
        add_arrow(s,
                  bx + (i - 1) * (bw + bgap) + bw,
                  by + bh // 2,
                  x,
                  by + bh // 2)

# loop arrow back from last box to first
last_x = bx + (len(boxes) - 1) * (bw + bgap) + bw // 2
first_x = bx + bw // 2
loop_y = by + bh + Inches(0.45)
# down from last
add_arrow(s, last_x, by + bh, last_x, loop_y, color=NAVY, weight=2)
# left across
add_arrow(s, last_x, loop_y, first_x, loop_y, color=NAVY, weight=2)
# up into first
add_arrow(s, first_x, loop_y, first_x, by + bh, color=NAVY, weight=2)

add_text(s, first_x + Inches(0.2), loop_y - Inches(0.35),
         last_x - first_x - Inches(0.4), Inches(0.4),
         "repeat for N rounds (default: 3)",
         size=11, italic=True, color=NAVY_SOFT, align=PP_ALIGN.CENTER)

# Below — explanatory text in two columns
exp_y = Inches(5.5)
col_w = Inches(5.9)
add_text(s, Inches(0.7), exp_y, col_w, Inches(0.4),
         "Why this matters", size=12, bold=True, color=CORAL)
add_text(s, Inches(0.7), exp_y + Inches(0.4), col_w, Inches(1.6),
         "A naïve LLM writes a happy-path test and stops.\n"
         "Each round, the Planner is told MISSING LINES TO COVER and instructed "
         "to design scenarios that hit them.",
         size=13, color=INK, line_spacing=1.4)

add_text(s, Inches(7.0), exp_y, col_w, Inches(0.4),
         "It's a feedback signal", size=12, bold=True, color=CORAL)
add_text(s, Inches(7.0), exp_y + Inches(0.4), col_w, Inches(1.6),
         "Coverage isn't the goal — fault-finding is. But it's the cheapest, "
         "fastest signal the model can react to between rounds.",
         size=13, color=INK, line_spacing=1.4)


# ---------- SLIDE 10: Takeaway ----------
s = prs.slides.add_slide(BLANK)
add_rect(s, 0, 0, SW, SH, NAVY)
add_rect(s, Inches(0.7), Inches(0.7), Inches(0.25), Inches(0.25), CORAL)
add_text(s, Inches(1.05), Inches(0.7), Inches(8), Inches(0.3),
         "TAKEAWAYS", size=11, bold=True, color=CORAL)
slide_number(s, 11, on_dark=True)

add_text(s, Inches(0.7), Inches(1.4), Inches(12), Inches(1.4),
         "Two ideas worth stealing.",
         font=HEADER_FONT, size=44, bold=True, color=ICE, line_spacing=1.05)

# Two big numbered takeaways
ty = Inches(3.2)
th = Inches(2.6)
tw = Inches(5.9)
gap = Inches(0.5)
start_x = (SW - tw * 2 - gap) // 2

# Card 1
x1 = start_x
add_rect(s, x1, ty, tw, th, NAVY_SOFT)
add_text(s, x1 + Inches(0.5), ty + Inches(0.3), Inches(1), Inches(0.7),
         "01", font=HEADER_FONT, size=40, bold=True, color=CORAL)
add_text(s, x1 + Inches(0.5), ty + Inches(1.05), tw - Inches(1), Inches(0.6),
         "Specialise your agents.",
         font=HEADER_FONT, size=22, bold=True, color=ICE)
add_text(s, x1 + Inches(0.5), ty + Inches(1.7), tw - Inches(1), Inches(1.0),
         "Smaller context. Sharper job. Fewer hallucinations.\n"
         "One LLM doing three things badly < three prompts doing one thing well.",
         size=13, color=STEEL, line_spacing=1.45)

# Card 2
x2 = start_x + tw + gap
add_rect(s, x2, ty, tw, th, NAVY_SOFT)
add_text(s, x2 + Inches(0.5), ty + Inches(0.3), Inches(1), Inches(0.7),
         "02", font=HEADER_FONT, size=40, bold=True, color=CORAL)
add_text(s, x2 + Inches(0.5), ty + Inches(1.05), tw - Inches(1), Inches(0.6),
         "Close the loop with the runtime.",
         font=HEADER_FONT, size=22, bold=True, color=ICE)
add_text(s, x2 + Inches(0.5), ty + Inches(1.7), tw - Inches(1), Inches(1.0),
         "Don't trust the LLM — make it prove its work.\n"
         "Pytest and coverage are cheap, brutal, and honest teachers.",
         size=13, color=STEEL, line_spacing=1.45)

# Honest caveat at bottom
add_text(s, Inches(0.7), Inches(6.5), Inches(12), Inches(0.4),
         "Still regression tests — MARTA captures what the code does, not what it should do.",
         font=HEADER_FONT, size=14, italic=True, color=STEEL, align=PP_ALIGN.CENTER)
add_text(s, Inches(0.7), Inches(6.9), Inches(12), Inches(0.4),
         "Thank you.",
         font=HEADER_FONT, size=16, bold=True, color=ICE, align=PP_ALIGN.CENTER)


# ---------- Save ----------
out = "/Users/mario/Desktop/GECAD/Test4Py/MARTA_presentation.pptx"
prs.save(out)

# macOS: o python-pptx (via miniconda) deixa o atributo com.apple.quarantine,
# que faz com que o PowerPoint abra o ficheiro em Modo Protegido (read-only).
# Limpa todos os xattrs para o ficheiro abrir editável.
import subprocess
try:
    subprocess.run(["xattr", "-c", out], check=False)
except FileNotFoundError:
    pass  # not on macOS

print(f"Saved: {out}")
print(f"Slides: {len(prs.slides)}")
