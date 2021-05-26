from questions import QUESTIONS
import random



def moneyWon(money, padaav, result):
    if result == "quit":
        print("Rs.",money)
    else:
        if padaav < 5:
            print("Rs. 0")
        elif padaav >= 5 and padaav < 10:
            print("Rs. 10,000")
        elif padaav >= 10:
            if result == "loss":
                print("Rs. 3,20,000")
            else:
                print("Rs. 1,00,00,000")



def isAnswerCorrect(question, answer):

    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''
    return True if answer == question["answer"] else False      #remove this


def lifeLine(ques):

    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''

    choose = ["1","2","3","4"]
    choose.remove(str(ques["answer"]))
    print(choose)
    choose = [random.choice(choose), str(ques["answer"])]
    return choose







def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks

    money = 0 
    padaav = 0
    result = ""
    choose = ["1","2","3","4"]
    lifeline_used = True
    check = False
    i = 0

    while i < 16:
        print(f'\tQuestion : {QUESTIONS[i]["name"]}' )
        print(f'\t\tOptions:')
        if "1" in choose:
            print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
        else:
            print()
        if "2" in choose:
            print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
        else:
            print()
        if "3" in choose:
            print(f'\t\t\tOption 3: {QUESTIONS[i]["option3"]}')
        else:
            print()
        if "4" in choose:
            print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')
        else:
            print()
        

        ans = "0"
        while not (ans == "1" or ans == "2" or ans == "3" or ans == "4"):
            ans = input('Your choice ( 1-4 ) : ')
            if ans == "quit":
                break
            if ans == "lifeline" and lifeline_used:
                lifeline_used = False
                choose = lifeLine(QUESTIONS[i])
                check = True
                break
            if not (ans == "1" or ans == "2" or ans == "3" or ans == "4"):
                if ans == "lifeline" and not lifeline_used:
                    print("Lifeline Already used")
                else:
                    print("Invalid Input")

        if check  and ans == "lifeline":
            check = False
            continue

        if ans == "quit":
            result = ans
            break

        # check for the input validations
        ans
        if isAnswerCorrect(QUESTIONS[i], int(ans)):
            # print the total money won.
            # See if the user has crossed a level, print that if yes
            print('\nCorrect !')
            padaav += 1
            money = QUESTIONS[i]["money"]
            print(money)

        else:
            # end the game now.
            # also print the correct answer
            print('\nIncorrect !')
            print("Correct Answer was " + QUESTIONS[i]["option" + str(QUESTIONS[i]["answer"])])
            result = "loss"
            break
        i = i + 1
        if padaav == 15:
            break
        if not lifeline_used:
            choose = ["1","2","3","4"]
    # print the total money won in the end.
    moneyWon(money, padaav, result)


kbc()
