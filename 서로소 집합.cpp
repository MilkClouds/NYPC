#include <iostream>
using namespace std;
int par[100];

void init(){
	for(int i=0;i<100;i++)par[i]=i;
}
int find(int u){
	return u==par[u] ? u : par[u]=find(par[u]); //Path Compression
}
void merge(int u,int v){
	u=find(u);v=find(v);
	if(u==v)return;
	par[u]=v; // without Union-By-Rank
}

int main(){
	init();
	merge(1,5);
	merge(2,5);
	merge(4,1);
	cout<<(find(5)==find(4))<<endl;
	cout<<(find(0)==find(1))<<endl;
}