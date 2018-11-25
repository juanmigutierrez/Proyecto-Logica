#ifndef heap_hpp
#define heap_hpp

#include <vector>
#include <iostream>

template <typename DataType>
class BinaryHeap{
public:
    BinaryHeap(int capacity = 100);

    bool isEmpty() const;
    const DataType & findMin() const;

    void insert(const DataType & elem);
    void deleteMin();

    void clear();
    void display() const;

private:
    unsigned int count;           // Numero de elementos
    std::vector<DataType> array;  // Vector de elementos
    void percolateDown(int hole);

};

#include "heap.cpp"

#endif /* heap_hpp */
