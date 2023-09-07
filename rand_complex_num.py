import random
from ComplexNumber import ComplexNumber


def rand_complex_num(real_lb, real_ub, im_lb, im_ub, amount=1):
    random_reals = random.sample(range(real_lb, real_ub + 1), amount)
    random_ims = random.sample(range(im_lb, im_ub + 1), amount)

    if amount == 1:
        return ComplexNumber(random_reals[0], random_ims[0])
    else:
        return [ComplexNumber(random_reals[i], random_ims[i]) for i in range(0, amount - 1)]
