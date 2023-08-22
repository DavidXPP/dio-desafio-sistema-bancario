import datetime

menu = 0
l = 0
saldo_atual = 0
i = 0
agora = datetime.datetime.now()
transacoes = []
formato_resumido = "%d/%m/%Y %H:%M:%S"
dia_atual = agora.now()




def deposito(saldo_atual, transacoes):
    try:
        sald_deposi = float(input("""
        Insira em R$ o quantidade que você deseja
        depositar:\n
        """))
        if sald_deposi < 0:
            print("Por favor, digite apenas números positivos!")
            deposito(saldo_atual)
    except ValueError:
        print("Por favor, digite apenas números!")
        deposito(saldo_atual)
    else:
        saldo_atual = sald_deposi + saldo_atual
        transacoes.append(agora.strftime(formato_resumido))
        transacoes.append(f"+R${sald_deposi}")

    return saldo_atual, transacoes

def saque(saldo_atual, transacoes, dia_atual, l):
        dia_atual = datetime.datetime.now()
        try:
            sald_saque = float(input("""
            Insira em R$ o quantidade que você deseja
            sacar:\n5
            """))
            if sald_saque < 0:
                print("Por favor, digite apenas números positivos!")
                saque(saldo_atual, transacoes, dia_atual, l)
        except ValueError:
            print("Por favor, digite apenas números!")
            saque(saldo_atual, transacoes, dia_atual, l)
        else:
            if sald_saque > saldo_atual:
                print(f"""Você não possuí saldo o suficiente, o seu saldo é R${saldo_atual:.2f} e você tentou sacar R${sald_saque:.2f}""")
                saque(saldo_atual, transacoes, dia_atual, l)
            elif sald_saque > 500:
                print(f"""Você não pode sacar mais que R$500,00, você tentd
                ou sacar R${sald_saque:.2f}""")
                saque(saldo_atual, transacoes, dia_atual, l)
            else:
                saldo_atual = saldo_atual - sald_saque
                transacoes.append(agora.strftime(formato_resumido))
                transacoes.append(f"-R${sald_saque}")
        l+=1
        if l >= 3:
            print(f"Você excedeu o número de saques, tente novamente em {dia_atual + datetime.timedelta(hours=24)}")
            dia_atual + datetime.timedelta(hours=24)
        return saldo_atual, transacoes, dia_atual, l

def extrato(saldo_atual, transacoes):
    for n in range(len(transacoes)):
        print(transacoes[n])
    print(f"Saldo Atual: R${saldo_atual}")
    return saldo_atual, transacoes


while menu != 'q':
    
    menu = input("""

    [d] - para depósito
    [s] - para saque
    [e] - para extrato
    [q] - para sair

    """)
    if menu == 'd':
        status = deposito(saldo_atual, transacoes)
        saldo_atual, transacoes = status[0], status[1]
        print(f"Seu saldo atual é:R${saldo_atual:.2f}")
    elif menu == 's':
        status = saque(saldo_atual, transacoes, dia_atual, l)
        saldo_atual, transacoes, dia_atual, l = status[0], status[1], status[2], status[3]
        if dia_atual <= agora.now() and l>=3:
            l = 0
        print(f"Seu saldo atual é:R${saldo_atual:.2f}, {l}")
    elif menu == 'e':
        status = extrato(saldo_atual, transacoes)
        saldo_atual, transacoes = status[0], status[1]
    elif menu == 'q':
        print("Até mais!")
        break
    else:
        if i > 0:
            print("Por favor digite alguma opção válida!")
    i += 1