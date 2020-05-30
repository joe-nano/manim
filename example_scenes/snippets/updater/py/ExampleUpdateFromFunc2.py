from manim import *


class ExampleUpdateFromFunc2(Scene):

    def construct(self):
        run_setting = {"run_time": 1, "rate_func": linear}
        tick_start = 0
        tick_end = 100
        val_tracker= ValueTracker(tick_start)
        dot_disp= Dot().scale(3).set_color(GREEN)
        self.add(dot_disp)
        def Tiny_Updater(dots,val_trackerX):
            def small_change2(mob):
                mob.move_to(DOWN * 0.01 * val_trackerX.get_value())
                print(val_trackerX.get_value())
                return mob
            return UpdateFromFunc(dots, small_change2)


        tick_start = 0
        tick_end = 100
        self.play(Tiny_Updater(dot_disp,val_tracker),val_tracker.set_value,tick_end,**run_setting)
        self.wait()
        tick_end = 200
        self.play(Tiny_Updater(dot_disp,val_tracker),val_tracker.set_value,tick_end,**run_setting)



from pathlib import Path
if __name__ == "__main__":
    scene_name= "ExampleUpdateFromFunc2"
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim -i -l -p -c 'BLACK' --video_dir ~/Downloads/ " + script + " " + scene_name)
    os.system("ffmpeg -i ~/Downloads/" + scene_name + ".mp4" + " "+  "~/Downloads/"+ scene_name + ".gif")
