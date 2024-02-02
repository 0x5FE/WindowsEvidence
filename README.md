# Funcionalidades

- ***Coleta de registros do visualizador de eventos:***
        Copia os arquivos de log de eventos do Windows, incluindo Application.evtx, Security.evtx e System.evtx, localizados em ***C:\Windows\System32\winevt\Logs\***, para o diretório de evidências.

- ***Coleta de arquivos de configuração do sistema:***
        Copia os arquivos de configuração do sistema, como sam, security e system, ***localizados em C:\Windows\System32\config\, para o diretório de evidências.***

- ***Coleta de dados do aplicativo:***
        Recupera arquivos de dados relevantes para o aplicativo, incluindo bancos de dados (.db), arquivos de texto (.txt) e arquivos de log (.log), de diretórios específicos em ***C:\Users\*\\AppData\Roaming e C : \Arquivos de Programas\*\\AppData\Roaming.***

- ***Identificação única do diretório de evidências:***
        O diretório de evidências é nomeado de acordo com o nome da máquina e um carimbo de data/hora, garantindo exclusividade e facilitando a organização.

- ***Exibição de mensagem de conclusão:***
        Após a conclusão da coleta, é exibida uma mensagem indicando o diretório onde as evidências foram armazenadas.


O script é executado na linha de comando e requer dois argumentos obrigatórios:

    machine_name: nome da máquina de destino.
    
    evidencia_dir: Diretório de destino para armazenar evidências coletadas

# Exemplo de uso:

`python audit.py machine_name C:\path\to\store\evidence`


# Possíveis erros e soluções

  ***Argumentos ausentes:***
        Se os argumentos machine_name ou evidencia_dir estiverem faltando, o script exibirá mensagens de erro. Certifique-se de fornecer ambos os argumentos.

   ***Permissões insuficientes:***
        Certifique-se de que o usuário que executa o script tenha as permissões necessárias para acessar os arquivos e diretórios especificados.

  ***Diretório de destino inexistente:***
        Se o diretório de destino especificado não existir, o script tentará criá-lo. No entanto, certifique-se de ter permissões suficientes para criar diretórios no caminho especificado.

  ***Arquivos não existentes:***
        Se alguns dos arquivos específicos não existirem no sistema, o script poderá falhar ao tentar copiá-los. Certifique-se de que esses arquivos estejam presentes no sistema de destino.

- Certifique-se de revisar as evidências coletadas para garantir que todas as informações relevantes sejam preservadas.
