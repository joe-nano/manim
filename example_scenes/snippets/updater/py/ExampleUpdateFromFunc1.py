from manim import *



class ExampleUpdateFromFunc1(Scene): #Two Options to update a scene one more nested, one more explicit
    def construct(self):
        tick_start=0
        tick_end=100
        val_tracker= ValueTracker(tick_start)
        dot_disp= Dot()
        self.add(dot_disp)
        # version A
        def small_change(dot_disp,val_tracker):
            dot_disp.shift(UP * 0.001 * val_tracker.get_value())
            print(dot_disp.get_center()[1])
            return dot_disp
        self.play(
            UpdateFromFunc(
                dot_disp,
                lambda mob: mob.become(small_change(dot_disp,val_tracker))),
            val_tracker.set_value,tick_end, rate_func= linear
        )
        #  version B
        val_tracker= ValueTracker(tick_start)
        def Tiny_Updater(dots,val_trackerX):
            def small_change2(mob):
                mob.shift(DOWN * 0.001 * val_trackerX.get_value())
                return mob
            return UpdateFromFunc(dots, small_change2)
        self.play(Tiny_Updater(dot_disp,val_tracker),val_tracker.set_value,tick_end)
        self.wait()

from pathlib import Path
if __name__ == "__main__":
    scene_name= "ExampleUpdateFromFunc1"
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim -i -l -p -c 'BLACK' --video_dir ~/Downloads/ " + script + " " + scene_name)
    #os.system("ffmpeg -i ~/Downloads/" + scene_name + ".mp4" + " "+  "~/Downloads/"+ scene_name + ".gif")
