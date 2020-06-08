from manim import *


class CarnotProcess(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 4,
        "x_axis_width": 9,
        "x_axis_label": "$V$",
        "x_tick_frequency": 4,
       # "x_labeled_nums" :range(0,3,1),


        "y_min": 0,
        "y_max": 40,
        "y_tick_frequency": 40,
        "y_axis_label": "$P$",
       # "y_labeled_nums" :range(0,26,2),

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
        import matplotlib.pyplot as plt
        from scipy.constants import zero_Celsius
        plt.rcParams['figure.dpi'] = 150

        Tmax = zero_Celsius+150
        Tmin = zero_Celsius+20
        R = 8.314
        kappa = 5/3
        V1= 1
        V2= 2

        p1 = R*Tmax/V1
        p2 = p1*V1/V2

        V3 = (Tmax/Tmin * V2**(kappa-1))**(1/(kappa-1))
        p3 = p2* V2**kappa / V3**kappa

        V4 = (Tmax/Tmin * V1**(kappa-1))**(1/(kappa-1))
        p4 = p3*V3/V4

        V12 = np.linspace(V1,V2,100)
        V23 = np.linspace(V2,V3,100)
        V34 = np.linspace(V3,V4,100)
        V41 = np.linspace(V4,V1,100)

        def p_isotherm(V,T):
            return (R*T)/V

        def p_adiabatisch(V,p_start,v_start):
            return (p_start*v_start**kappa)/V**kappa



        plt.plot(V12, p_isotherm(V12,Tmax),label = f"Tmax = {Tmax-zero_Celsius:.0f} °C")
        plt.plot(V23, p_adiabatisch(V23, p2,V2),label = f"Adia")
        plt.plot(V34, p_isotherm(V34,Tmin),label = f"Tmin = {Tmin-zero_Celsius:.0f} °C")
        plt.plot(V41, p_adiabatisch(V41, p4,V4),label = f"Adia2")

        isotherm12_graph = self.get_graph(lambda x : p_isotherm(x, Tmax)*0.01, x_min=V1, x_max=V2 ,color = BLACK)
        adiabatisch23_graph = self.get_graph(lambda x : p_adiabatisch(x, p2,V2)*0.01, x_min=V2, x_max=V3 ,color = BLACK)
        isotherm34_graph = self.get_graph(lambda x : p_isotherm(x, Tmin)*0.01, x_min=V3, x_max=V4 ,color = BLACK)
        adiabatisch41_graph = self.get_graph(lambda x : p_adiabatisch(x, p4,V4)*0.01, x_min=V4, x_max=V1 ,color = BLACK)

        isotherm12_graph_over = self.get_graph(lambda x : p_isotherm(x, Tmax)*0.01, x_min=V1-0.1, x_max=V2+0.5 ,color = RED, stroke_opacity=0.5)
        isotherm12_graph_over_Text = TexMobject(r" T_{max}").scale(0.5).next_to(isotherm12_graph_over,RIGHT,aligned_edge=DOWN, buff=0)
        self.add(isotherm12_graph_over,isotherm12_graph_over_Text)

        isotherm34_graph_over = self.get_graph(lambda x : p_isotherm(x, Tmin)*0.01, x_min=V3+0.3, x_max=V4-0.5 ,color = BLUE, stroke_opacity=0.5)
        isotherm34_graph_over_Text = TexMobject(r" T_{min}").scale(0.5).next_to(isotherm34_graph_over,RIGHT,aligned_edge=DOWN, buff=0)
        self.add(isotherm34_graph_over,isotherm34_graph_over_Text)

        upper_graph= self.get_graph(lambda x : p_isotherm(x, Tmax)*0.01  if x < V2 else p_adiabatisch(x, p2,V2)*0.01, x_min=V1-0.1, x_max=V2+0.5 ,color = RED, stroke_opacity=0.5)
        lower_graph = self.get_graph(lambda x :p_adiabatisch(x, p4,V4)*0.01 if x < V4 else p_isotherm(x, Tmin)*0.01)
        area_test = self.get_area(upper_graph,V1,V3,bounded=lower_graph)
        self.add(area_test)
        # area = self.get_area(isotherm12_graph,V1,V4,bounded=adiabatisch41_graph)
        # area2 = self.get_area(isotherm12_graph,V4,V2,bounded=isotherm34_graph)
        # area3 = self.get_area(adiabatisch23_graph,V2,V3,bounded=isotherm34_graph)
        #
        # self.add(area,area2,area3)



        self.add(isotherm12_graph,adiabatisch23_graph,isotherm34_graph,adiabatisch41_graph)
        self.wait(0.1)



        def get_y_value(input_tracker, graph):
            return graph.underlying_function(get_x_value(input_tracker))

        def get_graph_point(input_tracker,graph):
            return self.coords_to_point(get_x_value(input_tracker), get_y_value(input_tracker,graph))

        def get_x_value(input_tracker):
            return input_tracker.get_value()
        def get_x_point(input_tracker):
            return self.coords_to_point(get_x_value(input_tracker), 0)

        def get_v_line(input_tracker,graph):
            return DashedLine(get_x_point(input_tracker), get_graph_point(input_tracker,graph), stroke_width=2).set_color(BLACK)

        input_tracker_p1 = ValueTracker(V1)
        v_line_p1 = get_v_line(input_tracker_p1,isotherm12_graph)
        graph_dot_p1 = Dot(color=BLACK)
        graph_dot_p1.move_to(get_graph_point(input_tracker_p1,isotherm12_graph))
        x_label_p1 = TexMobject("{ V }_{ 1 }")
        x_label_p1.next_to(v_line_p1, DOWN)
        self.add(v_line_p1,graph_dot_p1,x_label_p1)
        num1 = TexMobject(r"{\large \textcircled{\small 1}} ").set_color(BLACK).scale(0.5)
        num1.next_to(graph_dot_p1,RIGHT,buff=0.4*SMALL_BUFF)
        self.add(v_line_p1,graph_dot_p1,x_label_p1,num1)

        input_tracker_p1 = ValueTracker(V2)
        v_line_p1 = get_v_line(input_tracker_p1,adiabatisch23_graph)
        graph_dot_p1 = Dot(color=BLACK)
        graph_dot_p1.move_to(get_graph_point(input_tracker_p1,adiabatisch23_graph))
        x_label_p1 = TexMobject("{ V }_{ 2 }")
        x_label_p1.next_to(v_line_p1, DOWN)
        num1 = TexMobject(r"{\large \textcircled{\small 2}} ").set_color(BLACK).scale(0.5)
        num1.next_to(graph_dot_p1,UP,buff=0.4*SMALL_BUFF)
        self.add(v_line_p1,graph_dot_p1,x_label_p1,num1)

        input_tracker_p1 = ValueTracker(V3)
        v_line_p1 = get_v_line(input_tracker_p1,isotherm34_graph)
        graph_dot_p1 = Dot(color=BLACK)
        graph_dot_p1.move_to(get_graph_point(input_tracker_p1,isotherm34_graph))
        x_label_p1 = TexMobject("{ V }_{ 3 }")
        x_label_p1.next_to(v_line_p1, DOWN)
        self.add(v_line_p1,graph_dot_p1,x_label_p1)
        num1 = TexMobject(r"{\large \textcircled{\small 3}} ").set_color(BLACK).scale(0.5)
        num1.next_to(graph_dot_p1,UP,buff=0.4*SMALL_BUFF)
        self.add(v_line_p1,graph_dot_p1,x_label_p1,num1)

        input_tracker_p1 = ValueTracker(V4)
        v_line_p1 = get_v_line(input_tracker_p1,adiabatisch41_graph)
        graph_dot_p1 = Dot(color=BLACK)
        graph_dot_p1.move_to(get_graph_point(input_tracker_p1,adiabatisch41_graph))
        x_label_p1 = TexMobject("{ V }_{ 4 }")
        x_label_p1.next_to(v_line_p1, DOWN)
        num1 = TexMobject(r"{\large \textcircled{\small 4}} ").set_color(BLACK).scale(0.5)
        num1.next_to(graph_dot_p1,DOWN+LEFT,buff=-0.3*SMALL_BUFF)
        self.add(v_line_p1,graph_dot_p1,x_label_p1,num1)

from pathlib import Path

if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim    -s  -c 'WHITE' --video_dir ~/Downloads/ " + script)
