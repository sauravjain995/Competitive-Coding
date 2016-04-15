#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main(){
	long long int T,n,m,i,j,a,b,ans;
	bool flag;
	map<long long int,long long int> dic;
	scanf("%lld",&T);
	for(i=0;i<T;i++){
		scanf("%lld",&n);
		flag = true;
		ans = 0;
		dic.clear();
		for(j=0;j<n;j++){
			scanf("%lld",&m);
			if(dic.find(m)==dic.end()){
				dic[m] = 1;
				if(dic[m]>n/2){
					flag = false;
					ans = m;
				}
			}
			else{
				dic[m]++;
				if(dic[m]>n/2){
					flag = false;
					ans = m;
				}
			}
		}
		if(flag == false){
			cout << "YES " << ans << endl;
		}
		else{
			cout << "NO"<< endl;
		}
	}
}