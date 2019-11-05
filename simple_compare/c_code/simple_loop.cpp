#include<iostream>
#include <chrono> 
using namespace std::chrono; 
using namespace std;
int main(int argc, char **argv){
	int n = atoi(string(argv[1]).c_str());
	auto start = high_resolution_clock::now();
	int a = 0;
	for(int i; i < n; i++){
		a += 1;
	}
	auto stop = high_resolution_clock::now();	
	auto duration = duration_cast<microseconds>(stop - start); 
	cout << "Running " << n << " loops: " << (float)(duration.count()) / 1000000<< " s" << endl; 

}
