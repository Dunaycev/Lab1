import control.matlab as ctr
import matplotlib.pyplot as plt
from array import*


def funс(w1,w2):
    #q = np.linspace(1, 2, 3000)
    #пытался изменить шаг дискретизации, чтобы переходная характеристика безынерционного звена правильна строилась
    y1,x1=ctr.step(w1)
    y2,x2 = ctr.step(w2)
    k1=(y1[2]-y1[1])/(x1[2]-x1[1]) #коэффициент наклона касательной
    t1=y1[0]
    Y1 = [(k1 * x1[i]+t1) for i in range(len(x1))] #массив с координатами касательной по у
    X1=x1                                    #массив с координатами касательной по х

    k2 = (y2[2] - y2[1]) / (x2[2] - x2[1])  # коэффициент наклона касательной
    t2 = y2[0]
    Y2 = [(k2 * x2[i] + t2) for i in range(len(x2))]  # массив с координатами касательной по у
    X2 = x2  # массив с координатами касательной по х

    fig, (ax1, ax2) = plt.subplots(
        nrows=1, ncols=2,
        figsize=(10, 4)
    )

    ax1.plot(x1, y1)  #переходная функция
    ax1.plot(x1, y2)  #график х2
    ax1.plot(x1, Y1)  # касательная
    ax1.plot(x1, Y2)  # касательная
    ax1.set_title('$Переходная$ $функция$ $и$ $касательная$')
    ax1.set_ylabel('Амплитуда')
    ax1.set_xlabel('Время (сек.)')

    y11, x11 = ctr.impulse(w1)
    y21, x21 = ctr.impulse(w2)

    ax2.plot(x11, y11)  #импульсная функция
    ax2.plot(x21, y21)  # график х2
    ax2.set_title('$Импульсная$ $функция$')
    ax2.set_ylabel('Амплитуда')
    ax2.set_xlabel('Время (сек.)')

    ax1.grid(True)
    ax2.grid(True)

    plt.show()
    mag, phase, omega = ctr.bode(w1, dB=False)
    mag, phase, omega = ctr.bode(w2, dB=False)
    plt.show()

for j in range(5):
    #безынерционное звено
    if j==0:
        a = ctr.tf([1.], [0.00000000001, 1.])
        b = ctr.tf([2.], [0.00000000001, 1.])
        funс(a, b)
    #апериодическое звено
    if j==1:
        a = ctr.tf([5.], [4., 1.])
        b = ctr.tf([10.], [8., 1.])
        funс(a, b)
    #интегрируещее звено
    if j==2:
        a = ctr.tf([1.], [1., 0.])
        b = ctr.tf([1.], [2., 0.])
        funс(a, b)
    #идиальное диф. звено
    if j == 3:
        a = ctr.tf([4.,0.], [0.00000000001, 1.])
        b = ctr.tf([8.,0.], [0.00000000001, 1.])
        funс(a, b)
    #реальное диф. звено
    if j == 4:
        a = ctr.tf([3.,0.], [1., 1.])
        b = ctr.tf([6.,0.], [2., 1.])
        funс(a, b)
