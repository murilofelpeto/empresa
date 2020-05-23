from empresa import Pessoa, Funcionario, Programador, Estagiario, Vendedor, Empresa


def test_calcula_salario_programador():
    programador = Programador("Nome", 23, "prg@empresa.com.br", 40)
    salario = programador.calcula_salario()
    assert salario == 6300.00

def test_aumento_salario_programador():
    programador = Programador("Nome", 23, "prg@empresa.com.br", 40)
    programador.aumenta_salario()
    assert programador.calcula_salario() == 6615.00

def test_calcula_salario_estagiario():
    estagiario = Estagiario('Nome', 18, 'estag@empresa.com.br', 20)
    salario =  estagiario.calcula_salario()
    assert salario == 1645.0

def test_aumento_salario_estagiario():
    estagiario = Estagiario('Nome', 18, 'estag@empresa.com.br', 20)
    estagiario.aumenta_salario()
    assert estagiario.calcula_salario() == 1714.75

def test_calcula_salario_sem_visita_vendedor():
    vendedor = Vendedor("Nome", 30, "vendedor@empresa.com.br", 30)
    salario = vendedor.calcula_salario()
    assert salario == 4400.00

def test_calcula_salario_com_duas_visitas_vendedor():
    vendedor = Vendedor("Nome", 30, "vendedor@empresa.com.br", 30)
    vendedor.realizar_visita(2)
    salario = vendedor.calcula_salario()
    assert salario == 4460.00

def test_calcula_salario_apos_zerar_visitas_vendedor():
    vendedor = Vendedor("Nome", 30, "vendedor@empresa.com.br", 30)
    vendedor.realizar_visita(2)
    salario = vendedor.calcula_salario()
    assert salario == 4460.00

    vendedor.zerar_visitas()
    salario = vendedor.calcula_salario()
    assert salario == 4400.00

def test_aumento_salario_vendedor():
    vendedor = Vendedor("Nome", 30, "vendedor@empresa.com.br", 30)
    vendedor.aumenta_salario()
    assert vendedor.calcula_salario() == 4602.50

def test_calcula_folha_pagamento_empresa():
    programador = Programador("prg", 23, "prg@empresa.com.br", 40)
    estagiario = Estagiario('estag', 18, 'estag@empresa.com.br', 20)
    vendedor1 = Vendedor("v1", 30, "v1@empresa.com.br", 30)
    vendedor2 = Vendedor("v2", 30, "v2@empresa.com.br", 30)

    funcionarios = list()
    funcionarios.append(programador)
    funcionarios.append(estagiario)
    funcionarios.append(vendedor1)
    funcionarios.append(vendedor2)
    
    empresa = Empresa("Empresa", 12345, "TI", funcionarios)
    folha_pagamento = empresa.folha_pagamento()
    assert folha_pagamento == 16745.00

def test_calcula_folha_pagamento_com_dissidio_empresa():
    programador = Programador("prg", 23, "prg@empresa.com.br", 40)
    estagiario = Estagiario('estag', 18, 'estag@empresa.com.br', 20)
    vendedor1 = Vendedor("v1", 30, "v1@empresa.com.br", 30)
    vendedor2 = Vendedor("v2", 30, "v2@empresa.com.br", 30)

    funcionarios = list()
    funcionarios.append(programador)
    funcionarios.append(estagiario)
    funcionarios.append(vendedor1)
    funcionarios.append(vendedor2)
    
    empresa = Empresa("Empresa", 12345, "TI", funcionarios)
    empresa.dissidio_anual()
    folha_pagamento = empresa.folha_pagamento()
    assert folha_pagamento == 17534.75

def test_mostra_visitas_empresa():
    programador = Programador("prg", 23, "prg@empresa.com.br", 40)
    estagiario = Estagiario('estag', 18, 'estag@empresa.com.br', 20)
    
    vendedor1 = Vendedor("v1", 30, "v1@empresa.com.br", 30)
    vendedor1.realizar_visita(3)
    
    vendedor2 = Vendedor("v2", 30, "v2@empresa.com.br", 30)
    vendedor2.realizar_visita(5)

    funcionarios = list()
    funcionarios.append(programador)
    funcionarios.append(estagiario)
    funcionarios.append(vendedor1)
    funcionarios.append(vendedor2)
    
    empresa = Empresa("Empresa", 12345, "TI", funcionarios)
    assert vendedor1.email in empresa.listar_visitas()
    assert empresa.listar_visitas()[vendedor1.email] == 3

    assert vendedor2.email in empresa.listar_visitas()
    assert empresa.listar_visitas()[vendedor2.email] == 5

def test_zera_visitas_empresa():
    programador = Programador("prg", 23, "prg@empresa.com.br", 40)
    estagiario = Estagiario('estag', 18, 'estag@empresa.com.br', 20)
    
    vendedor1 = Vendedor("v1", 30, "v1@empresa.com.br", 30)
    vendedor1.realizar_visita(3)
    
    vendedor2 = Vendedor("v2", 30, "v2@empresa.com.br", 30)
    vendedor2.realizar_visita(5)

    funcionarios = list()
    funcionarios.append(programador)
    funcionarios.append(estagiario)
    funcionarios.append(vendedor1)
    funcionarios.append(vendedor2)
    
    empresa = Empresa("Empresa", 12345, "TI", funcionarios)
    assert vendedor1.email in empresa.listar_visitas()
    assert empresa.listar_visitas()[vendedor1.email] == 3

    assert vendedor2.email in empresa.listar_visitas()
    assert empresa.listar_visitas()[vendedor2.email] == 5

    empresa.zerar_visitas_vendedores()
    assert vendedor1.email in empresa.listar_visitas()
    assert empresa.listar_visitas()[vendedor1.email] == 0

    assert vendedor2.email in empresa.listar_visitas()
    assert empresa.listar_visitas()[vendedor2.email] == 0
# Fazer os testes do vendedor (calcula salario, calcula aumento, aumenta visita)
# Fazer os testes de erro de carga horaria
# Fazer os testes de carga horaria (consulta e alteração)