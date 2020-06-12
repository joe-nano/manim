from manim import *

class DOt(Scene):
    def construct(self):
        sourunding_dot = Dot().scale(1.3).set_fill(color=BLACK).set_z_index(-1)
        innerdot = Dot().set_color("#669900")
        moving_dot= VGroup(sourunding_dot,innerdot)
        self.add(moving_dot)

        self.wait()


from pathlib import Path
if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim  -s -p -c 'WHITE' --video_dir ~/Downloads/ " + script )