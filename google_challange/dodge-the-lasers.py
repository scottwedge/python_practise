def floor(x):
    sqrt_2 = long("41421356237309504880168872420969807856967187537694807317667973799073247846210703885038753432764157273501384623091229702492483605585073721264412149709993583141322266592750559275579995050115278206")
    ten_pow = long("100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
    rate = long((x*(x+1))/2)
    if x <= 10:
        for i in range(x):
            rate += long((sqrt_2*(i+1))/ten_pow)
        return rate
    last = long((sqrt_2 * x) / ten_pow)
    rate += (x * last) - long((last * (last + 1))/2) - \
        floor(last)
    return rate


def solution(str_n):
    return str(floor(long(str_n)))
