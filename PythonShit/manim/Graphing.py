from manim import *


class DefaultTemplate(Scene):
    def construct(self):

        ax = Axes(
            x_range=(-10, 10, 1),
            y_range=(-5, 5, 1),
            x_length=20,
            y_length=10,
        ).add_coordinates()

        number_plane = NumberPlane(
            x_range=(-10, 10, 1),
            y_range=(-5, 5, 1),
            x_length=20,
            y_length=10,
            background_line_style={
                "stroke_color": DARK_BLUE,
                "stroke_width": 2,
                "stroke_opacity": 0.6
            }
        )

        graph = ax.plot(lambda x: np.sin(x), x_range=[-7, 7], 
                        use_smoothing=False, color=RED, stroke_width=5
                        )

        self.play(Write(number_plane), Write(ax), run_time=3)
        self.play(Create(graph), run_time=3)
        
        self.wait(1)
