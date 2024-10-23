from manim import *
import random  # Don't forget to import random for random choices

class PhotonSimulation(Scene):
    def construct(self):
        # Define the polarizer (yellow line)
        polarizer = Line(UP * 2.5, DOWN * 2.5, color=LIGHT_BROWN, stroke_width=8).shift(RIGHT * 2)
        self.add(polarizer)

        # Create a list of photons (blue dots)
        photons = [
            Dot(color=BLUE).shift(LEFT * 2.5 + UP * 2),  # Photon 1
            Dot(color=BLUE).shift(LEFT * 2.5 + UP),  # Photon 2
            Dot(color=BLUE).shift(LEFT * 2.5),  # Photon 3
            Dot(color=BLUE).shift(LEFT * 2.5 + DOWN * 1),  # Photon 4
            Dot(color=BLUE).shift(LEFT * 2.5 + DOWN * 2),  # Photon 5
            Dot(color=BLUE).shift(LEFT * 2.5 + DOWN * 3)   # Photon 6
        ]

        # Add the photons to the scene
        for photon in photons:
            self.add(photon)

        photon_results = []
        # Animate each photon moving to the polarizer
        for photon in photons:
            self.play(photon.animate.move_to(polarizer.get_center()), run_time=0.5)

            # Simulate the measurement result: green = 1, red = 0
            result_color = random.choice([GREEN, RED])
            bit_result = "1" if result_color == GREEN else "0"
            photon_results.append(bit_result)

            # Change the photon's color based on the result
            self.play(photon.animate.set_color(result_color))

            # Display the bit result (1 for green, 0 for red) near the photon
            result_text = Text(bit_result, color=result_color).scale(0.75).next_to(photon, RIGHT)
            self.play(Write(result_text))
            self.play(
                FadeOut(result_text)
            )

        all_results_text = Text(f"Results: {' '.join(photon_results)}", color=WHITE).scale(0.75).to_edge(DOWN)
        self.play(Write(all_results_text))