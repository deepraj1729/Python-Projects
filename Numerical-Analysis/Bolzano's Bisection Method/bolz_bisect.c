#include<stdio.h>
#include<math.h>
#include<time.h>

float Fx(float x) 
{
    float z = x*x*x -9*x +1 ;  // Define the function here (change it for different equations/questions)
    return z;
}

double Round(double val,int d_p) // Rounding numbers to given decimal places
{
    double nearest = roundf(val * pow(10,d_p)) / pow(10,d_p);
    return nearest;
}


int Bolzano_Bisection_Root(double a,double b,int d_p, int i,int count) // Recursive function for getting approx root
{

    double c = (a+b)/2,init_c,new_c;
    float f = Fx(c);
    printf("\nStep %d: a = %0.5f , b = %0.5f , bisection(c) = %lf f(c) = %0.4f, count = %d",i,a,b,c,f,count);
    
    if(f <0)
    {
        init_c = c;
        a=c;
        new_c = (a+b)/2;
        if(count == 3)
        {
            printf("\n\nLoop terminated, real root found = %.*lf",d_p,new_c);
            return 0 ;
        }    
        if(Round(init_c,d_p) == Round(new_c,d_p))
            count++;    
        else
            count =1 ;   

        i++;   
        Bolzano_Bisection_Root(a,b,d_p,i,count);
    }
    else
    {
        init_c = c;
        b=c;
        new_c = (a+b)/2;
        if(count == 3)
        {
            printf("\n\nLoop terminated, real root found = %.*lf",d_p,new_c); 
            return 0;
        }     
        if(Round(init_c,d_p) == Round(new_c,d_p))
            count++;
        else
            count =1; 
        i++; 
        Bolzano_Bisection_Root(a,b,d_p,i,count);
    }
}

int main()
{   
    double a,b;
    int d_p;
    printf("\n#####################   Welcome to Bolzano's Bisection Root Program ###############\n");
    printf("\n1.Enter the Lower limit (a) of the root: ");
    scanf("%lf",&a);
    printf("\n2.Enter the Upper limit (b) of the root: ");
    scanf("%lf",&b);
    printf("\n3.Enter the no of decimal places to be considered: ");
    scanf("%d",&d_p);

    clock_t begin = clock(); // CPU Time count starts (for getting the CPU time of execution of the recursive function)

    Bolzano_Bisection_Root(a,b,d_p,1,1); // Bolzano_Bisection_Root(...,1,1) initially set i=1 and count=1  
    //---------------------------------     Program ends when count = 3  -----------------------------------------------//
    clock_t end = clock(); // CPU Time count ends
    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC; // The difference in time is the execution time in sec
    printf("\nExecution time: %lf",time_spent);
    printf("\n");
    return 0;

}