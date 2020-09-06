#include<stdio.h>
#include<math.h>
#include<time.h>

float Fx(float x) 
{
    float z = x*exp(x)-3 ;  // Define the function here (change it for different equations/questions)
    // x0 = 1, b=2, d_p = 4  ans: app_root = 1.0499
    return z;
}

double Round(double val,int d_p) // Rounding numbers to given decimal places
{
    double nearest = roundf(val * pow(10,d_p)) / pow(10,d_p);
    return nearest;
}

int Regular_Falsi_Root(double a, double b,int d_p,int i,int count) // Regular Falsi Root approximation function
{
    double init_x,new_x;
    double fa = Fx(a);
    double fb = Fx(b);
    double t = (a*fb - b*fa)/(fb - fa);
    printf("\nStep %d: x(%d) = %0.5lf ,f(x%d) = %0.5lf , b = %0.5lf , count = %d",i,i-1,a,i-1,fa,b,count);

    if(fa <0)
    {
        init_x = a;
        a = t;
        new_x = t;
        if(count == 3)
        {
            printf("\n\nLoop terminated, real root found = %.*lf\n",d_p,new_x);
            return 0 ;
        }    
        if(Round(init_x,d_p) == Round(new_x,d_p))
            count++;
        else
            count =1;    
        i++;   
        Regular_Falsi_Root(a,b,d_p,i,count);
    }    
    else
    {
        printf("\nSomething went wrong. Couldn't converge into a real root !!!\n");
        return 0;
    }    
}    

int main()  // Main function begins
{
    double x,b;
    int d_p;
    printf("\n------------- Welcome to Regular Falsi Approximation program  --------------\n");
    printf("\n1.Enter the Lower limit (Xo) of the root: ");
    scanf("%lf",&x);
    printf("\n2.Enter the Upper limit (b) of the root: ");
    scanf("%lf",&b);
    printf("\n3.Enter the no of decimal places to be considered: ");
    scanf("%d",&d_p);
    printf("\n----------------------------------------------------------------------------");

    clock_t begin = clock(); // CPU Time count starts (for getting the CPU time of execution of the recursive function)

    Regular_Falsi_Root(x,b,d_p,1,1); // Bolzano_Bisection_Root(...,1,1) initially set i=1 and count=1 

    //---------------------------------     Program ends when count = 3  --------------------------------------------//

    clock_t end = clock(); // CPU Time count ends
    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC; // The difference in time is the execution time in sec
    printf("\n----------------------------------------------------------------------------");
    printf("\nExecution time: %lf",time_spent);
    printf("\n----------------------------------------------------------------------------");
    return 0;
}