import math
import time

def Fx(m):
    #z = math.pow(m,3)-m-1
    # z = m*(math.tan(m))-1.28    
    # z = 10*(math.log10(m))-m*m+3   
    z = m*m*m -9*m +1 
    #z = math.pow(m,4)-m-10    
    #z = 3*math.pow(m,3)+5*m-40    

    return z


def Bolzano_Bisection_Root(a,b,d_p,i=1,count=1):
    c = (a+b)/2
    f = Fx(c)
    print("Step {}: a = {:0.5f} , b = {:0.5f} , bisection(c) = {} f(c) = {:0.4f}, count = {}".format(i,a,b,c,f,count))
    
    if f <0:
        init_c = c
        a=c
        new_c = (a+b)/2
        if count == 3:
            print("\nLoop terminated, real root found = {}".format(round(new_c,d_p)))
            return 0 
        if round(init_c,d_p) == round(new_c,d_p):
            count=count+1  
        else:
            count =1    
        i+=1    
        Bolzano_Bisection_Root(a,b,d_p,i,count)
    else:
        init_c = c
        b=c
        new_c = (a+b)/2
        if count == 3:
            print("\nLoop terminated, real root found = {}".format(round(new_c,d_p))) 
            return 0  
        if round(init_c,d_p) == round(new_c,d_p):
            count=count+1
        else:
            count =1    
        i+=1 
        Bolzano_Bisection_Root(a,b,d_p,i,count)      


if __name__ == "__main__":
    print("-------------  Welcome to Bolzano's Bisection Root Program --------------\n")
    low_lt = float(input("Enter Lower limit of the root (a): "))
    up_lt = float(input("Enter Upper limit of the root (b): "))
    d_p = int(input("Enter the no. of Decimal places for approximation: "))
    print("----------------------------------------------------------------------------")
    start_time = time.time()
    Bolzano_Bisection_Root(low_lt,up_lt,d_p)
    print("----------------------------------------------------------------------------")
    print("\n--- Execution time: {} seconds ---\n".format(time.time() - start_time))
    print("----------------------------------------------------------------------------")