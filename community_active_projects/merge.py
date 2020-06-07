from manim import *


class CarnotProcess(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 6,
        "x_axis_width": 9,
        "x_axis_label": "$V$",
        "x_tick_frequency": 1,
        "x_labeled_nums" :range(0,3,1),


        "y_min": 0,
        "y_max": 50,
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

        isotherm12_graph = self.get_graph(lambda x : p_isotherm(x, Tmax)*0.01, x_min=V1, x_max=V2 ,color = RED)
        adiabatisch23_graph = self.get_graph(lambda x : p_adiabatisch(x, p2,V2)*0.01, x_min=V2, x_max=V3 ,color = RED)
        isotherm34_graph = self.get_graph(lambda x : p_isotherm(x, Tmin)*0.01, x_min=V3, x_max=V4 ,color = RED)
        adiabatisch41_graph = self.get_graph(lambda x : p_adiabatisch(x, p4,V4)*0.01, x_min=V4, x_max=V1 ,color = RED)


        self.add(isotherm12_graph,adiabatisch23_graph,isotherm34_graph,adiabatisch41_graph)
        self.wait(0.1)




from pathlib import Path

if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim   -p -s  -c 'BLACK' --video_dir ~/Downloads/ " + script)
