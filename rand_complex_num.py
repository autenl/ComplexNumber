import random
from ComplexNumber import ComplexNumber


def rand_complex_num(real_lb, real_ub, im_lb, im_ub, amount=1):
    if amount == 1:
        random_real = random.uniform(real_lb, real_ub)
        random_im = random.uniform(im_lb, im_ub)

        return ComplexNumber(random_real, random_im)
    else:
        rand_list = []
        for i in range(0, amount):
            random_real = random.uniform(real_lb, real_ub)
            random_im = random.uniform(im_lb, im_ub)

            rand_list.append(ComplexNumber(random_real, random_im))

        return rand_list
