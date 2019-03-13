#include <iostream>
#include <vector>
using namespace std;

int find_unvisited(vector<int> visited, int n){
    int j;
    for(j = 0; j < n; j++){
        if(visited[j] == 0)
            return j;
    }
    return -1;
}

int main() {
	int n, num, j, k;
	
	cin>>n;
	vector<int> permu;
	vector<int> visited;   //keeps track whether an element has been visited
	for(j = 0; j < n; j++){
	    cin>>num;
	    permu.push_back(num);
	    visited.push_back(0);          //marking all unvisited
	}
	
	vector<vector<int>> allcycles;
	while(true){
	    int first_unvisited = find_unvisited(visited, n);
	    if(first_unvisited == -1)
	        break;
	    visited[first_unvisited] = 1;
	    int head = first_unvisited;
	    int current = permu[head];
	    vector<int> cycle;
	    cycle.push_back(head+1);
	    int steps = 0;
	    while(true){
	        cycle.push_back(current);
	        if(current-1 == head){
	            break;
	        }
	        visited[current-1] = 1;
	        current = permu[current-1];
	    }
	    allcycles.push_back(cycle);
	}
	int l = allcycles.size();
	cout<<l<<endl;
	for(j = 0; j < l; j++){
	    for(k = 0; k < allcycles[j].size(); k++)
	        cout<<allcycles[j][k]<<" ";
	    cout<<endl;
	}
	return 0;
}
