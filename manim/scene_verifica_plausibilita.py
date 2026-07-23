"""
"Verifica di plausibilità" — un risultato assurdo viene scartato e corretto
in tempo reale, poi un segno di spunta conferma che il risultato ha senso.
"""
from manim import *
from orbit_theme import *
import numpy as np


class VerificaPlausibilita(Scene):
    def construct(self):
        self.camera.background_color = NAVY

        header = eyebrow_text("Verifica di plausibilità")
        safe_zone_scale(header, max_width=3.9)
        header.to_edge(UP, buff=0.6)
        self.play(FadeIn(header, shift=DOWN * 0.2), run_time=0.6)

        context = body_text("La velocità del ciclista è...", color=SLATE, font_size=22)
        safe_zone_scale(context, max_width=3.6)
        context.next_to(header, DOWN, buff=0.6)
        self.play(FadeIn(context), run_time=0.5)

        wrong = display_text("1.400 km/h", color=WHITE, font_size=44)
        safe_zone_scale(wrong, max_width=3.6)
        wrong.next_to(context, DOWN, buff=0.5)
        self.play(FadeIn(wrong, scale=1.15), run_time=0.6)

        warning = eyebrow_text("Improbabile", color=ORANGE, font_size=18)
        warning.next_to(wrong, DOWN, buff=0.35)
        self.play(FadeIn(warning), run_time=0.4)
        self.wait(1.0)

        right = display_text("24 km/h", color=ORANGE, font_size=44)
        right.move_to(wrong.get_center())

        self.play(FadeOut(warning), run_time=0.3)
        self.play(Transform(wrong, right), run_time=0.7)
        self.wait(0.3)

        check = VMobject(stroke_color=ORANGE, stroke_width=5, fill_opacity=0)
        check.set_points_as_corners([
            np.array([-0.32, -0.02, 0]),
            np.array([-0.08, -0.28, 0]),
            np.array([0.38, 0.32, 0]),
        ])
        check.next_to(wrong, DOWN, buff=0.55)

        plausible_label = eyebrow_text("Plausibile", color=ORANGE_SOFT, font_size=18)
        plausible_label.next_to(check, DOWN, buff=0.3)

        self.play(Create(check), run_time=0.6)
        self.play(FadeIn(plausible_label, shift=UP * 0.1), run_time=0.5)
        self.wait(2.2)

        self.play(
            FadeOut(VGroup(header, context, wrong, check, plausible_label)),
            run_time=0.7,
        )
