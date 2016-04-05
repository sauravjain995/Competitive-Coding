#include <stdio.h>

int main(){
	int a,T,n,sum;
	while(1){
		sum = 0;
		scanf("%d",&n);
		if(n==0)
			break;
		else{
			for(a=1;a<=n;a++){
				sum += a*a;
			}
		}
		printf("%d\n",sum);
	}

}