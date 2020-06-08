from manim import *

zero_Celsius = 273.15

class CarnotProcessEntro(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 4,
        "x_axis_width": 9,
        "x_axis_label": "$S$",
        "x_tick_frequency": 4,
       # "x_labeled_nums" :range(0,3,1),


        "y_min": 0,
        "y_max": 10,
        "y_tick_frequency": 10,
        "y_axis_label": "$T$",

       # "y_labeled_nums" :range(0,26,2),

        "graph_origin": 2.5 * DOWN + 4 * LEFT,
        "function_color": RED,
        "axes_color": GREY,

        "x_label_direction": DOWN,
        "y_label_direction": LEFT,
    }

    def construct(self):
        R = 8.314
        Tmax=8
        Tmin=2
        S1=1
        S2=3
        self.setup_axes(animate=False)
        T_max_graph = self.get_graph(lambda x : Tmax, x_min=S1, x_max=S2 ,color = BLACK)
        T_min_graph = self.get_graph(lambda x : Tmin, x_min=S1, x_max=S2 ,color = BLACK)

        self.add(T_max_graph,T_min_graph)

        self.add(Line(T_max_graph.get_points()[0], T_min_graph.get_points()[0]).set_color(BLACK))
        self.add(Line(T_max_graph.get_points()[-1], T_min_graph.get_points()[-1]).set_color(BLACK))

        area_test = self.get_area(T_min_graph,S1,S2,bounded=T_max_graph)
        self.add(area_test)

        ddd= TexMobject(r"\Delta W").scale(0.7).move_to(area_test.get_center())
        bg= ddd.add_background_rectangle(color= WHITE)
        self.add(ddd)

        def get_y_value(input_tracker, graph):
            return graph.underlying_function(get_x_value(input_tracker))

        def get_graph_point(input_tracker,graph):
            return self.coords_to_point(get_x_value(input_tracker), get_y_value(input_tracker,graph))

        def get_x_value(input_tracker):
            return input_tracker.get_value()
        def get_x_point(input_tracker):
            return self.coords_to_point(get_x_value(input_tracker), 0)

        def get_y_point(input_tracker,graph):
            return self.coords_to_point(0, get_y_value(input_tracker,graph))
        def get_v_line(input_tracker,graph):
            return DashedLine(get_x_point(input_tracker), get_graph_point(input_tracker,graph), stroke_width=2).set_color(BLACK)

        def get_h_line(input_tracker,graph):
            return DashedLine(get_graph_point(input_tracker,graph), get_y_point(input_tracker,graph), stroke_width=2)


        input_tracker_p1 = ValueTracker(S1)
        v_line_p1 = get_v_line(input_tracker_p1,T_max_graph)
        graph_dot_p1 = Dot(color=BLACK)
        graph_dot_p1.move_to(get_graph_point(input_tracker_p1,T_max_graph))
        x_label_p1 = TexMobject("{ S }_{ 1 },{ S }_{ 4 }")
        x_label_p1.next_to(v_line_p1, DOWN)
        self.add(v_line_p1,graph_dot_p1,x_label_p1)
        num1 = TexMobject(r"{\large \textcircled{\small 1}} ").set_color(BLACK).scale(0.7)
        num1.next_to(graph_dot_p1,UP,buff=0.4*SMALL_BUFF)
        self.add(v_line_p1,graph_dot_p1,x_label_p1,num1)

        input_tracker_p1 = ValueTracker(S2)
        v_line_p1 = get_v_line(input_tracker_p1,T_max_graph)
        graph_dot_p1 = Dot(color=BLACK)
        graph_dot_p1.move_to(get_graph_point(input_tracker_p1,T_max_graph))
        x_label_p1 = TexMobject("{ S }_{ 2 },{ S }_{ 3 }")
        x_label_p1.next_to(v_line_p1, DOWN)
        num1 = TexMobject(r"{\large \textcircled{\small 2}} ").set_color(BLACK).scale(0.7)
        num1.next_to(graph_dot_p1,UP,buff=0.4*SMALL_BUFF)
        self.add(v_line_p1,graph_dot_p1,x_label_p1,num1)

        input_tracker_p1 = ValueTracker(S2)
        v_line_p1 = get_v_line(input_tracker_p1,T_min_graph)
        graph_dot_p1 = Dot(color=BLACK)
        graph_dot_p1.move_to(get_graph_point(input_tracker_p1,T_min_graph))
        self.add(v_line_p1,graph_dot_p1)#,x_label_p1)
        num1 = TexMobject(r"{\large \textcircled{\small 3}} ").set_color(BLACK).scale(0.7)
        num1.next_to(graph_dot_p1,DOWN,buff=0.4*SMALL_BUFF)
        num1.add_background_rectangle(color=WHITE)
        self.add(v_line_p1,graph_dot_p1,num1)
        h_line_p1 = get_h_line(input_tracker_p1,T_max_graph).set_color(BLACK)
        annot1 = TexMobject(r"\text{T}_{\text{max}}").next_to(h_line_p1,LEFT)
        self.add(h_line_p1,annot1)

        input_tracker_p1 = ValueTracker(S1)
        v_line_p1 = get_v_line(input_tracker_p1,T_min_graph)
        graph_dot_p1 = Dot(color=BLACK)
        graph_dot_p1.move_to(get_graph_point(input_tracker_p1,T_min_graph))
        self.add(v_line_p1,graph_dot_p1)#,x_label_p1)
        num1 = TexMobject(r"{\large \textcircled{\small 4}} ").set_color(BLACK).scale(0.7)
        num1.next_to(graph_dot_p1,DOWN,buff=0.4*SMALL_BUFF)
        num1.add_background_rectangle(color=WHITE)
        self.add(v_line_p1,graph_dot_p1,num1)
        h_line_p1 = get_h_line(input_tracker_p1,T_min_graph).set_color(BLACK)
        annot1 = TexMobject(r"\text{T}_{\text{min}}").next_to(h_line_p1,LEFT)
        self.add(h_line_p1,annot1)

        input_tracker_Q= ValueTracker(S1+(S2-S1)/2)
        graph_dot_p1 = Dot(color=BLACK)
        graph_dot_p1.move_to(get_graph_point(input_tracker_Q,T_max_graph))
        #self.add(graph_dot_p1)
        aa= Arrow(graph_dot_p1.get_center()+UP, graph_dot_p1.get_center(),buff=0).set_color(BLACK)
        self.add(aa)
        ddd= TexMobject(r"\Delta Q_a").scale(0.7)
        self.add(ddd.next_to(graph_dot_p1.get_center()+UR*0.5,UP,buff=0))

        input_tracker_Q= ValueTracker(S1+(S2-S1)/2)
        graph_dot_p1 = Dot(color=BLACK)
        graph_dot_p1.move_to(get_graph_point(input_tracker_Q,T_min_graph))
        #self.add(graph_dot_p1)
        aa= Arrow(graph_dot_p1.get_center(), graph_dot_p1.get_center()+DOWN,buff=0).set_color(BLACK)
        self.add(aa)
        ddd= TexMobject(r"\Delta Q_{ab}").scale(0.7)
        self.add(ddd.next_to(graph_dot_p1.get_center()+DOWN+UR*0.5,UP,buff=0))

from pathlib import Path

if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim    -s -p  -c 'WHITE' --video_dir ~/Downloads/ " + script)
