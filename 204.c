#include <stdio.h>
#include <math.h>

int is_prime(int n){
    if (n == 1) {
        return 0 ;
    }
    else if(n == 2){
        return 1 ;
    }
    int squre = sqrt(n) ;
    int i ;
    for(i = 2 ; i < squre + 1 ; i ++){
        if (n % i == 0){
            return 0 ;

        }
    }
    return 1 ;
}
    

int factors(int n) {
    int j, squre ;
    squre = sqrt(n) ;
    for (j = 1 ; j <= squre + 1 ; j ++ ){
        if ((n % j == 0) && (is_prime(j) == 1) && (j > 100)){
            return 1 ;
        }
        else if ((n % j == 0) && (is_prime(n/j)) && ((n/j) > 100)){
            return 1 ;
        }
    }
    return 0 ;
}

int main(){
    int n = 1 ;
    int counter = 0 ;
    while (n <= pow(10, 9)){
        printf("%d\n", n) ;
        if (factors(n) == 0) {
            counter += 1 ;
        }
        n += 1 ;
    }
    printf("counter = %d\n", counter) ;
}
