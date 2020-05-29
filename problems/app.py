if __name__ == "__main__":

    current = 2020;
    isAge = False;
    isYear = False;
    yearBirth = 0;
    number = int(input('enter age or age/year of birth : '));

    if number<125:
        isAge = True;
    elif number>1900:
        isYear = True;
    else:
        print('Problem with input...');
        exit();

    if isAge:
        yearBirth = current-number;
        print(f'You will become 100 years old in {yearBirth+100}');
    elif isYear:
        print(f'Your age is {current-number} and you will become 100 years old in {number+100}');
        yearBirth = number;

    print('1.you want to know your age in perticular year\n2.Exit')
    num = int(input());
    if num==1:
        year = int(input('Enter year: '));
        if year-yearBirth<=-2:
            print(f"Don't fool us you born in {yearBirth} and you are asking for age in {year}");
        elif abs(yearBirth-year)==1:
            print("You are in your mother's stomach not born yet...");
        elif year==yearBirth:
            print(f'You born in {year}')
        elif yearBirth<year:
            print(f'Your age in {year} will be {year-yearBirth}');    
    else:
        exit();
