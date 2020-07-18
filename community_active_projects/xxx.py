from manim import *

class Heelloo(Scene):
    def construct(self):
        dot = Dot()
        x= TexMobject("hl")
        self.add(dot)
        self.wait(1)

from pathlib import Path
if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l -p -c 'BLACK' --video_dir ~/Downloads/ " + script )