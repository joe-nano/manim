from manim import *


class CarnotProcess(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 3,
        "x_axis_width": 9,
        "x_axis_label": "$V$",
        "x_tick_frequency": 1,
        "x_labeled_nums" :range(0,3,1),


        "y_min": 0,
        "y_max": 26,
        "y_tick_frequency": 1,
        "y_axis_label": "$P$",
        "y_labeled_nums" :range(0,26,2),

        "graph_origin": 2.5 * DOWN + 4 * LEFT,
        "function_color": RED,
        "axes_color": GREY,

        "x_label_direction": DOWN,
        "y_label_direction": LEFT,
    }

    def construct(self):
        R = 8.314
        Tmax = 300
        Tmin = 280
        self.setup_axes(animate=False)

        def isotherm_function_tmax(V):
            return (R*Tmax)/V*0.01

        def isotherm_function_tmin(V):
            return (R*Tmin)/V*0.01
        func_graph1 = self.get_graph(isotherm_function_tmax, x_min=1, x_max=2 ,color = RED)
        area1 = self.get_area(func_graph1,1,2)
        self.add(area1)
        self.add(func_graph1)

        func_graph2 = self.get_graph(isotherm_function_tmin, x_min=1, x_max=2 ,color = RED)
        area2 = self.get_area(func_graph2,1,2)
        self.add(area2)
        self.add(func_graph2)


from pathlib import Path

if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim   -p -s  -c 'BLACK' --video_dir ~/Downloads/ " + script)
