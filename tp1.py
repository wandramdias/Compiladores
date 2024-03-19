import re  # Importa o módulo de expressões regulares

class SymbolTable(object):
    def __init__(self):
        self.symbolTable = {}
    
    def insertEntry(self, lexema, entry):
        if lexema not in self.symbolTable:
            self.symbolTable[lexema] = entry
    
    def getEntry(self, lexema):
        return self.symbolTable.get(lexema, None)

class TableEntry(object):
    def __init__(self, lexema, tipo, num_linha, ref_valor):
        self.lexema = lexema
        self.tipo = tipo
        self.num_linha = num_linha
        self.ref_valor = ref_valor
    
    def setTipo(self, tipo):
        self.tipo = tipo
    
    def setRefValor(self, rv):
        self.ref_valor = rv

# Criação de uma instância da tabela de símbolos
tabela_de_simbolos = SymbolTable()

# Inserção de entradas na tabela de símbolos
palavras_reservadas = ['fn', 'main', 'let', 'int', 'float', 'char', 'if', 'else', 'while', 'print', 'println', 'return']
sinais_de_pontuacao = ['(', ')', '->', ':', ',', '{', '}', '.', ';']
operadores = ['=', '==', '!=', '>', '>=', '<', '<=', '+', '-', '*', '/']
outros_terminais = [',', '"', "'", 'CHAR_LITERAL', 'FORMATTED_STRING']

# Adicionando palavras reservadas na tabela de símbolos
for palavra in palavras_reservadas:
    tabela_de_simbolos.insertEntry(palavra, TableEntry(palavra, 'PALAVRA_RESERVADA', None, None))

# Abertura do arquivo para leitura
with open('calculadora.p', 'r') as file:
    # Iteração sobre cada linha do arquivo
    for linha_num, linha in enumerate(file, 1):  # Enumerate começa a contar do 1
        # Usa expressão regular para encontrar lexemas na linha
        lexemas = re.findall(r'\b(?:\d+\.\d+|\d+|\w+)\b', linha)
        for lexema in lexemas:
            if lexema in palavras_reservadas:
                tipo = 'PALAVRA_RESERVADA'
            elif lexema.isdigit():
                tipo = 'INT'
            elif lexema.replace('.', '', 1).isdigit():
                tipo = 'FLOAT'
            else:
                tipo = 'ID'
            
            # Verifica a posição de início e término de cada lexema
            inicio = linha.find(lexema)
            fim = inicio + len(lexema) - 1
            print(f"Lexema: {lexema}, Tipo: {tipo}, Linha: {linha_num}, Início: {inicio}, Fim: {fim}")
