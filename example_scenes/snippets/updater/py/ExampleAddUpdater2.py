from manim import *

class ExampleAddUpdater2(Scene):
    def construct(self):
        path = VMobject()
        dot = Dot()
        path.set_points_as_corners([dot.get_center(),dot.get_center()])
        def update_path(path):
            previus_path = path.copy()
            previus_path.add_points_as_corners([dot.get_center()])
            path.become(previus_path)

        path.add_updater(update_path)

        self.add(path,dot)
        self.play(
            Rotating(
                dot,
                radians=PI,
                about_point=RIGHT,
                run_time=2
            )
        )
        self.wait(0.2)
        self.play(
            dot.shift,UP
        )
        self.play(
            dot.shift,LEFT
        )
        self.wait()


from pathlib import Path
if __name__ == "__main__":
    scene_name= "ExampleAddUpdater2"
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim -i -l -p -c 'BLACK' --video_dir ~/Downloads/ " + script + " " + scene_name)
    #os.system("ffmpeg -i ~/Downloads/" + scene_name + ".mp4" + " "+  "~/Downloads/"+ scene_name + ".gif")
