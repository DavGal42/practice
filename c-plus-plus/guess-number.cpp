#include <iostream>
#include <ctime>
//srand(time(0));

int main() {
    int guess;
    int attempt = 0;

    srand(time(0));
    int num = rand() % 100 + 1;

    while(true) {
        std::cout << "Guess the number between 1-100\n";
        std::cout << "You have 7 attempts!\n";
        std::cin >> guess;

        if(guess < num) {
            attempt++;
            std::cout << "\nlower\n";
            std::cout << "Attempts: " << attempt << "/7\n\n";
        } else if (guess > num) {
            attempt++;
            std::cout << "\nhigher\n";
            std::cout << "Attempts: " << attempt << "/7\n\n";
        } else {
            std::cout << "\n-----------------\n";
            std::cout << "You win!\n";
            std::cout << "-----------------\n";
            break;
        }

        if(attempt == 7) {
            std::cout << "-----------------\n";
            std::cout << "You lose!\n";
            std::cout << "-----------------\n";
            break;
        }
    }

    return 0;
}