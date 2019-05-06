#include <iostream>
using namespace std;

int N,M,ans;
string S;
int main(){
	cin>>N>>M;
	for(int i=0;i<N;i++)for(int j=0;j<M;j++){
		cin>>S;
		ans+=S=="NEXON";
	}
	cout<<ans;
}
