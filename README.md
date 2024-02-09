
# Script de Download Automatizado de Vulnerabilidades

Este script Python automatiza o download de arquivos de vulnerabilidades de diferentes provedores, conforme especificado em um arquivo de configuração XML. Ele suporta downloads agendados através de cron jobs e pode operar através de um proxy, se necessário. 

## Recursos

- Leitura de configurações de provedor de um arquivo XML.
- Download de arquivos a partir de URLs especificadas.
- Suporte para execução através de proxies.
- Logging de atividades e erros.

## Pré-requisitos

- Python 3.x
- Biblioteca `requests` do Python (Instale usando `pip install requests`).

## Configuração

1. **Arquivo de Configuração XML**: Nomeie o arquivo como `vulnerabilities-database.conf` e estruture-o conforme o exemplo abaixo:

    ```xml
    <vulnerabilities-databases>
        <provider name="NomeDoProvedor">
            <enabled>yes</enabled>
            <source>"URL"</source>
        </provider>
        <!-- Adicione mais provedores conforme necessário -->
    </vulnerabilities-databases>
    ```

2. **Configuração do Proxy**: Se estiver em um ambiente que requer um proxy para acesso à internet, configure o script com os detalhes do proxy editando as linhas relevantes no script:

    ```python
    proxies = {
        "http": "http://endereco_do_proxy:porta",
        "https": "http://endereco_do_proxy:porta",
    }
    ```

    Substitua `endereco_do_proxy` e `porta` pelos valores corretos do seu ambiente. Para autenticação, use:

    ```python
    proxies = {
        "http": "http://usuario:senha@endereco_do_proxy:porta",
        "https": "http://usuario:senha@endereco_do_proxy:porta",
    }
    ```

    **Nota de Segurança**: Tenha cuidado ao inserir credenciais de proxy diretamente no script.

3. **Configuração do Logging**: O script registra todas as operações em `download_log.log`. Verifique este arquivo para acompanhar o progresso e identificar possíveis erros.

## Execução

Execute o script manualmente usando:

```bash
python download_all_providers.py
```

Ou configure um cron job para automação:

```cron
*/30 * * * * /usr/bin/python3 /caminho/para/download_all_providers.py
```

Este cron job executa o script a cada 30 minutos.



## Contribuições

Sinta-se livre para forkar o projeto, enviar pull requests ou relatar bugs e sugestões na seção de issues.

## Licença

```license
Licença MIT

Copyright (c) 2024 

A permissão é concedida, gratuitamente, a qualquer pessoa que obtenha uma cópia
deste software e dos arquivos de documentação associados (o "Software"), para lidar
com o Software sem restrição, incluindo, sem limitação, os direitos
de usar, copiar, modificar, fundir, publicar, distribuir, sublicenciar e/ou vender
cópias do Software, e permitir às pessoas a quem o Software é
fornecido fazê-lo, sob as seguintes condições:

O aviso de direitos autorais acima e este aviso de permissão devem ser incluídos em todas as
cópias ou partes substanciais do Software.

O SOFTWARE É FORNECIDO "COMO ESTÁ", SEM GARANTIA DE QUALQUER TIPO, EXPRESSA OU
IMPLÍCITA, INCLUINDO, MAS NÃO SE LIMITANDO A, AS GARANTIAS DE COMERCIALIZAÇÃO,
ADEQUAÇÃO A UM PROPÓSITO ESPECÍFICO E NÃO INFRINGIMENTO. EM NENHUM CASO OS
AUTORES OU DETENTORES DOS DIREITOS AUTORAIS SERÃO RESPONSÁVEIS POR QUALQUER RECLAMAÇÃO, DANOS OU OUTRA
RESPONSABILIDADE, SEJA EM AÇÃO DE CONTRATO, TORTURA OU DE OUTRA FORMA, DECORRENTE DE,
FORA OU EM CONEXÃO COM O SOFTWARE OU O USO OU OUTRAS NEGOCIAÇÕES NO SOFTWARE.
```

