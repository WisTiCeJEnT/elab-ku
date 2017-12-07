def fah_to_cel(start, end, step): # version ne
    print(f"{'Fahrenheit':>12}{'Celcius':>12}")
    print(f"{'----------':>12}{'-------':>12}")
    fah = start
    while (start>end and fah>end) or (start<end and fah<end):
        if (start>=end and step>=0) or (start<=end and step<=0):
            break
        cel = (5/9)*(fah-32)
        print(f"{fah:12.2f}{cel:12.2f}")
        fah = fah + step
    print(f"{'----------':>12}{'-------':>12}")
