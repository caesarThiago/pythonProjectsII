import math

def fatorialNum(numero): 
    var_num = math.factorial(numero)
    return var_num

def principioFundamentalContagem(possibilidades, opcoes): 
    var_pfc = possibilidades * opcoes
    return var_pfc

def permutacaoSimples(numero): 
    var_ps = math.factorial(numero)
    return var_ps

def permutacaoRepeticao(total_evento, elementos_repetidos): 
    var_pr = (math.factorial(total_evento)) / (math.factorial(elementos_repetidos) * math.factorial(elementos_repetidos) * math.factorial(elementos_repetidos))
    return var_pr

def arranjoSimples(total_elementos_eventos, total_agrupamentos): 
    var_ank = math.factorial(total_elementos_eventos) / (math.factorial(total_elementos_eventos - total_agrupamentos))
    return var_ank

def arranjoRepeticao(total_elementos_eventos, total_num_escolhidos): 
    var_ank = math.pow(total_elementos_eventos, total_num_escolhidos)
    return var_ank

def combinacaoSimples(total_elementos_eventos, total_agrupamentos): 
    var_cs = math.factorial(total_elementos_eventos) / (math.factorial(total_agrupamentos) * math.factorial(total_elementos_eventos - total_agrupamentos))
    return var_cs

def combinacaoRepeticao(total_elementos_eventos, total_agrupamentos): 
    var_cr = math.factorial(total_elementos_eventos * total_agrupamentos - 1) / (math.factorial(total_agrupamentos) * math.factorial(total_elementos_eventos - 1))
    return var_cr

