"""
"Tre modalità, un solo metodo" — tre anelli concentrici, un pianeta per
anello con un ritmo diverso (teoria lenta, esercizio veloce, recupero a
sosta e ripartenza). Un connettore sottile lega i tre punti in ogni istante,
per leggersi come un'unica orbita.
"""
from manim import *
from orbit_theme import *
import numpy as np


def recupero_angle(t, cycle=2.0, move_time=1.2, move_amount=1.35):
    full_cycles = int(t // cycle)
    local = t % cycle
    angle = full_cycles * move_amount
    if local < move_time:
        angle += move_amount * (local / move_time)
    else:
        angle += move_amount
    return angle


class TreModalita(Scene):
    def construct(self):
        self.camera.background_color = NAVY
        center = ORIGIN

        header = eyebrow_text("Tre modalità, un solo metodo")
        safe_zone_scale(header, max_width=3.9)
        header.to_edge(UP, buff=0.6)
        self.play(FadeIn(header, shift=DOWN * 0.2), run_time=0.6)

        r_teoria, r_esercizio, r_recupero = 1.85, 1.3, 0.75

        ring_teoria = hairline_ring(r_teoria, color=WHITE, opacity=0.14)
        ring_esercizio = hairline_ring(r_esercizio, color=ORANGE, opacity=0.18)
        ring_recupero = hairline_ring(r_recupero, color=WHITE, opacity=0.14)
        rings = VGroup(ring_teoria, ring_esercizio, ring_recupero).move_to(center)

        core = Dot(radius=0.05, color=ORANGE, fill_opacity=0.9).move_to(center)
        core_halo = Dot(radius=0.16, color=ORANGE, fill_opacity=0.18).move_to(center)

        self.play(Create(rings), FadeIn(core_halo, core), run_time=1.0)

        dot_teoria = planet_dot(color=WHITE)
        dot_esercizio = planet_dot(color=ORANGE)
        dot_recupero = planet_dot(color=ORANGE_SOFT)

        label_teoria = eyebrow_text("Teoria", color=SLATE, font_size=16)
        label_esercizio = eyebrow_text("Esercizio", color=ORANGE, font_size=16)
        label_recupero = eyebrow_text("Recupero", color=ORANGE_SOFT, font_size=16)

        label_teoria.move_to(point_on_ring(center, r_teoria + 0.32, 3 * PI / 4))
        label_esercizio.move_to(point_on_ring(center, r_esercizio + 0.3, -PI / 4))
        label_recupero.move_to(point_on_ring(center, r_recupero + 0.3, PI / 2))

        self.play(
            FadeIn(dot_teoria, dot_esercizio, dot_recupero),
            FadeIn(label_teoria, label_esercizio, label_recupero),
            run_time=0.6,
        )

        clock = ValueTracker(0)
        clock.add_updater(lambda m, dt: m.set_value(m.get_value() + dt))
        self.add(clock)

        speed_teoria = 0.5
        speed_esercizio = 2.15

        dot_teoria.add_updater(
            lambda m: m.move_to(point_on_ring(center, r_teoria, clock.get_value() * speed_teoria))
        )
        dot_esercizio.add_updater(
            lambda m: m.move_to(point_on_ring(center, r_esercizio, clock.get_value() * speed_esercizio))
        )
        dot_recupero.add_updater(
            lambda m: m.move_to(point_on_ring(center, r_recupero, recupero_angle(clock.get_value())))
        )

        connector = always_redraw(lambda: Polygon(
            dot_teoria.get_center(), dot_esercizio.get_center(), dot_recupero.get_center(),
            color=CYAN, stroke_width=1, stroke_opacity=0.28, fill_opacity=0,
        ))
        self.add(connector)

        self.wait(8.5)

        dot_teoria.clear_updaters()
        dot_esercizio.clear_updaters()
        dot_recupero.clear_updaters()
        clock.clear_updaters()

        self.play(
            FadeOut(VGroup(
                header, rings, core, core_halo, connector,
                dot_teoria, dot_esercizio, dot_recupero,
                label_teoria, label_esercizio, label_recupero,
            )),
            run_time=0.7,
        )
