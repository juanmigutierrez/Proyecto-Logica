#include <random>
#include <iostream>
#include "heap.hpp"

int main() {
    const short min = 1;
    const short max = 5;
    std::random_device rd;
    std::default_random_engine generator{rd()};
    std::uniform_int_distribution<short> distribution(min, max);

    // declare and initialize heap of shorts
    BinaryHeap<short> hp;

    // fill heap

    for (int i = min; i <= max; i++) {
        short number = distribution(generator);
        hp.insert(number);
        std::cout << "Inserted " << number << std::endl;
    }

    std::cout << "Heap:" << std::endl;
    hp.display();
    std::cout << std::endl;

    // print heap minimum
    std::cout << "Min Heap:" << hp.findMin() <<	std::endl;

    // remove elements in order
    while(!hp.isEmpty()){
        std::cout << hp.findMin() << std::endl;
        hp.deleteMin();
    }
    std::cout << std::endl;
    return 0;
}
