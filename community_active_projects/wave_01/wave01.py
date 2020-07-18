from manim import *

from manim import *


def FolderScanner():
    from pathlib import Path
    prefix = "p"
    suffix = ".png"
    directory= Path.home() / "Documents/manim_resources/wave/no_disp"
    file_names= [subp for subp in directory.rglob('*') if  (prefix in subp.name) & (suffix == subp.suffix)]
    file_names.sort()
    file_names_string  = [str(file_name) for file_name in file_names]
    return file_names_string

class WaveScene(Scene):
    def construct(self):
        def get_image(imgs_list,image_number):
            return ImageMobject(imgs_list[int(image_number)]).scale(4)
        imgs=FolderScanner()
        current_frame = get_image(imgs,0)
        self.add(current_frame)
        tick_start=0; tick_end=len(imgs)
        val_tracker= ValueTracker(tick_start)
        def Tiny_Updater(frames, val_trackerX):
            def change_function(mob):
                val= int(val_trackerX.get_value())
                mob.become(get_image(imgs, val))
                return mob
            return UpdateFromFunc(frames, change_function)
        self.play(Tiny_Updater(current_frame,val_tracker),val_tracker.set_value,tick_end,rate_func= linear, run_time=1)


from pathlib import Path
if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim  -m  -c 'BLACK' --video_dir ~/Downloads/ " + script )