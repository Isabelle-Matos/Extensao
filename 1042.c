#include <stdio.h>


int main()
{
    int a[3], b[3], aux = 0;
    for(int i = 0; i<3; i++){
        scanf("%d", &a[i]);
    }
  for(int i = 0; i<3; i++){
        b[i] = a[i];
  }


  for(int i=0; i<3; i++){
    for(int j=i; j<3; j++){
        if(a[i]>a[j]){
            aux = a[i];
            a[i] = a[j];
            a[j] = aux;
        }

    }
  }
    for(int i = 0; i<3; i++){
    printf("%d\n", a[i]);

  }
  printf("\n");
  
    for(int i = 0; i<3; i++){
    printf("%d\n", b[i]);
  }


   
    return 0;
}
