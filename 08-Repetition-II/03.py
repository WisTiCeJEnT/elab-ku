def fah_to_cel(start, end, step): # version 2
    print(f"{'Fahrenheit':>12}{'Celcius':>12}")
    print(f"{'----------':>12}{'-------':>12}")
    for fah in range(start,end,step):
        cel = (5/9)*(fah-32)
        print(f"{fah:12.2f}{cel:12.2f}")
    print(f"{'----------':>12}{'-------':>12}")
