from manim import *

class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello World", font_size=72)
        text.to_edge(UP)

        circle = Circle()

        self.play(
            Write(text, run_time=3)
        )
        self.play(
            Transform(text[0], circle),
            run_time=2,
            rate_functions=linear
        )