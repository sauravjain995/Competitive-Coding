#include <stdio.h>

int main(){
	int T,i,a,final=0;
	scanf("%d",&T);
	for (i=0;i<T;i++){
		scanf("%d",&a);
		final ^= a;
	}
	printf("%d",final);
	return 0;
}