from manim import *


class CarnotProcess(GraphScene):
    CONFIG = {

        "x_min": 0.5,
        "x_max": 4,
        "x_axis_width": 9,
        "x_axis_label": "$V$",
        "x_tick_frequency": 3.5,
       # "x_labeled_nums" :range(0,3,1),


        "y_min": 0,
        "y_max": 40,
        "y_tick_frequency": 40,
        "y_axis_label": "$P$",
       # "y_labeled_nums" :range(0,26,2),

        "graph_origin": 3 * DOWN + 6.5 * LEFT,
        "function_color": RED,
        "axes_color": GREY,

        "x_label_direction": RIGHT,
        "y_label_direction": LEFT,
    }

    def construct(self):
        R = 8.314

        self.setup_axes(animate=False)
        self.x_axis_label_mob.shift(0.5*LEFT*abs(self.y_axis[0].points[0]-self.x_axis[0].points[0]))
        # self.ti.shift(LEFT*abs(self.y_axis[0].points[0]-self.x_axis[0].points[0]))
        self.x_axis.shift(LEFT*abs(self.y_axis[0].points[0]-self.x_axis[0].points[0]))
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
        isotherm12_graph_over_Text = TexMobject(r" \text{T}_{\text{max}}").scale(0.7).next_to(isotherm12_graph_over,RIGHT,aligned_edge=DOWN, buff=0)
        self.add(isotherm12_graph_over,isotherm12_graph_over_Text)

        isotherm34_graph_over = self.get_graph(lambda x : p_isotherm(x, Tmin)*0.01, x_min=V3+0.3, x_max=V4-0.5 ,color = BLUE, stroke_opacity=0.5)
        isotherm34_graph_over_Text = TexMobject(r"\text{T}_{\text{min}}").scale(0.7).next_to(isotherm34_graph_over,RIGHT,aligned_edge=DOWN, buff=0)
        self.add(isotherm34_graph_over,isotherm34_graph_over_Text)

        upper_graph= self.get_graph(lambda x : p_isotherm(x, Tmax)*0.01  if x < V2 else p_adiabatisch(x, p2,V2)*0.01)
        lower_graph = self.get_graph(lambda x :p_adiabatisch(x, p4,V4)*0.01 if x < V4 else p_isotherm(x, Tmin)*0.01)
        area_in_bewtween = self.get_area(upper_graph,V1,V3,bounded=lower_graph,dx_scaling=0.2)
        self.add(area_in_bewtween)
        upper_graph.get_function()
        def work_out(x):
            return p_isotherm(x, Tmax)  if x < V2 else p_adiabatisch(x, p2,V2)
        def work_in(x):
            return p_adiabatisch(x, p4,V4) if x < V4 else p_isotherm(x, Tmin)

        from scipy.integrate import quad

        oben = quad(work_out, V1, V3)[0]
        print(f"Arbeit raus {oben=:.2f}")
        unten = quad(work_in, V3, V1)[0]
        print(f"Arbeit rein {unten=:.2f}")


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
        num1 = TexMobject(r"{\large \textcircled{\small 1}} ").set_color(BLACK).scale(0.7)
        num1.next_to(graph_dot_p1,RIGHT,buff=0.4*SMALL_BUFF)
        self.add(v_line_p1,graph_dot_p1,x_label_p1,num1)

        input_tracker_p1 = ValueTracker(V2)
        v_line_p1 = get_v_line(input_tracker_p1,adiabatisch23_graph)
        graph_dot_p1 = Dot(color=BLACK)
        graph_dot_p1.move_to(get_graph_point(input_tracker_p1,adiabatisch23_graph))
        x_label_p1 = TexMobject("{ V }_{ 2 }")
        x_label_p1.next_to(v_line_p1, DOWN)
        num1 = TexMobject(r"{\large \textcircled{\small 2}} ").set_color(BLACK).scale(0.7)
        num1.next_to(graph_dot_p1,UP,buff=0.4*SMALL_BUFF)
        self.add(v_line_p1,graph_dot_p1,x_label_p1,num1)

        input_tracker_p1 = ValueTracker(V3)
        v_line_p1 = get_v_line(input_tracker_p1,isotherm34_graph)
        graph_dot_p1 = Dot(color=BLACK)
        graph_dot_p1.move_to(get_graph_point(input_tracker_p1,isotherm34_graph))
        x_label_p1 = TexMobject("{ V }_{ 3 }")
        x_label_p1.next_to(v_line_p1, DOWN)
        self.add(v_line_p1,graph_dot_p1,x_label_p1)
        num1 = TexMobject(r"{\large \textcircled{\small 3}} ").set_color(BLACK).scale(0.7)
        num1.next_to(graph_dot_p1,UP,buff=0.4*SMALL_BUFF)
        self.add(v_line_p1,graph_dot_p1,x_label_p1,num1)

        input_tracker_p1 = ValueTracker(V4)
        v_line_p1 = get_v_line(input_tracker_p1,adiabatisch41_graph)
        graph_dot_p1 = Dot(color=BLACK)
        graph_dot_p1.move_to(get_graph_point(input_tracker_p1,adiabatisch41_graph))
        x_label_p1 = TexMobject("{ V }_{ 4 }")
        x_label_p1.next_to(v_line_p1, DOWN)
        num1 = TexMobject(r"{\large \textcircled{\small 4}} ").set_color(BLACK).scale(0.7)
        num1.next_to(graph_dot_p1,DOWN+LEFT,buff=-0.3*SMALL_BUFF)
        self.add(v_line_p1,graph_dot_p1,x_label_p1,num1)

        #annotation:
        ddd= TexMobject(r"\Delta W").next_to(graph_dot_p1, UP).scale(0.7)
        bg= ddd.add_background_rectangle(color= WHITE)
        self.add(ddd)

        input_tracker_Q= ValueTracker(V1+(V2-V1)/2)
        graph_dot_p1 = Dot(color=BLACK)
        graph_dot_p1.move_to(get_graph_point(input_tracker_Q,isotherm12_graph))
        #self.add(graph_dot_p1)
        aa= Arrow(graph_dot_p1.get_center()+UR*0.5, graph_dot_p1.get_center(),buff=0).set_color(BLACK)
        self.add(aa)
        ddd= TexMobject(r"\Delta Q_a").scale(0.7)
        self.add(ddd.next_to(graph_dot_p1.get_center()+UR*0.5,UP,buff=0))

        input_tracker_Q2= ValueTracker(V3+(V4-V3)/2)
        graph_dot_p1 = Dot(color=BLACK)
        graph_dot_p1.move_to(get_graph_point(input_tracker_Q2,isotherm34_graph))
        #self.add(graph_dot_p1)
        aa= Arrow(graph_dot_p1.get_center(), graph_dot_p1.get_center()+DL*0.5,buff=0).set_color(BLACK)
        self.add(aa)
        ddd= TexMobject(r"\Delta Q_{ab}").scale(0.7)
        self.add(ddd.next_to(graph_dot_p1.get_center()+DL*0.5,DOWN,buff=0.05))


        def make_box():
            p1 = [0,1,0]
            p2 = [0,0,0]
            p3= [0.75,0,0]
            p4 = [0.75,1,0]
            l1 = Line(p1,p2).set_color(BLACK)
            l2 = Line(p2,p3).set_color(BLACK)
            l3 = Line(p3,p4).set_color(BLACK)
            obj = VGroup(l1,l2,l3)
            return obj
        def make_box_high():
            p1 = [0,4,0]
            p2 = [0,0,0]
            p3= [0.75,0,0]
            p4 = [0.75,4,0]
            l1 = Line(p1,p2).set_color(BLACK)
            l2 = Line(p2,p3).set_color(BLACK)
            l3 = Line(p3,p4).set_color(BLACK)
            obj = VGroup(l1,l2,l3)
            return obj
        DISTANCELEFTRIGHT= 0.8
        cold = make_box().shift(DOWN+DISTANCELEFTRIGHT*LEFT)
        cold.add_background_rectangle(color=BLUE)
        cold.text = TexMobject(r" \text{T}_{\text{min}}").scale(0.6).set_color(BLACK)
        cold.text.move_to(cold.get_center())
        hot = make_box().shift(DOWN+DISTANCELEFTRIGHT*RIGHT)
        hot.text = TexMobject(r" \text{T}_{\text{max}}").scale(0.6).set_color(BLACK)
        hot.text.move_to(hot.get_center())

        hot.add_background_rectangle(color= RED)
        obj = make_box_high()
        baths= VGroup(obj,cold, hot, cold.text, hot.text).to_edge(UR).shift(2*DOWN+LEFT*DISTANCELEFTRIGHT)
        self.add(baths)
        baths_hotcold = VGroup(cold, hot, cold.text, hot.text)
        #self.play(baths_hotcold.shift, LEFT*DISTANCELEFTRIGHT)
        #self.add(baths_hotcold.copy().shift(RIGHT*DISTANCELEFTRIGHT*2))
        #self.wait()
        path_weight = Path().home()/"Documents/manim_resources/weight.svg"
        weight_light = SVGMobject(str(path_weight)).set_stroke(width=0).scale(0.4)
        weight_light.set_color(interpolate_color(GREY,WHITE,0.2))
        weight_light.scale(0.829)
        weight_heavy = SVGMobject(str(path_weight)).set_stroke(width=0).scale(0.4)
        weight_heavy.set_color(interpolate_color(GREY,BLACK,0.2))

        weight_light.set_z_index(2)
        weight_heavy.set_z_index(2)
        stamp_thickness  = 0.1
        def make_stemp():
            stemp  = Rectangle()
            p1 = [0,stamp_thickness,0]
            p2 = [0,0,0]
            p3= [0.75,0,0]
            p4 = [0.75,stamp_thickness,0]
            lines = []
            lines.append(Line(p2,p3).set_color(BLACK))
            lines.append(Line(p4,p1).set_color(BLACK))
            lines.append(Line(p1,p2).set_color(BLACK).shift(RIGHT*0.1*0.75))
            lines.append(Line(p1,p2).set_color(BLACK).shift(RIGHT*0.2*0.75))
            lines.append(Line(p1,p2).set_color(BLACK).shift(RIGHT*0.3*0.75))
            lines.append(Line(p1,p2).set_color(BLACK).shift(RIGHT*0.4*0.75))
            lines.append(Line(p1,p2).set_color(BLACK).shift(RIGHT*0.5*0.75))
            lines.append(Line(p1,p2).set_color(BLACK).shift(RIGHT*0.6*0.75))
            lines.append(Line(p1,p2).set_color(BLACK).shift(RIGHT*0.7*0.75))
            lines.append(Line(p1,p2).set_color(BLACK).shift(RIGHT*0.8*0.75))
            lines.append(Line(p1,p2).set_color(BLACK).shift(RIGHT*0.9*0.75))
            obj = VGroup(*lines)
            return obj
        stemp= make_stemp()
        stemp.set_x(obj.get_center()[0])
        center= obj.get_center()
        dot_1 = Dot(center).shift(DOWN*0.2).set_color(BLUE_A)
        dot_2 = Dot(point=[center[0],((V2-V1) /(V3-V1)) *2+dot_1.get_y() ,0])
        dot_3 = Dot(point=[center[0],((V3-V1) /(V3-V1)) *2+dot_1.get_y() ,0])
        dot_4 = Dot(point=[center[0],((V4-V1) /(V3-V1)) *2+dot_1.get_y() ,0])


        line_1 = Line(dot_1.copy().shift(RIGHT*(0.75/2-0.01)).get_center(), dot_1.copy().shift(RIGHT*(0.75/2+0.01)).get_center()).set_color(GREEN).set_opacity(1).set_z_index(1)
        line_2 = Line(dot_2.copy().shift(RIGHT*(0.75/2-0.01)).get_center(), dot_2.copy().shift(RIGHT*(0.75/2+0.01)).get_center()).set_color(GREEN).set_opacity(1).set_z_index(1)
        line_3 = Line(dot_3.copy().shift(RIGHT*(0.75/2-0.01)).get_center(), dot_3.copy().shift(RIGHT*(0.75/2+0.01)).get_center()).set_color(GREEN).set_opacity(1).set_z_index(1)
        line_4 = Line(dot_4.copy().shift(RIGHT*(0.75/2-0.01)).get_center(), dot_4.copy().shift(RIGHT*(0.75/2+0.01)).get_center()).set_color(GREEN).set_opacity(1).set_z_index(1)
        self.add(line_1,line_2,line_3,line_4)
        line_1b = Line(dot_1.copy().shift(LEFT*(0.75/2-0.01)).get_center(), dot_1.copy().shift(LEFT*(0.75/2+0.01)).get_center()).set_color(GREEN).set_opacity(1).set_z_index(1)
        line_2b = Line(dot_2.copy().shift(LEFT*(0.75/2-0.01)).get_center(), dot_2.copy().shift(LEFT*(0.75/2+0.01)).get_center()).set_color(GREEN).set_opacity(1).set_z_index(1)
        line_3b = Line(dot_3.copy().shift(LEFT*(0.75/2-0.01)).get_center(), dot_3.copy().shift(LEFT*(0.75/2+0.01)).get_center()).set_color(GREEN).set_opacity(1).set_z_index(1)
        line_4b = Line(dot_4.copy().shift(LEFT*(0.75/2-0.01)).get_center(), dot_4.copy().shift(LEFT*(0.75/2+0.01)).get_center()).set_color(GREEN).set_opacity(1).set_z_index(1)
        self.add(line_1b,line_2b,line_3b,line_4b)


        plat1A = Dot(dot_1.get_center()+UP*stamp_thickness+LEFT).set_color(LIGHT_BROWN).set_opacity(0.4)
        lin_plat1A  = Line(plat1A.copy().shift(LEFT*0.4),plat1A.copy().shift(RIGHT*0.4)).set_color(LIGHT_BROWN).set_opacity(0.4)
        plat1B = Dot(dot_1.get_center()+UP*stamp_thickness+RIGHT).set_color(LIGHT_BROWN).set_opacity(0.4)
        lin_plat1B  = Line(plat1B.copy().shift(LEFT*0.4),plat1B.copy().shift(RIGHT*0.4)).set_color(LIGHT_BROWN).set_opacity(0.4)

        plat2A = Dot(dot_3.get_center()+UP*stamp_thickness+LEFT).set_color(LIGHT_BROWN).set_opacity(0.4)
        plat2A_later= plat2A.copy()
        lin_plat2A  = Line(plat2A.copy().shift(LEFT*0.4),plat2A.copy().shift(RIGHT*0.4)).set_color(LIGHT_BROWN).set_opacity(0.4)
        plat2B = Dot(dot_3.get_center()+UP*stamp_thickness+RIGHT).set_color(LIGHT_BROWN).set_opacity(0.4)
        lin_plat2B  = Line(plat2B.copy().shift(LEFT*0.4),plat2B.copy().shift(RIGHT*0.4)).set_color(LIGHT_BROWN).set_opacity(0.4)

        val_tracker= ValueTracker(V1)

        self.add(lin_plat1A,lin_plat1B,lin_plat2A,lin_plat2B)
        self.add(weight_heavy,weight_light)

        weight_heavy.move_to(plat1A.get_center(),aligned_edge=DOWN)
        height_of_weight_heavy =  weight_heavy.get_center()[1]-plat1A.get_center()[1]
        weight_light.move_to(plat2A.get_center(),aligned_edge=DOWN)
        height_of_weight_light = weight_light.get_center()[1]-plat2A.get_center()[1]
        def update_y_coordinate_of_stemp(mob):
            mob.set_y((val_tracker.get_value()-V1) /(V3-V1) *2 +dot_1.get_y()+stamp_thickness/2)
            return mob
        def update_y_coordinate_of_weight_heavy(mob):
            mob.set_y((val_tracker.get_value()-V1) /(V3-V1) *2 +dot_1.get_y()+stamp_thickness+height_of_weight_heavy)
            return mob
        def update_y_coordinate_of_weight_light(mob):
            mob.set_y((val_tracker.get_value()-V1) /(V3-V1) *2 +dot_1.get_y()+stamp_thickness+height_of_weight_light)

        stemp.add_updater(update_y_coordinate_of_stemp)
        self.add(stemp)

        baths_hotcold.shift(LEFT*DISTANCELEFTRIGHT)

        square= Rectangle(fill_opacity=1).set_stroke(width=0).set_color(RED)
        square.set_width(0.75)
        square.set_z_index(-1)
        square.set_x(center[0])
        square.set_height((stemp.get_center()-obj.get_bottom())[1]-stamp_thickness/2,stretch=True)
        square.align_to(obj,DOWN)

        def update_gas_square(square):
            square.set_height((stemp.get_center()-obj.get_bottom())[1]-stamp_thickness/2,stretch=True)
            square.align_to(obj,DOWN)
            return square
        num_colors= 1000
        cols =  color_gradient([RED,WHITE,BLUE], num_colors)
        def update_gas_square_turn_blue(square):
            square.set_height((stemp.get_center()-obj.get_bottom())[1]-stamp_thickness/2,stretch=True)
            square.align_to(obj,DOWN)
            integ = int((val_tracker.get_value()-V2)/(V3-V2)*(num_colors-1))
            square.set_color(cols[integ])
            return square
        def update_gas_square_turn_red(square):
            square.set_height((stemp.get_center()-obj.get_bottom())[1]-stamp_thickness/2,stretch=True)
            square.align_to(obj,DOWN)
            integ = int((val_tracker.get_value()-V1)/(V4-V1)*(num_colors-1))
            square.set_color(cols[integ])
            return square

        self.add(square)

        #### START
        sourunding_dot = Dot().scale(1.3).set_fill(color=BLACK).set_z_index(-1)
        innerdot = Dot().set_color(WHITE).scale(1)
        moving_dot= VGroup(sourunding_dot,innerdot)
        moving_dot.move_to(get_graph_point(val_tracker,isotherm12_graph))
        self.add(moving_dot)

        #1-2
        self.wait()
        square.add_updater(update_gas_square)
        self.play(weight_heavy.shift, RIGHT)
        weight_heavy.add_updater(update_y_coordinate_of_weight_heavy)
        moving_dot.add_updater(lambda x: x.move_to(get_graph_point(val_tracker,isotherm12_graph)))
        self.play(val_tracker.set_value, V2, rate_func= linear, run_time=2)
        self.play(baths_hotcold.shift, RIGHT*DISTANCELEFTRIGHT)
        #2-3
        moving_dot.add_updater(lambda x: x.move_to(get_graph_point(val_tracker,adiabatisch23_graph)))
        square.add_updater(update_gas_square_turn_blue)
        self.play(val_tracker.set_value, V3,  rate_func= linear, run_time=2)
        weight_heavy.remove_updater(update_y_coordinate_of_weight_heavy)
        self.play(weight_heavy.shift, RIGHT)
        self.play(baths_hotcold.shift, RIGHT*DISTANCELEFTRIGHT)
        self.play(weight_light.shift, RIGHT)
        weight_light.add_updater(update_y_coordinate_of_weight_light)
        square.remove_updater(update_gas_square_turn_blue)

        #3-4
        moving_dot.add_updater(lambda x: x.move_to(get_graph_point(val_tracker,isotherm34_graph_over)))
        self.play(val_tracker.set_value, V4,  rate_func= linear, run_time=2)
        self.play(baths_hotcold.shift, LEFT*DISTANCELEFTRIGHT)

        #4-1
        moving_dot.add_updater(lambda x: x.move_to(get_graph_point(val_tracker,adiabatisch41_graph)))
        square.add_updater(update_gas_square_turn_red)
        self.play(val_tracker.set_value, V1,  rate_func= linear, run_time=2)
        self.play(weight_light.shift, RIGHT)
        weight_light.remove_updater(update_y_coordinate_of_weight_light)
        self.play(baths_hotcold.shift, LEFT*DISTANCELEFTRIGHT)
        square.remove_updater(update_gas_square_turn_red)
        self.wait()

        ## new circle
        wl1 = weight_light.deepcopy()
        wh1 = weight_heavy.deepcopy()

        self.remove(weight_light)
        self.remove(weight_heavy)
        self.add(wl1,wh1)
        weight_light = SVGMobject(str(path_weight)).set_stroke(width=0).scale(0.4)
        weight_light.set_color(interpolate_color(GREY,WHITE,0.2))
        weight_light.scale(0.829)
        weight_heavy = SVGMobject(str(path_weight)).set_stroke(width=0).scale(0.4)
        weight_heavy.set_color(interpolate_color(GREY,BLACK,0.2))
        weight_heavy.move_to(plat1A.get_center(), aligned_edge=DOWN).set_z_index(2)
        weight_light.move_to(plat2A.get_center(), aligned_edge=DOWN).set_z_index(2)
        self.play(FadeIn(weight_light),FadeIn(weight_heavy))
        self.play(VGroup(wl1,wh1).shift,RIGHT)

        #1-2 second cicle
        square.add_updater(update_gas_square)
        self.play(weight_heavy.shift, RIGHT)
        weight_heavy.add_updater(update_y_coordinate_of_weight_heavy)
        moving_dot.add_updater(lambda x: x.move_to(get_graph_point(val_tracker,isotherm12_graph)))
        self.play(val_tracker.set_value, V2, rate_func= linear, run_time=2)
        self.play(baths_hotcold.shift, RIGHT*DISTANCELEFTRIGHT)
        #2-3
        moving_dot.add_updater(lambda x: x.move_to(get_graph_point(val_tracker,adiabatisch23_graph)))
        square.add_updater(update_gas_square_turn_blue)
        self.play(val_tracker.set_value, V3,  rate_func= linear, run_time=2)
        weight_heavy.remove_updater(update_y_coordinate_of_weight_heavy)
        self.play(weight_heavy.shift, RIGHT)
        self.play(baths_hotcold.shift, RIGHT*DISTANCELEFTRIGHT)
        self.play(weight_light.shift, RIGHT)
        weight_light.add_updater(update_y_coordinate_of_weight_light)
        square.remove_updater(update_gas_square_turn_blue)

        #3-4
        moving_dot.add_updater(lambda x: x.move_to(get_graph_point(val_tracker,isotherm34_graph_over)))
        self.play(val_tracker.set_value, V4,  rate_func= linear, run_time=2)
        self.play(baths_hotcold.shift, LEFT*DISTANCELEFTRIGHT)

        #4-1
        moving_dot.add_updater(lambda x: x.move_to(get_graph_point(val_tracker,adiabatisch41_graph)))
        square.add_updater(update_gas_square_turn_red)
        self.play(val_tracker.set_value, V1,  rate_func= linear, run_time=2)
        self.play(weight_light.shift, RIGHT)
        self.play(baths_hotcold.shift, LEFT*DISTANCELEFTRIGHT)
        self.wait()
from pathlib import Path

if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim   -p  -s  -c 'WHITE' --video_dir ~/Downloads/ " + script)
