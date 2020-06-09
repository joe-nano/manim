from manim import *


class CarnotProcess(GraphScene):
    def construct(self):
        stamp_thickness  = 0.1
        def make_stemp():
            stemp  = Rectangle()
            p1 = [0,stamp_thickness,0]
            p2 = [0,0,0]
            p3= [0.75,0,0]
            p4 = [0.75,stamp_thickness,0]
            lines = []
            lines.append(Line(p2,p3).set_color(BLACK))
            lines.append(Line(p4,p1).set_color(BLACK))
            lines.append(Line(p1,p2).set_color(BLACK).shift(RIGHT*0.1*0.75))
            lines.append(Line(p1,p2).set_color(BLACK).shift(RIGHT*0.2*0.75))
            lines.append(Line(p1,p2).set_color(BLACK).shift(RIGHT*0.3*0.75))
            lines.append(Line(p1,p2).set_color(BLACK).shift(RIGHT*0.4*0.75))
            lines.append(Line(p1,p2).set_color(BLACK).shift(RIGHT*0.5*0.75))
            lines.append(Line(p1,p2).set_color(BLACK).shift(RIGHT*0.6*0.75))
            lines.append(Line(p1,p2).set_color(BLACK).shift(RIGHT*0.7*0.75))
            lines.append(Line(p1,p2).set_color(BLACK).shift(RIGHT*0.8*0.75))
            lines.append(Line(p1,p2).set_color(BLACK).shift(RIGHT*0.9*0.75))
            obj = VGroup(*lines)
            return obj
        stemp = make_stemp()
        self.add(stemp)
        V1=1
        V2=3
        V3=1.1
        val_tracker= ValueTracker(V1)
        def updater(x):
            offset=2
            x.set_y(val_tracker.get_value()-offset)
            return x
        stemp.add_updater(updater)
        self.add(stemp)
        self.play(val_tracker.set_value, V2, rate_func= linear)
        self.wait()
        self.play(val_tracker.set_value, V3, rate_func= linear)

        self.wait()

from pathlib import Path

if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim     -p    -c 'WHITE' --video_dir ~/Downloads/ " + script)
