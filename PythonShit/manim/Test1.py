from manim import *


class DefaultTemplate(Scene):
    def construct(self):

        G = Group()
        text_arr = ["aaaa1", "aaaa2", "aaaa3", "aaaa4", "aaaa5", "aaaa6"]
        sq = Square()

        for i in text_arr:
            t = Text(i, font_size=48, font="Classic Console Neue")
            self.add(t.move_to(np.array((-4.0, 0, 0.0)))), G.add(t)
            self.play(Write(t), run_time = 1)
            self.play(G.animate.shift(np.array((0.0, 1.0, 0.0))) , run_time = 1)

        self.play(G.animate.move_to(ORIGIN))
        self.play(Rotate(G, PI))
        self.play(Transform(G, MathTex("\\pi")))
        self.wait(1)
