print("Welcome to our fitness calculator, check the |MENU| options and make your choice. But first, tell me this information.")

seu_peso = float(input("Enter your weight (EX = 82.7): "))
sua_altura = float(input("Enter your height (EX = 1.60): "))
meta_diaria = float(input("Enter your daily exercise time goal: "))

#MENU
while True:
    print("|MENU|")
    print("1- Your BMI value")
    print("2- How much water you should drink daily")
    print("3- Estimated calorie burn from physical activities")
    print("4- Check if your daily exercise goal was completed")
    print("5- Show full daily summary")
    print("6- Exit program")

    opcoes = int(input("Enter the desired option: "))
    # BMI calculation
    if opcoes == 1:
        calculo_de_imc = seu_peso / (sua_altura * sua_altura)
        if calculo_de_imc < 18.5:
            print(f"Your BMI is {calculo_de_imc: .2f}", " you are underweight.")
        elif calculo_de_imc >= 18.5 and calculo_de_imc <= 24.9:
            print(f"Your BMI is {calculo_de_imc: .2f}", " you are at an ideal weight.")
        elif calculo_de_imc >= 25 and calculo_de_imc <= 29.9:
            print(f"Your BMI is {calculo_de_imc: .2f}",  " you are overweight")
        elif calculo_de_imc >= 30 and calculo_de_imc <= 34.9:
            print(f"Your BMI is {calculo_de_imc: .2f}", " you have obesity")
        elif calculo_de_imc > 35:
            print(f"Your BMI is {calculo_de_imc: .2f}", " you have severe obesity")

    # daily hydration goal
    elif opcoes == 2:
        calculo_de_hidra = seu_peso * 35
        print("Drink ", calculo_de_hidra, "ml")

    # estimated calorie burn from physical activity (MET)
    elif opcoes == 3:
        print("These are the average intensity values for each physical activity")
        print("1- Rest")
        print("2- Walking")
        print("3- Fast walking")
        print("7- Sports")
        print("10- Running")
        met = int(input("Enter the intensity value of your activity: "))

        while met > 0:
            if met == 1 or met == 2 or met == 3 or met == 7 or met == 10:
                tempo_em_horas = int(input("Enter how many hours you practiced the activity: "))
                tempo_em_min = int(input("Enter the minutes you practiced: "))
                tempo_para_calculo = tempo_em_min/60 + tempo_em_horas
                calculo_gasto_atividade = met * seu_peso * tempo_para_calculo
                print("Estimated calorie burn ", f"{calculo_gasto_atividade: .2f}", " kcal")
                break
            else:
                print("Invalid input, try again")
            met = int(input("Enter the intensity value of your activity: "))

    # daily exercise goal (time)
    elif opcoes == 4:
        tempo_feito = float(input("Enter the time you exercised: "))
        calculo_de_meta = tempo_feito - meta_diaria
        if calculo_de_meta < 0:
            print("You did not complete your daily goal")
        else:
            print("You completed your daily goal")

    # daily summary
    elif opcoes == 5:
        # option 1
        calculo_de_imc = seu_peso / (sua_altura * sua_altura)

        # option 2
        calculo_de_hidra = seu_peso * 35

        # option 3
        print("To provide your full summary, I need the following information")
        print("These are the average intensity values for each physical activity, enter the number of the one you practiced.")
        print("1- Rest")
        print("2- Walking")
        print("3- Fast walking")
        print("7- Sports")
        print("10- Running")
        met = int(input("Enter the intensity value of your activity: "))

        while met > 0 or met < 0 or met == 0:
            if met == 1 or met == 2 or met == 3 or met == 7 or met == 10:
                tempo_em_horas = int(input("Enter how many hours you practiced the activity: "))
                tempo_em_min = int(input("Enter the minutes you practiced: "))
                tempo_para_calculo = tempo_em_min/60 + tempo_em_horas
                calculo_gasto_atividade = met * seu_peso * tempo_para_calculo
                break
            else:
                print("Invalid input, try again")
            met = int(input("Enter the intensity value of your activity: "))

        # option 4
        tempo_feito = float(input("Enter the time you exercised: "))
        calculo_de_meta = tempo_feito - meta_diaria

        print(f"Your BMI is {calculo_de_imc: .2f}", "and you should drink daily ", calculo_de_hidra, "ml, and your calorie burn from activities is ", f"{calculo_gasto_atividade: .2f}", " kcal")
        if calculo_de_meta < 0:
            print("You did not complete your daily goal")
        else:
            print("You completed your daily goal")

    # option 6
    elif opcoes == 6:
        print("Ending program...")
        break
    else:
        print("Invalid response, try again.")
