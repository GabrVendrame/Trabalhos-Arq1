class Ula:
    def __init__(self):
        pass
    
    def soma(self, op1, op2):
        result = [" "] * 12
        cin = 0
        for i in range(len(op1)):
            ab = int(op1[len(op1) - i-1]) ^ int(op2[len(op2) - i-1])
            result[i] = ab ^ cin
            cin = ab & cin | int(op1[len(op1) - i-1]) & int(op2[len(op2) - i-1])
        if len(op1) < 12:
            result[len(op1)] = cin
        result.reverse()
        return result
        
    def subtracao(self, op1, op2):
        result = [" "] * 12
        bwin = 0
        for i in range (len(op1)):
            ab = int(op1[len(op1) - i-1]) ^ int(op2[len(op2) - i-1])
            result[i] = ab ^ bwin
            bwin = ~int(op1[len(op1) - i-1]) & int(op2[len(op2) - i-1]) | (~ab & bwin)
        if len(op1) < 12:
            result[len(op1)] = bwin
        result.reverse()
        return result

    def multiplicacao(self, op1, op2):
        uc = Uctrl()
        result = [0] * 12
        op1 = uc.verificaBits(op1, result)
        op2 = int(op2, 2)
        for i in range(op2):
            result = self.soma(op1, result)
        return result

    def divisao(self, op1, op2):
        uc = Uctrl()
        result = [0] * 12
        op1 = uc.verificaBits(op1, result)
        op2 = uc.verificaBits(op2, op1)
        while int(op1, 2) >= int(op2, 2):
            op1 = "".join(str(c) for c in self.subtracao(op1, op2))
            result = self.soma(result, "000000000001")
        return result

class Uctrl:
    def __init__(self):
        pass

    def converteBin(self, numero):
        numero_bin = format(int(numero), "b")
        return numero_bin
        
    def verificaBits(self, op1, op2):
        if len(op1) < len(op2):
            for i in range (len(op2) - len(op1)):
                op1 = '0' + op1
        return op1

    def selecOperacao(self, instrucao, op1, op2):
        ula = Ula()
        if instrucao == "ADD" or instrucao == "add":
            op1 = self.verificaBits(op1, op2)
            op2 = self.verificaBits(op2, op1)
            resultado = ula.soma(op1, op2)
            print(resultado)
        elif instrucao == "SUB" or instrucao == "sub":
            op1 = self.verificaBits(op1, op2)
            op2 = self.verificaBits(op2, op1)
            resultado = ula.subtracao(op1, op2)
            print(resultado)
        elif instrucao == "MUL" or instrucao == "mul":
            resultado = ula.multiplicacao(op1, op2)
            print(resultado)
        elif instrucao == "DIV" or instrucao == "div":
            resultado = ula.divisao(op1, op2)
            print(resultado)

def main():
    uc = Uctrl()
    instrucao = input()
    instrucao = instrucao.split(" ")
    op1 = uc.converteBin(instrucao[1])
    op2 = uc.converteBin(instrucao[2])
    print(op1)
    print(op2)
    #
    uc.selecOperacao(instrucao[0], op1, op2)

if __name__ == "__main__":
    main()