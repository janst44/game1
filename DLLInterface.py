#ifndef DLLINTERFACE_H_
#define DLLINTERFACE_H_

#include <string>

using namespace std;


/*
* Warning: Do not modify this document in any way, including its name.  Consequences of doing so
* include the inability to compile with the grading test driver.  As stated in the Midterm packet,
* any section of code that does not compile will not be graded.
*/

/**
* The DLLInterface defines some of the  basic operations performed on a double-linked list.
* Your implementation of this interface must be a  double-linked list.
*/
class DLLInterface {
public:
	DLLInterface(){};
	virtual ~DLLInterface(){};

	/**
	* Adds a Node to the end of the list.
	* After the operation, the size should have increased by 1.
	*/
	virtual bool insertTail(string name) = 0;

	/**
	* Deletes all DDL Nodes allocated on the heap.
	*/
	virtual void clear() = 0;
};

#endif /* DLLINTERFACE_H_ */

