from manim import *

class Test(Scene):
    def construct(self):
        a=1
        dot = Dot()
        circ=Circle()
        circ.set_color(GREEN)
        rect=Rectangle()
        rect.set_fill(color=BLUE,opacity=0.5)
        self.add(circ)
        self.play(Transform(circ,rect))
        self.play(dot.shift,2*UP)
        self.add(dot)
        self.wait(1)
        print(a)


from pathlib import Path
if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim   -p -c 'BLACK' --video_dir ~/Downloads/ " + script )