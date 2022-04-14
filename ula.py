class Ula:
    def __init__(self):
        pass
    
    def soma(self, op1, op2):
        i, j = len(op1)-1, len(op2)-1
        result = ""
        cin = 0
        # percorre e compara os dois números até que o tamanho de um dos dois chegue a "zero"
        while i >= 0 and j >= 0:
            ab = int(op1[i]) ^ int(op2[j])
            result += str(ab ^ cin)
            cin = ab & cin | int(op1[i]) & int(op2[j])
            i -= 1
            j -= 1
        # "while" complementar ao de cima, caso o operador2 tenha sido a causa
        # da quebra do primeiro laço
        while i >= 0 :
            result += str(int(op1[i]) ^ cin)
            cin = int(op1[i]) & cin
            i -= 1
        # "while" complementar ao primeiro "while", caso o operador1 tenha sido a causa
        # da quebra do primeiro "while"
        while j >= 0:
            result += str(int(op2[j]) ^ cin)
            cin = int(op2[j]) & cin
            j -= 1
        # trata "bits" excedentes
        if len(result) < 12 and cin == 1:
            result += str(cin)
        return result[::-1]
        
    def subtracao(self, op1, op2):
        i, j = len(op1)-1, len(op2)-1
        result = ""
        bwin = 0
        while i >= 0 and j >= 0:
            ab = int(op1[i]) ^ int(op2[j])
            result += str(ab ^ bwin)
            bwin = ~int(op1[i]) & int(op2[j]) | (~ab & bwin)
            i -= 1
            j -= 1
        while i >= 0 :
            result += str(int(op1[i]) ^ bwin)
            bwin = ~int(op1[i]) & bwin
            i -= 1
        while j >= 0:
            result += str(int(op2[j]) ^ bwin)
            bwin = ~int(op2[j]) & bwin
            j -= 1
        # similar a soma
        return result[::-1]

    def multiplicacao(self, op1, op2):
        result = "0"
        for i in range(int(op2, 2)):
            result = self.soma(op1, result)
        return result

    def divisao(self, op1, op2):
        result = "0"
        while int(op1, 2) >= int(op2, 2):
            op1 = self.subtracao(op1, op2)
            result = self.soma(result, "1")
        return result

class Uctrl:
    def __init__(self):
        pass

    def complementoDois(self, operando):
        ula = Ula()
        um = '1'
        if(operando[0] == '-'):
            operando = operando[1:]
            numero_bin = self.converteBin(operando)
            numero_bin = '0' + numero_bin
            numero_bin = list(numero_bin)
            for i in range (len(numero_bin)):
                if numero_bin[i] == '0':
                    numero_bin[i] = '1'
                else:
                    numero_bin[i] = '0'
            result = "".join(char for char in ula.soma(numero_bin, um))
            return result
        else:
            numero_bin = self.converteBin(operando)
            numero_bin = '0' + numero_bin
            return numero_bin
            
    def converteBin(self, operando):
        numero_bin = format(int(operando), "b")
        return numero_bin

    def selecOperacao(self, instrucao):
        ula = Ula()
        if instrucao[0] == "ADD" or instrucao[0] == "add":
            op1 = self.complementoDois(instrucao[1])
            op2 = self.complementoDois(instrucao[2])
            resultado = ula.soma(op1, op2)
            print(resultado)
        elif instrucao[0] == "SUB" or instrucao[0] == "sub":
            op1 = self.complementoDois(instrucao[1])
            op2 = self.complementoDois(instrucao[2])
            resultado = ula.subtracao(op1, op2)
            print(resultado)
        elif instrucao[0] == "MUL" or instrucao[0] == "mul":
            resultado = ula.multiplicacao(op1, op2)
            print(resultado)
        elif instrucao[0] == "DIV" or instrucao[0] == "div":
            resultado = ula.divisao(op1, op2)
            print(resultado)

def main():
    uc = Uctrl()
    instrucao = input()
    instrucao = instrucao.split(" ")
    ##
    uc.selecOperacao(instrucao)

if __name__ == "__main__":
    main()