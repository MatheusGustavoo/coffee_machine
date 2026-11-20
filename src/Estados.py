import enum


class Estado_Maquina(enum.Enum):
    PRONTA = "aceita crédito e pedidos"
    AGUARDANDO_LIMPEZA = (
        "atingido o limite de 30 preparos desde a última limpeza; pedidos bloqueados."
    )
    MANUTENCAO = (
        "colocada pelo operador para reabastecer ou limpar; pedidos bloqueados."
    )
    PREPARANDO = "há uma bebida em preparo; novos pedidos são recusados até o término."
