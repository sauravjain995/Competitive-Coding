#include <iostream>
using namespace std;

int main(){
	int T,m,n,D,i,j,k,l;
	cin >> T;
	for(i=0;i<T;i++){
		cin >> n >> m >> D;
		j = 0;
		for(l=0;l<n;l++){
			cin >> k;
			if(1.0*k/D > (int)(k/D)) {
				j += k/D;
			} else if(1.0*k/D == (int)k/D) {
				j += k/D - 1;
			}
		}
		if (j>=m)
			cout<<"YES"<<endl;
		else
			cout<<"NO"<<endl;
		}
	}
