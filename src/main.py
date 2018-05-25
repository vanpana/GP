from src.Controller import Controller
import matplotlib.pyplot as plt

if __name__ == '__main__':
    chromosome_number = 200
    gen_number = 30

    ctrl = Controller(chromosome_number, gen_number, "../data/data_100.csv")

    ctrl.run()

    plt.plot(range(0, gen_number), ctrl.averages)
    plt.axis([0, gen_number, min(ctrl.averages), max(ctrl.averages)])
    plt.show()
