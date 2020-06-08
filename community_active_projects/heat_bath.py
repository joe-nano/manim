from manim import *


class Heat(Scene):
    def construct(self):
        def make_box():
            p1 = [0,1,0]
            p2 = [0,0,0]
            p3= [1,0,0]
            p4 = [1,1,0]
            l1 = Line(p1,p2)
            l2 = Line(p2,p3)
            l3 = Line(p3,p4)
            obj = VGroup(l1,l2,l3)
            return obj
        DISTANCELEFTRIGHT= 1.1
        hot = make_box().shift(DOWN+DISTANCELEFTRIGHT*LEFT)
        hot.add_background_rectangle(color=RED)
        cold = make_box().shift(DOWN+DISTANCELEFTRIGHT*RIGHT)
        cold.add_background_rectangle(color= BLUE)
        cold.text = TexMobject(r" \text{T}_{\text{max}}").scale(0.7).set_color(WHITE)
        cold.text.move_to(cold.get_center())
        obj = make_box()
        VGroup(obj,hot,cold,cold.text).to_edge(UR).shift(3*DOWN+LEFT*DISTANCELEFTRIGHT)
        self.add(obj,hot,cold,cold.text)
        self.play(VGroup(cold,hot).shift, RIGHT*DISTANCELEFTRIGHT)
        self.wait()
        self.play(VGroup(cold,hot).shift, LEFT*2*DISTANCELEFTRIGHT)
        self.play(VGroup(cold,hot).shift, RIGHT*DISTANCELEFTRIGHT)
        self.wait()

from pathlib import Path

if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim    -p -s -c 'BLACK' --video_dir ~/Downloads/ " + script)
