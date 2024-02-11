from manim import *


class DefaultTemplate(Scene):
    def construct(self):
        steps = [
            MathTex(
                "\\int", "_{-\\infty}", "^{+\\infty}", "e", "^{-x^{2}}", "dx",
            ),
            MathTex(
                "\\Bigg(", 
                    "\\int", "_{-\\infty}", "^{+\\infty}", "e", "^{-x^{2}}", "dx" ,"\\cdot", 
                    "\\int", "_{-\\infty}", "^{+\\infty}", "e", "^{-y^{2}}", "dy"
                "\\Bigg)", "^{\\frac{1}{2}}",
            ),
            MathTex(
                "\\Bigg(", "\\iint_{\\mathbb{R}}", "e", 
                    "^{-x^{2}-y^{2}}", "dx", "dy"
                "\\Bigg)", "^{\\frac{1}{2}}",
            ),
            MathTex(
                "\\Bigg(", "\\iint_{\\mathbb{R}}", "e", "^{-r^{2}}", 
                    "|\\mathcal{J}(\\theta, r)|", "d\\theta", "dr"
                "\\Bigg)", "^{\\frac{1}{2}}",
            ),
            MathTex(
                "\\Bigg(", "\\iint_{\\mathbb{R}}", "e", "^{-r^{2}}",  
                    "r", "d\\theta", "dr"
                "\\Bigg)", "^{\\frac{1}{2}}",
            ),
            MathTex(
                "\\Bigg(", "\\int", 
                    "_{0}", "^{2\\pi}", "d\\theta", "\\int", "_{0}", "^{\\infty}", "r", "e", "^{-r^{2}}", "dr"
                "\\Bigg)", "^{\\frac{1}{2}}",
            ),
            MathTex(
                "\\Bigg(", 
                    "2", "\\pi", "\\cdot", "\\frac{1}{2}", "\\int", "_{0}", "^{\\infty}", "e", "^{-r}", "dr"
                "\\Bigg)", "^{\\frac{1}{2}}",
            ),
            MathTex(
                "\\Big(", 
                    "\\pi", "\\cdot", "\\Gamma (1)"
                "\\Big)", "^{\\frac{1}{2}}",
            ),
            MathTex(
                    "\\pi", "^{\\frac{1}{2}}"
            ),
            MathTex(
                    "\\sqrt", "\\pi"
            ),
        ]

        self.play(Create(steps[0]))
        self.wait(0.25)

        for i in range(1, len(steps)):
            self.play(Transform(steps[0], steps[i]))
            self.wait(0.25)

        self.play(FadeOut(steps[0]))
