#include "Node.h"

int Node::getMagnitude() const { return magnitude; }

NodeInterface* Node::getnext() const { return next.get(); }

NodeInterface* Node::getprev() const { return prev.get(); }