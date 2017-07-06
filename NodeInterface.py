//YOU MAY NOT MODIFY THIS DOCUMENT

#pragma once

#include <iostream>

class NodeInterface {

public:
	NodeInterface() {}
	virtual ~NodeInterface() {}

	/*
	* @return the data that is stored in this node.
	*/
	virtual int getMagnitude() const = 0;

	/*
	* @return the next of this node or null if it doesn't have one.
	*/
	virtual NodeInterface * getNext() const = 0;

	/*
	* @return the next of this node or null if it doesn't have one.
	*/
	virtual NodeInterface * getPrev() const = 0;

};