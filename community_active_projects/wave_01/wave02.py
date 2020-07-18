from manim import *



class Wave02(Scene):

    def construct(self):
        tick_start=1
        tick_end=2
        val_tracker= ValueTracker(tick_start)
        dot_disp= Dot().set_color(RED)
        self.add(dot_disp)
        def dot_updater(mob):
            mob.set_y(val_tracker.get_value())

        dot_disp.add_updater(dot_updater)
        self.play(val_tracker.set_value, tick_end, rate_func= smooth, run_time=1)
        self.wait()

from pathlib import Path
if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim    -c 'BLACK' --video_dir ~/Downloads/ " + script )