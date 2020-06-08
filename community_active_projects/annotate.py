from manim import *

class Lala(Scene):
    def construct(self):
        num1 = TexMobject(r"{\large \textcircled{\small 1}} ").set_color(BLACK)
        num1.next_to(l1,DOWN,buff=SMALL_BUFF)
        num2 = TexMobject(r"{\large \textcircled{\small 2}} ").set_color(BLACK)
        num3 = TexMobject(r"{\large \textcircled{\small 3}} ").set_color(BLACK)
        num2.next_to(num3,UP)
        self.add(num1)
        self.wait(1)

from pathlib import Path
if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l -s -p -c 'WHITE' --video_dir ~/Downloads/ " + script )