from manim import *
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, figsize=(16,3))




def get_image(image_name):
    img = ImageMobject(image_name).scale(1 )
    return img


def my_function(amplitude, omega, t, k, x):
    return amplitude * np.sin(omega * t - k * x)


def get_image_plot(amplitude, omega, t, k, x):
    plt.cla()
    plt.rcParams['figure.dpi'] = 200
    fig, ax = plt.subplots(1, figsize=(16,3))

    x=np.linspace(-50,150,10001)
    plt.xlim(-50, 150)

    tick_pos= [ 50*(i) for i in range(-1,4)]
    [plt.axhline(i, color= "Gray", alpha=0.4 ) for i in range(-2,3)]
    [plt.axvline(i, color= "Gray", alpha=0.4 ) for i in tick_pos]
    plt.axhline(0, color= "Black")
    plt.ylim(-3,3)
    ################
    plt.yticks(fontsize=20, alpha=0.6);
    plt.xticks(tick_pos , fontsize=20, alpha=0.6 );
    plt.annotate(r'x in [m]',
                 xy=(1, 0), xycoords='axes fraction',
                 xytext=(-20, 20), textcoords='offset pixels',
                 horizontalalignment='right',
                 verticalalignment='bottom',
                 fontsize=20);
    def g(x,t):
        interfering_waves=81
        k_all=np.linspace(0,0.5,interfering_waves)
        x_m, k_m = np.meshgrid(x,k_all)
        matrix= np.exp(-1j*(k_m*x_m - (k_m/(k_m**1.100+1))*t) )
        my_sum=np.sum(matrix,axis=0)
        return my_sum/interfering_waves
    plt.axhline(c="k")
    plt.axvline(c="k")
    plt.plot(x,np.real(3*g(x,t)), lw=2.5)
    plt.savefig("tmp.png",dpi=200)
    img = get_image("tmp.png").to_edge(UL).shift(LEFT)
    return img


class FinalDisp(Scene):
    def construct(self):
        x_values = np.linspace(0, 30, 400)

        amp1 = 0.0
        amp2 = 1
        tr_amplitude = ValueTracker(amp1)

        k1 = 1
        k2 = 1.3
        tr_k = ValueTracker(k1)

        t1 = 1
        t2 = 2
        tr_time = ValueTracker(t1)

        omega1 = 1
        omega2 = 2.5
        track_omega = ValueTracker(omega1)

        image = get_image_plot(amp1, omega1, t1, k1, x_values)
        self.add(image)

        def update_image(mob):
            new_mob = get_image_plot(
                tr_amplitude.get_value(),
                track_omega.get_value(),
                tr_time.get_value(),
                tr_k.get_value(),
                x_values
            )
            mob.become(new_mob)

        image.add_updater(update_image)

        #self.play(tr_amplitude.set_value, amp2)
        self.play(tr_time.set_value, 100, run_time=7, rate_func= linear)


from pathlib import Path

if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim   -p  -c 'WHITE' --video_dir ~/Downloads/ " + script)
