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
        "num_rects" : 5000
    }

    def construct(self):
        R = 8.314
        T = 300
        self.setup_axes(animate=False)

        def isotherm_function_tmax(V):
            return (R*T)/V*0.01

        def get_y_value(input_tracker, graph):
            return graph.underlying_function(get_x_value(input_tracker))

        def get_graph_point(input_tracker,graph):
            print(self.coords_to_point(get_x_value(input_tracker), get_y_value(input_tracker,graph)))
            return self.coords_to_point(get_x_value(input_tracker), get_y_value(input_tracker,graph))

        def get_x_value(input_tracker):
            return input_tracker.get_value()

        func_graph = self.get_graph(isotherm_function_tmax, x_min=1, x_max=2 ,color = RED)
        self.add(func_graph)
        moving_dot = Dot()
        V1= 1
        V2= 2
        val_tracker1=ValueTracker(V1)
        val_tracker2= ValueTracker(V2)
        moving_dot.move_to(get_graph_point(val_tracker1,func_graph)).set_color(GREEN)
        self.add(moving_dot)
        moving_dot.add_updater(lambda x: x.move_to(get_graph_point(val_tracker1,func_graph)).set_color(GREEN))
        self.add(moving_dot)
        self.play(val_tracker1.set_value, val_tracker2.get_value(), rate_func= linear,run_time=3)
        self.wait()

        def make_box():
            p1 = [0,1,0]
            p2 = [0,0,0]
            p3= [1,0,0]
            p4 = [1,1,0]
            l1 = Line(p1,p2)
            l2 = Line(p2,p3)
            l3 = Line(p3,p4)
            obj = VGroup(l1,l2,l3)
            return obj
        DISTANCELEFTRIGHT= 1.1
        hot = make_box().shift(DOWN+DISTANCELEFTRIGHT*LEFT)
        hot.add_background_rectangle(color=RED)
        cold = make_box().shift(DOWN+DISTANCELEFTRIGHT*RIGHT)
        cold.add_background_rectangle(color= BLUE)
        obj = make_box()
        VGroup(obj,hot,cold).to_edge(UR).shift(3*DOWN+LEFT*DISTANCELEFTRIGHT)
        self.add(obj,hot,cold)

from pathlib import Path
if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim  -p -s -c 'BLACK' --video_dir ~/Downloads/ " + script )