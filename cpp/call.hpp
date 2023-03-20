#ifndef CALL_HPP
#define CALL_HPP

int get_value(void);

void print_fizzbuzz(int data);

template <typename T, typename U>
auto Sum(T a, U b) {
    return a + b;
}

template <typename T>
class Rectangle {
    public:
    Rectangle(T height, T width) : height_(height), width_(width){}

    T Area() const {
        return height_ * width_;
    }

    private:
        const T height_;
        const T width_;
};

#endif
