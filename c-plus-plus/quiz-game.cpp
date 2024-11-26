#include <iostream>


int main() {

    std::string questions[] = {"1. What does the acronym 'HTML' stand for?",
                                "2. Which programming language is primarily used for developing Android apps?",
                                "3. What symbol is used to start a comment in Python?",
                                "4. Which data structure uses the LIFO principle (Last In, First Out)?"};

    std::string options[][4] = {{"A. Hyper Text Machine Language", "B. Hyper Text Markup Language",
                                "C. High Tech Markup Language", "D. Hyperlink Markup Language"},
                                {"A. Python", "B. Java", "C. Swift", "D. Ruby"},
                                {"A. //", "B. <!--", "C. #", "D. /*"},
                                {"A. Queue", "B. Array", "C. Stack", "D. Linked List"}};

    char answerKey[] = {'B', 'B', 'C', 'C'};

    int questionsSize = sizeof(questions)/sizeof(std::string);
    int optionsSize = sizeof(options[0])/sizeof(std::string);
    char guess;
    int score = 0;

    for(int i = 0; i < questionsSize; i++) {
        std::cout << "-----------------------------------------------------------------------\n";
        std::cout << questions[i] << "\n";
        std::cout << "-----------------------------------------------------------------------\n";

        for(int j = 0; j < optionsSize; j++) {
            std::cout << options[i][j] << "\n";
        }

        std::cin >> guess;
        guess = toupper(guess);

        if(guess == answerKey[i]) {
            std::cout << "Correct!\n";
            score++;
        } else {
            std::cout << "Wrong!\n";
            std::cout << "Answer: " << answerKey[i] << '\n';
        }
    }

    std::cout << "--------------\n";
    std::cout << "Score: " << score << "/4\n";    
    std::cout << "--------------\n";    

    return 0;
}