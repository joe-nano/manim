from manim import *


class Area(GraphScene):
    def construct(self):
        self.setup_axes()
        graph_func = lambda x:x**2/2
        graph = self.get_graph(graph_func,x_min=0,x_max=4)
        area = self.get_area(graph,t_min=0,t_max=6)
        self.add(graph,area)


from pathlib import Path

if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim   -p -s  -c 'BLACK' --video_dir ~/Downloads/ " + script)
