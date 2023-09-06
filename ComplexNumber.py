import math
import matplotlib.pyplot as plt


class ComplexNumber:
    def __init__(self, real_part, im_part):
        self.real_part = real_part
        self.im_part = im_part

    def __add__(self, other):
        real_sum = self.real_part + other.real_part
        imaginary_sum = self.im_part + other.im_part

        return ComplexNumber(real_sum, imaginary_sum)

    def __sub__(self, other):
        real_diff = self.real_part - other.real_part
        imaginary_diff = self.im_part - other.im_part

        return ComplexNumber(real_diff, imaginary_diff)

    def __mul__(self, other):
        real_component = self.real_part * other.real_part - self.im_part * other.im_part
        im_component = self.real_part * other.im_part + self.im_part * other.real_part

        return ComplexNumber(real_component, im_component)

    def __truediv__(self, other):
        factor = 1 / (other.modulus() ** 2)
        real_component = self.real_part * other.real_part + self.im_part * other.im_part
        im_component = -self.real_part * other.im_part + self.im_part * other.real_part

        return ComplexNumber(factor * real_component, factor * im_component)

    def __pow__(self, power):
        if (self.real_part < 0) and (self.im_part == 0):
            return ComplexNumber(self.real_part ** power, 0)
        else:
            mod_factor = self.modulus() ** power
            return ComplexNumber(mod_factor * math.cos(power * self.arg()), mod_factor * math.sin(power * self.arg()))

    def modulus(self):
        return math.sqrt(self.real_part ** 2 + self.im_part ** 2)

    def arg(self):
        if self.real_part == 0:
            if self.im_part > 0:
                return math.pi / 2
            elif self.im_part < 0:
                return -math.pi / 2
            else:
                return 0

        theta = math.atan(self.im_part / self.real_part)

        if self.real_part < 0:
            if self.im_part > 0:
                return math.pi - theta
            else:
                return math.pi + theta
        else:
            return theta

    def print_num(self):
        if self.real_part == 0 and self.im_part == 0:
            print(0)
        elif self.real_part == 0 and self.im_part != 0:
            print(f"{self.im_part:.3f}i")
        elif self.real_part != 0 and self.im_part == 0:
            print(f"{self.real_part:.3f}")
        elif self.im_part < 0:
            print(f"{self.real_part:.3f} - {abs(self.im_part):.3f}i")
        else:
            print(f"{self.real_part:.3f} + {self.im_part:.3f}i")

    def graph_point(self, labeled=False, color_choice='k'):
        plt.scatter(self.real_part, self.im_part, color=color_choice, marker='o')

        if labeled:
            if self.real_part == 0 and self.im_part == 0:
                label = "0"
            elif self.real_part == 0 and self.im_part != 0:
                label = f"{self.im_part:.2f}i"
            elif self.real_part != 0 and self.im_part == 0:
                label = f"{self.real_part:.2f}"
            elif self.im_part < 0:
                label = f"{self.real_part:.2f} - {abs(self.im_part):.2f}i"
            else:
                label = f"{self.real_part:.2f} + {self.im_part:.2f}i"
            plt.annotate(label, (self.real_part, self.im_part), xytext=(5, 5), textcoords="offset pixels")

    # UNDER CONSTRUCTION
    def graph_vector(self, color_choice="k", origin=(0, 0)):
        fig, ax = plt.subplots()
        ax.quiver(origin[0], origin[1], self.real_part, self.im_part, color=color_choice)


