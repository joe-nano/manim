from manim import *


def firststep(t):
    return np.array((t, 1/t, 0))


class CarnotProcess(Scene):
    def construct(self):
        func = ParametricFunction(firststep,t_min=0.4, t_max=1, fill_opacity=0)
        dot = Dot().set_color(GREEN)
        self.add(dot)
        self.add(func)
        self.wait(0.1)

from pathlib import Path
if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l -p -s -smpl -c 'BLACK' --video_dir ~/Downloads/ " + script )