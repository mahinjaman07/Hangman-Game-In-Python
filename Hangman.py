MyWord = "Hello";
chance = 5;
GuesLatters = [];
Done = False;

while not Done:
    for letter in MyWord:
        if letter.lower() in GuesLatters:
            print(letter, end=" ");
        else:
            print("_", end= "");



    Myguess = input(f"Your Chances {chance}, Guess The Next Letter: ");
    GuesLatters.append(Myguess.lower());

    if Myguess.lower() not in MyWord:
        chance -= 1;

        if chance == 0 :
            print("You are loser..! Please Try Again...<3");
            break;
    Done = True;
    for latter in MyWord:
         if latter.lower() not in GuesLatters:
             Done = False;


if Done:
    print(f"You Have Won The Game, The Word Is {MyWord}")
