#include <iostream>
using namespace std;

int N,M,ans;
string S;
int main(){
	cin>>N>>M;
	for(int i=0;i<N*M;i++){
		cin>>S;
		ans+=S=="NEXON";
	}
	cout<<ans;
}
