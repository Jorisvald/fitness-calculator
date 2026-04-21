seu_peso = float(input("Digite seu peso (EX = 82.7): "))
sua_altura = float(input("Digite sua altura (EX = 1.60): "))

#MENU
while True:
    print("1- O valor do seu IMC")
    print("2- Quanto de água você deve beber diáriamente")
    print("3- Estimativa de gasto calórico de atividades físicas")
    print("4- Se sua meta diária de exercícios foi concluida")
    print("5- Apresentar resumo diário de tudo")
    print("6- Finalizar programa")

    opcoes = int(input("Digite a opção desejada: "))
    #calculo de IMC
    if opcoes == 1:
        calculo_de_imc = seu_peso / (sua_altura * sua_altura)
        print(f"O seu IMC é {calculo_de_imc: .2f}")

    #meta diaria de hidrataçao
    elif opcoes == 2:
        calculo_de_hidra = seu_peso * 35
        print("Beber ", calculo_de_hidra, "ml")


    #estimativa de gasto calorico de  ativi. fisica -met(intensidade de atividade)
    elif opcoes == 3:
        print("Esses são os valores de intensidade média de cada atividade física")
        print("1- Descanso")
        print("2- Caminhada")
        print("3- Caminhada rapida")
        print("7- Esportes")
        print("10- Corrida")
        met = int(input("Digite o valor de intensidade da sua atividade: "))

        while met > 0:
            if met == 1 or met == 2 or met == 3 or met == 7 or met == 10:
                tempo_em_horas = int(input("Digite por quanto tempo você irá praticar a atividade em horas: "))
                tempo_em_min = int(input("Digite os minutos que você praticou: "))
                tempo_para_calculo = tempo_em_min/60 + tempo_em_horas
                calculo_gasto_atividade = met * seu_peso * tempo_para_calculo
                print("Estimativa de gasto calórico ", f"{calculo_gasto_atividade: .2f}", " kcal")
                break
            else:
                print("Comando inválido, digite novamente")
            met = int(input("Digite o valor de intensidade da sua atividade: "))




    #meta diaria de exercicios(tempo)
    elif opcoes == 4:
        meta_diaria = float(input("Digite a meta diária de tempo de exercícios: "))
        tempo_feito = float(input("Digite o tempo que voce praticou o exercício: "))
        calculo_de_meta = tempo_feito - meta_diaria
        if calculo_de_meta < 0:
            print("Você não concluiu sua meta diária")

        else:
            print("Você concluiu sua meta diária")


    #seu resumo diario
    elif opcoes == 5:
        #opção 1
        calculo_de_imc = seu_peso / (sua_altura * sua_altura)

        #opção 2
        calculo_de_hidra = seu_peso * 35

        #opção 3
        print("Para que possa lhe dar o resumo de tudo preciso das seguintes informações")
        print("Esses são os valores de intensidade média de cada atividade física")
        print("1- Descanso")
        print("2- Caminhada")
        print("3- Caminhada rapida")
        print("7- Esportes")
        print("10- Corrida")
        met = int(input("Digite o valor de intensidade da sua atividade: "))

        while met > 0 or met < 0 or met == 0:
            if met == 1 or met == 2 or met == 3 or met == 7 or met == 10:
                tempo_em_horas = int(input("Digite por quanto tempo você irá praticar a atividade em horas: "))
                tempo_em_min = int(input("Digite os minutos que você praticou: "))
                tempo_para_calculo = tempo_em_min/60 + tempo_em_horas
                calculo_gasto_atividade = met * seu_peso * tempo_para_calculo
                break
            else:
                print("Comando inválido, digite novamente")
            met = int(input("Digite o valor de intensidade da sua atividade: "))

        #opção 4
        meta_diaria = float(input("Digite a meta diária de tempo de exercícios: "))
        tempo_feito = float(input("Digite o tempo que voce praticou o exercício: "))
        calculo_de_meta = tempo_feito - meta_diaria

        print(f"o seu IMC é {calculo_de_imc: .2f}", "e você deve beber diáriamente ", calculo_de_hidra, "ml, e seu gasto de calorias em atividaes físicas é ", f"{calculo_gasto_atividade: .2f}", " kcal")
        if calculo_de_meta < 0:
            print("Você não concluiu sua meta diária")

        else:
            print("Você concluiu sua meta diária")

    #opcao 6
    elif opcoes == 6:
        print("Finalizando programa...")
        break
    else:
        print("Resposta inválida, digite novamente.")