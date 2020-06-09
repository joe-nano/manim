from manim import *


class XAxis(GraphScene):
    CONFIG = {
        "x_min": 5,
        "x_max": 10,
    }
    def construct(self):
        self.setup_axes(animate=False)
        self.x_axis.shift(LEFT*abs(self.y_axis[0].points[0]-self.x_axis[0].points[0]))
        graph_func = lambda x:(x-7)**2/2
        graph = self.get_graph(graph_func,x_min=5,x_max=9)
        self.add(graph)



from pathlib import Path

if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim   -p -s  -c 'BLACK' --video_dir ~/Downloads/ " + script)
