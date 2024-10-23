

from manim import *

class AES_simulation(Scene):
    def construct(self):
        encrypted_text = Text("ㅁ%&#*~ㅇ?")
        decrypted_text = Text("2aesthtic")
        lock = ImageMobject("Lock_icon.png")
        key = ImageMobject("Key_icon.png")
        lock.scale(0.5)
        key.scale(0.8)
        self.add(lock)
        self.add(key)
        lock.to_edge(LEFT)
        key.to_edge(RIGHT)
        encrypted_text.to_edge(LEFT)
        encrypted_text.to_edge(UP)
        decrypted_text.to_edge(RIGHT)
        decrypted_text.to_edge(UP)

        self.play(
            Write(encrypted_text),
        )
        self.play(
            lock.animate.center(),
            run_time=1
        )
        self.play(
            key.animate.move_to(lock.get_center()),
            run_time=1
        )
        self.play(
            Transform(encrypted_text, decrypted_text),
            run_time=2
        )