#include "DLLInterface.h"
#include "LinkedList.h"
#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
#include <cstring>
using namespace std;

class DLL: public DLLInterface
{
public:
	DLL(){}
	~DLL(){}

	/**
	* Adds the given name to the end of the list so that at(-1) == name.
	* After the operation, the size should have increased by 1..
	*/
	bool insertTail(string name);

	/**
	* Removes all nodes from the list.
	* size() should return 0 after this operation.
	*/
	void clear();

};

