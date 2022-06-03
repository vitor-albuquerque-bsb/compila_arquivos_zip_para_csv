# compila_arquivos_zip_para_csv
Programa desenvolvido para facilitar a consolidação de arquivos .csv que estão dentro  de várias pastas zipadas e exclusão de colunas desnecessárias.

Auxiliar de tarefas em ETL.

Como usar:

	1 - Diretório de Origem - Selecione o caminho onde contém as pastas zipadas contendo os arquivos .csv;

	2 - Diretório de Destino - Selecione o caminho onde o novo arquivo .csv consolidado será salvo;

	3 - Exclusão de Colunas - Especifique o nome das colunas que devem ser excluídas;

	4 - Após a especificação dos dados acima, clique em 'compilar' e aguarde o aviso de conclusão.

Importante:

* A pasta de origem deve conter apenas pastas com extensão .zip, caso contrário será gerado erro. Separe uma pasta
  apenas com os arquivos que devem ser tratados.

* Também será gerado erro caso seja descrita coluna inexistente. A nomenclatura das colunas devem estar EXATAMENTE iguais
  as colunas do arquivo original.

* As colunas devem ser separadas por vírgula, qualquer outro tipo de separador não é aceito. Exemplo:
  COLUNA1,COLUNA2,COLUNA3,COLUNA99,COLUNA114

* No momento o programa só roda em conjunto com o drop de colunas, caso não deseje excluir nenhuma coluna do compilado, 
  entre em contato comigo para ajuste do código fonte ou aguarde desenvolvimento.

* Em caso de tratamento de big dados, é normal ocorrer travamento ou lentidão na execução do programa. 
  Aguarde a mensagem de conclusão.

::Sobre::

Este programa foi escrito por Vítor Albuquerque em Python utilizando pandas e tkinter.
