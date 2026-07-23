"""
ORBIT — tema Manim condiviso.

Palette, font e piccoli helper visivi coerenti con il sito (assets/css/blog.css
e index.html). Le prossime scene devono importare da qui invece di
ridefinire colori/font ogni volta.

Motivo grafico: anelli orbitali concentrici come linee hairline (1px),
punti "pianeta" piccoli, nessun elemento 3D/illustrativo/fotografico.
"""

from manim import *
import numpy as np

# ---------------------------------------------------------------------------
# Palette (dal brief + assets/css/blog.css)
# ---------------------------------------------------------------------------
NAVY = "#0F1E3D"          # sfondo principale
NAVY_ALT = "#0B1E3D"      # variante usata in index.html
NAVY_DEEP = "#071527"     # variante più scura
ORANGE = "#F5821F"        # accento primario
ORANGE_ALT = "#F2811D"    # variante usata in index.html
ORANGE_SOFT = "#F9A752"   # oro / accento secondario
CREAM = "#F6F4EF"
WHITE = "#FFFFFF"
SLATE = "#94A3B8"         # testo secondario
CYAN = "#22D3EE"          # accento spaziale, da usare con parsimonia

BACKGROUND = NAVY

# ---------------------------------------------------------------------------
# Font (devono essere installati nel sistema — vedi manim/README.md)
# ---------------------------------------------------------------------------
FONT_DISPLAY = "Space Grotesk"   # titoli / numeri
FONT_BODY = "Inter"              # testo
FONT_MONO = "IBM Plex Mono"      # eyebrow / etichette (sempre MAIUSCOLO)


# ---------------------------------------------------------------------------
# Helper di testo
# ---------------------------------------------------------------------------
def display_text(text, color=WHITE, weight=BOLD, font_size=48, **kwargs):
    return Text(text, font=FONT_DISPLAY, weight=weight, color=color, font_size=font_size, **kwargs)


def body_text(text, color=WHITE, font_size=32, **kwargs):
    return Text(text, font=FONT_BODY, color=color, font_size=font_size, **kwargs)


def eyebrow_text(text, color=ORANGE_SOFT, font_size=22, **kwargs):
    return Text(text.upper(), font=FONT_MONO, color=color, font_size=font_size, **kwargs)


# ---------------------------------------------------------------------------
# Helper orbitali
# ---------------------------------------------------------------------------
def hairline_ring(radius, color=WHITE, opacity=0.16, stroke_width=1.3):
    """Anello concentrico sottile, non un tubo 3D."""
    return Circle(radius=radius, color=color, stroke_width=stroke_width,
                   stroke_opacity=opacity, fill_opacity=0)


def planet_dot(color=WHITE, radius=0.055, glow=True):
    """Punto 'pianeta' vettoriale con un lieve alone, senza elementi 3D."""
    dot = Dot(radius=radius, color=color, fill_opacity=1)
    if not glow:
        return dot
    halo = Dot(radius=radius * 2.6, color=color, fill_opacity=0.16)
    group = VGroup(halo, dot)
    group.dot = dot
    group.halo = halo
    return group


def point_on_ring(center, radius, angle):
    return center + radius * np.array([np.cos(angle), np.sin(angle), 0])


def safe_zone_scale(mobject, max_width=3.9, max_height=None):
    """Adatta un mobject alla 'safe zone' condivisa da orizzontale e verticale
    (il vincolo reale è la larghezza in formato 1080x1920)."""
    if mobject.width > max_width:
        mobject.set(width=max_width)
    if max_height is not None and mobject.height > max_height:
        mobject.set(height=max_height)
    return mobject
