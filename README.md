# GS1-PYTHON
Descrição do problema e foco da resolução:  
Em vista da dificuldade que é uma pessoa sintomática por alguma doença se locomover a uma farmácia e consultar quais remédios melhor se encaixa para o seu quadro, pensamos em algo que focasse na praticidade dessa situação.  
 
Descrição da solução idealizada: 
Pensando nisso, nossa ideia é criar um site farmacêutico onde serão apresentados os medicamentos e suplementos disponíveis para a compra, além de integrar um ChatBot, onde a IA fará basicamente a função de um farmacêutico: apontar o melhor medicamento conforme o sintoma geral da pessoa. Caso seja algo mais agravante, ele orientará a passar com um especialista. 
 
Implementação: 
O site será possível através de um código HTML responsável pela navegação do usuário. A interação com a IA será por conta do ChatBot desenvolvido através das ferramentas do IBM Cloud. O banco de dados também será necessário para armazenar as informações dos medicamentos e usuários que acessarem o ChatBot. Para isso, criaremos um Diagrama de Entidade Relacionametal contendo todos os atributos a entidades necessários para a devida relação dos dados. Será implementado também um Diagrama de classes com atributos e métodos presentes na Farmácia Virtual, além de um projeto Java contendo as Classes do Domínio apresentados nesse Diagrama. Por fim, iremos criar um Menu, onde através de alguns códigos em Python, haverá interação da Farmácia Virtual com usuário. 
 
Objetivo do projeto: 
Navegando pelo site da SalesForce percebe-se a ausência de um leitor descritivo de imagens, o que além de contribuir para a dificuldade no acesso de pessoas com baixa visão ou deficientes visuais, acaba tornando o site escasso de acessibilidade. Com isso, nosso objetivo é a implementação desse leitor, onde o usuário será capaz de compreender melhor as informações apresentadas no site através do acesso ao significado das imagens ali retratadas. 
 
Como nosso sistema suprirá o site a Sales Force? 
Com o foco do challenge sendo a acessibilidade no site da SalesForce, analisando alguns aspectos, decidimos focar no público com algum tipo de deficiência visual. Como ao acessar o site essas pessoas já têm acessos a softwares leitores de textos, mas não a leitores de imagens, com a implementação do nosso sistema até a 4° sprint, o usuário poderá saber o que as imagens ali presentes representam, suprindo a questão de uma maior acessibilidade para a empresa. 

Este projeto se baseia em um menu de uma farmácia  on-line.
Possui uma lista com quatro tópicos:
1- consultar medicamentos
2-realizar compra
3-consultar pedidos
4- sair

-Se o usuário selecionar “1.Consultar medicamentos” ira aparecer os medicamentos e suas unidades disponíveis.
-Se o usuário selecionar “2.realizar compra” o programa irá pedir à pessoa coloque o nome do medicamento e quantas unidades.
Caso coloque o nome errado ou uma quantidade mais do que tem no estoque irá aparecer a mensagem:
"Desculpe, o medicamento escolhido não está disponível ou a quantidade desejada é maior do que o estoque. "
-Se o usuário selecionar “3.consultar pedidos” o programa irá mostrar o pedido da pessoa.
Caso não tenha feito nenhum pedido, irá aparecer a seguinte mensagem “Nenhum pedido realizado até o momento.". E o programa irá rodar novamente.
E por ultimo a opção “4.Sair” que finaliza o programa.

LINK VÍDEO: https://youtu.be/OMt3WbHK8Ns?si=LVIBdXyZF49TUm2s

INTEGRANTES DO GRUPO
Giovanna Lima (RM:553369)
Rebeca Lopes (RM:553764)
Matheus MariOtto (RM:554200)
