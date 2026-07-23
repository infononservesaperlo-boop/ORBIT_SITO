"""
"Non si spiega, si fa emergere" — una domanda si apre in un piccolo albero
di passaggi che si accendono uno alla volta, fino al risultato finale.
"""
from manim import *
from orbit_theme import *


class DomandeGuida(Scene):
    def construct(self):
        self.camera.background_color = NAVY

        eyebrow = eyebrow_text("Metodo Orbit")
        eyebrow.to_edge(UP, buff=0.6)

        question = display_text("Che equazione è questa?", font_size=38)
        safe_zone_scale(question, max_width=3.8)
        question.move_to(ORIGIN).shift(UP * 0.2)

        self.play(FadeIn(eyebrow, shift=DOWN * 0.2), run_time=0.6)
        self.play(FadeIn(question, shift=UP * 0.15), run_time=0.9)
        self.wait(0.9)

        # la domanda si "riduce" a piccola etichetta in alto: si apre il percorso sotto
        small_q = body_text("«Che equazione è questa?»", color=SLATE, font_size=20)
        safe_zone_scale(small_q, max_width=3.6)
        small_q.next_to(eyebrow, DOWN, buff=0.35)
        self.play(Transform(question, small_q), run_time=0.7)

        steps_data = [
            ("01", "Riconosci il tipo di equazione"),
            ("02", "Isola l'incognita"),
            ("03", "Sostituisci i valori"),
        ]

        rows = VGroup()
        for num, label in steps_data:
            dot = Dot(radius=0.065, color=SLATE, fill_opacity=0.35)
            num_txt = eyebrow_text(num, color=SLATE, font_size=17)
            label_txt = body_text(label, color=SLATE, font_size=21)
            row = VGroup(dot, num_txt, label_txt).arrange(RIGHT, buff=0.16)
            rows.add(row)
        rows.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        safe_zone_scale(rows, max_width=3.8)
        rows.next_to(question, DOWN, buff=0.55)

        self.play(FadeIn(rows, shift=UP * 0.1), run_time=0.5)
        self.wait(0.2)

        prev_dot = None
        lines = VGroup()
        for row in rows:
            dot, num_txt, label_txt = row
            if prev_dot is not None:
                line = Line(prev_dot.get_center(), dot.get_center(),
                            color=ORANGE, stroke_width=1.5, stroke_opacity=0.7)
                self.play(Create(line), run_time=0.3)
                lines.add(line)
            self.play(
                dot.animate.set_fill(ORANGE, opacity=1),
                num_txt.animate.set_color(ORANGE),
                label_txt.animate.set_color(WHITE),
                run_time=0.45,
            )
            prev_dot = dot
            self.wait(0.15)

        result_box = RoundedRectangle(
            width=2.3, height=0.95, corner_radius=0.14,
            color=ORANGE, stroke_width=1.6, fill_color=NAVY_DEEP, fill_opacity=1,
        )
        result_txt = display_text("x = 3", color=ORANGE, font_size=38)
        result_txt.move_to(result_box.get_center())
        result = VGroup(result_box, result_txt)
        result.next_to(rows, DOWN, buff=0.55)

        self.play(FadeIn(result, scale=0.85), run_time=0.6)
        self.play(Flash(result_txt, color=ORANGE, flash_radius=0.85, line_length=0.25), run_time=0.5)
        self.wait(1.3)

        self.play(
            FadeOut(VGroup(eyebrow, question, rows, lines, result)),
            run_time=0.7,
        )
