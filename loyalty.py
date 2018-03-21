import random
import pickle

def people():
    print(people)


def load(people):
    try:
        me = pickle.load(open("info.txt", "rb"))
    except EOFError:
        me = []
    return people

def askSave(save):
   
    ask = input("Save info?\n-->").upper()
    if ask == "yes":
        output = open('info.txt', 'wb')
        pickle.dump(people, output)
        output.close()
        print(people)



    elif ask == "no":
        print("Thanks anyways")
        return
        people = load()


print('Good Evening, Thank you for choosing Food Mart!')
print('Would you like to create an account?')

while True:
    choice = input("> ")


    if choice == 'yes':
        print('What is your name?')
        name = input()
        print("Ok " + name + ".")
        print('What is your email?')
        email = input()

        
        print('Is your information correct?')
        
        answer_choice = input('yes or no >>> ')

        if answer_choice == 'yes':
            print('Great, your information is stored')
            print('We will start you off with 200 loyalty points!')
            

            points = 200
 

        if answer_choice == 'no':
            print('What is your name?')
            name = input()
            print("Ok " + name + ".")
            print('What is your email?')
            email = input()
            print('Have a good day!')
            break

 
    elif choice == 'no':
        print('Have a good day!')
        break


people.append({'name': name, 'email': email, 'points': points})

askSave(people)


            


