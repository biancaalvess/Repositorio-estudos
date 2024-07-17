def notas(*n, sit=False):
    """"
    -> Função para analisar notas e situações de vários alunos
    :param n: uma ou mais notas dos alubis(aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações osbre a siuação da turma.
    """
    r = dict()
    r['total'] = len (n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] > 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOAVÉL'
        else:
            r['situação'] = 'RUIM'
    return r


#Programa Principal
resp = notas(9, 10, 5.5, 2.5, 9, 8.5, sit=True)
print(resp)
help(notas)