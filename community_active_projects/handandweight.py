from manim import *
from pathlib import Path

class lllll(Scene):

    def construct(self):
        path_hand = Path("/home/jan-hendrik/Documents/manim_resources/hand.svg")
        hand = SVGMobject(str(path_hand)).set_style(stroke_width=0)
        hand.submobjects[1].set_color(BLACK)
        hand.submobjects[0].set_color("#FCE8D0")

        #print(*hand.submobjects, sep="\n")
        self.add(hand.shift(4*LEFT))

        path_weight = Path("/home/jan-hendrik/Documents/manim_resources/weight.svg")
        weight = SVGMobject(str(path_weight)).set_color(GREY).set_stroke(width=0)
        #weight.set_stroke(color=BLACK , width=1)
        #print(*weight.submobjects, sep="\n")

        self.add(weight)
        self.play(VGroup(weight,hand).shift,UP)

if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim  -p -s -c 'WHITE' --video_dir ~/Downloads/ " + script )