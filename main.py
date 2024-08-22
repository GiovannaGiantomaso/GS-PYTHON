class Farmacia:
   def __init__(self):
       self.medicamentos_disponiveis = {"Paracetamol": 10, "Aspirina": 15, "antiinflamatorio": 5}
       self.pedidos = []
   def exibir_menu_principal(self):
       print("Bem-vindo à Farmácia Online")
       print("1. Consultar Medicamentos")
       print("2. Realizar Compra")
       print("3. Consultar Pedidos")
       print("4. Sair")
   def consultar_medicamentos(self):
       print("Lista de Medicamentos Disponíveis:")
       for medicamento, estoque in self.medicamentos_disponiveis.items():
           print(f"{medicamento}: {estoque} unidades")

   def realizar_compra(self):
       print("Realizar Compra:")
       self.consultar_medicamentos()
       medicamento_escolhido = input("Digite o nome do medicamento desejado: ")
       quantidade_desejada = int(input("Digite a quantidade desejada: "))
       if (
           medicamento_escolhido in self.medicamentos_disponiveis
           and quantidade_desejada <= self.medicamentos_disponiveis[medicamento_escolhido]
       ):
           self.medicamentos_disponiveis[medicamento_escolhido] -= quantidade_desejada
           self.pedidos.append({medicamento_escolhido: quantidade_desejada})
           print("Compra realizada com sucesso!")
       else:
           print(
               "Desculpe, o medicamento escolhido não está disponível ou a quantidade desejada é maior do que o estoque."
           )
   def consultar_pedidos(self):
       print("Consultar Pedidos:")
       if not self.pedidos:
           print("Nenhum pedido realizado até o momento.")
       else:
           for index, pedido in enumerate(self.pedidos, start=1):
               print(f"Pedido {index}: {pedido}")

   def menu_principal(self):
       while True:
           self.exibir_menu_principal()
           escolha = input("Digite o número da opção desejada: ")
           if escolha == "1":
               self.consultar_medicamentos()
           elif escolha == "2":
               self.realizar_compra()
           elif escolha == "3":
               self.consultar_pedidos()
           elif escolha == "4":
               print("Saindo... Obrigado!")
               break
           else:
               print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
   farmacia_online = Farmacia()
   farmacia_online.menu_principal()
