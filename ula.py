class Ula:
    def __init__(self):
        pass
    
    def soma(self, operando1, operando2):
        i, j = len(operando1)-1, len(operando2)-1
        result = ""
        cin = 0
        # compara bit a bit ambos operadores até que o tamanho de um chegue a 0
        while i >= 0 and j >= 0:
            ab = int(operando1[i]) ^ int(operando2[j])
            result += str(ab ^ cin)
            cin = ab & cin | int(operando1[i]) & int(operando2[j])
            i -= 1
            j -= 1
        # termina a comparacao caso o segundo operador tenha tamanho 0 no primeiro "while"
        while i >= 0 :
            result += str(int(operando1[i]) ^ cin)
            cin = int(operando1[i]) & cin
            i -= 1
        # termina a comparacao caso o primeiro operador tenha tamanho 0 no primeiro "while"
        while j >= 0:
            result += str(int(operando2[j]) ^ cin)
            cin = int(operando2[j]) & cin
            j -= 1
        # trata bits excedentes
        if len(result) < 12 and cin == 1:
            result += str(cin)
        return result[::-1]
        
    def subtracao(self, operando1, operando2):
        i, j = len(operando1)-1, len(operando2)-1
        result = ""
        bwin = 0
        # mesma ideia da funcao de soma para todos os laços
        while i >= 0 and j >= 0:
            ab = int(operando1[i]) ^ int(operando2[j])
            result += str(ab ^ bwin)
            bwin = ~int(operando1[i]) & int(operando2[j]) | (~ab & bwin)
            i -= 1
            j -= 1
        while i >= 0 :
            result += str(int(operando1[i]) ^ bwin)
            bwin = ~int(operando1[i]) & bwin
            i -= 1
        while j >= 0:
            result += str(int(operando2[j]) ^ bwin)
            bwin = ~int(operando2[j]) & bwin
            j -= 1
        return result[::-1]

    def multiplicacao(self, operando1, operando2):
        result = "0"
        # soma o número n vezes // n = operando2 base10
        for i in range(int(operando2, 2)):
            result = self.soma(operando1, result)
        return result

    def divisao(self, operando1, operando2):
        result = "0"
        # subtrai o número n vezes // n = operando2 base10
        while int(operando1, 2) >= int(operando2, 2):
            operando1 = self.subtracao(operando1, operando2)
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
            operando1 = self.complementoDois(instrucao[1])
            operando2 = self.complementoDois(instrucao[2])
            resultado = ula.soma(operando1, operando2)
            print("Soma: {}".format(resultado))
        elif instrucao[0] == "SUB" or instrucao[0] == "sub":
            operando1 = self.complementoDois(instrucao[1])
            operando2 = self.complementoDois(instrucao[2])
            resultado = ula.subtracao(operando1, operando2)
            print("Subtracao: {}".format(resultado))
        elif instrucao[0] == "MUL" or instrucao[0] == "mul":
            operando1 = self.converteBin(instrucao[1])
            operando2 = self.converteBin(instrucao[2])
            resultado = ula.multiplicacao(operando1, operando2)
            print("Multiplicacao: {}".format(resultado))
        elif instrucao[0] == "DIV" or instrucao[0] == "div":
            operando1 = self.converteBin(instrucao[1])
            operando2 = self.converteBin(instrucao[2])
            resultado = ula.divisao(operando1, operando2)
            print("Divisao: {}".format(resultado))

def main():
    uc = Uctrl()
    with open("entrada.txt") as file:
        for line in file:
            instrucao = line.strip("\n").split(" ")
            uc.selecOperacao(instrucao)

if __name__ == "__main__":
    main()