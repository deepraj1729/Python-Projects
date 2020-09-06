import math
import time

def Fx(x):
    # z = math.pow(x,3)-5*x-7
    z = x*math.exp(x)-3
    return z

def Regular_Falsi_Root(a,b,d_p,i=1,count=0):
    fa = Fx(a)
    fb = Fx(b)
    t = (a*fb - b*fa)/(fb - fa)
    print(" Step:{}: x({}) = {:0.5f} ,f(x{}) = {:0.5f} b = {:0.5f} ,  count = {}".format(i,i-1,a,i-1,fa,b,count))

    if fa <0:
        init_x = a
        a = t
        new_x = t
        if count == 2:
            print("\nLoop terminated, real root found = {}".format(round(new_x,d_p)))
            return 0 
        if round(init_x,d_p) == round(new_x,d_p):
            count=count+1  
        else:
            count =0    
        i=i+1    
        Regular_Falsi_Root(a,b,d_p,i,count)
    else:
        print("Something went wrong. Couldn't converge into a real root !!!")
        return 0

if __name__ == "__main__":
    print("------------- Welcome to Regular Falsi Approximation program  --------------\n")
    low_lt = float(input("Enter Lower limit of the root (Xo): "))
    up_lt = float(input("Enter Upper limit of the root (b): "))
    d_p = int(input("Enter the no. of Decimal places for approximation: "))
    print("----------------------------------------------------------------------------")
    start_time = time.time()
    Regular_Falsi_Root(low_lt,up_lt,d_p)
    print("----------------------------------------------------------------------------")
    print("\n--- Execution time: {} seconds ---\n".format(time.time() - start_time))
    print("----------------------------------------------------------------------------")