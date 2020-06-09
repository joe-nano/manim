from manim import *
from pathlib import Path

class Color_Updater(Scene):

    def construct(self):
        tick_start=1.0
        tick_end=2.0
        val_tracker= ValueTracker(tick_start)
        square= Square(fill_opacity=1).set_stroke(width=0)
        self.add(square)
        num_colors= 1000
        cols =  color_gradient([RED,WHITE,BLUE], num_colors)
        def dot_updater(mob):
            integ = int((val_tracker.get_value()-tick_start)/(tick_end-tick_start)*(num_colors-1))
            mob.set_color(cols[integ])
            print(integ)

        square.add_updater(dot_updater)
        self.play(val_tracker.set_value, tick_end, rate_func= linear,run_time=3)
        self.wait()

if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim   -l -c 'WHITE' --video_dir ~/Downloads/ " + script )