#include <stdio.h>


// int move(n, source, target, extra) {
//     if (n == 0) {
//         return
//     }
//     else {
//         move(n - 1, source, extra, target)
//         #target.append source.pop
//         move(n - 1, extra, target, source)
//     }
// }


// int print_all(a, b, c) {
//     printer(a, length_a);
//     printer(b, length_b);
//     printer(c, length_c);
// }


int printer(int array[], int length) {
    for (int i = 0; i <= length; ++i)
        printf(" %d ", array[i])
    return 0;
}


int main(){
    #define N 3

    int a[N], b[N], c[N];

    for (int i = 0; i <= N; ++i)
        a[i] = i + 1;

    printer(&a, N);
}