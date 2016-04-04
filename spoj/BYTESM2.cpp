#include <iostream>
using namespace std;
int max(int a,int b, int c){
	if(a>b){
		if(a>c){
			return a;
		}
	}
	if(b>c){
		return b;
	}
	return c;
}
int max(int arr[], int size) {
	int it, maxval = 0;
	for(it = 0; it < size; it++) {
		if(maxval < arr[it]) {
			maxval = arr[it];
		}
	}
	return maxval;
}

int main(){
	int t,it;
	cin >> t;
	for (it=0;it<t;it++){
		int h,w;
		cin >> h >> w;
		int DP[102][102],X[102][102];
		for (int i=0; i<h;i++){
			for(int j=0;j<w;j++){
				cin >> X[i][j];
				DP[i][j] = 0;
			}
			DP[i][w] = 0;
			DP[i][w+1] = 0;
		}
		for (int l=0;l<w;l++){
			DP[0][l+1] = X[0][l];
		}
		for (int i=1; i<h;i++){
			for(int j=1;j<w+1;j++){
				DP[i][j] = X[i][j-1] + max(DP[i-1][j-1],DP[i-1][j],DP[i-1][j+1]);
			}
		}
		cout << max(DP[h-1],w+2);

	}
	return 0;

}