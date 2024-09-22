import time

palavra = "REACT"

jubileu = [
 "o",
"/", "|", "/",
 "|",
"/", "/" ]

jubileu_perdeu = [
    "  _______     ",
    "  |     |     ",
    "  |     o     ",
    "  |    /|/    ",
    "  |     |     ",
    "  |    / /    ",
    "__|__         "
]

jubileu_ganhou = [
 " o",         
 "\\|/",       
 " |",      
"/ \\"     ]

def iniciar_jogo():
    
    palavra_correta = (len(palavra) * "-")


    print("\n🔔 Seja muito bem-vindo(a) ao Jogo da Forca! 🔔")
    print("Será que você consegue salvar o Jubileu? 😱")
    time.sleep(2)
    print("\nRegras do jogo:\n")
    print("- O Jubileu está em perigo! A cada erro, uma parte do corpo dele será enforcada.")
    print(f"- Você tem {len(palavra)+1} tentativas para adivinhar a palavra correta e salvar o Jubileu!")
    print("- Se errar todas as vezes, Jubileu será enforcado! 😢")

    print(f'   {jubileu[0]} \n {jubileu[1]} {jubileu[2]} {jubileu[3]} \n   {jubileu[4]} \n  {jubileu[5]} {jubileu[6]}')
    
    time.sleep(2)
    
    count = len(palavra)+1

    while count >= 1:

        lista_palavra_correta = list(palavra_correta)
        
        print(f'\n TEMA: LINGUAGEM DE PROGRAMAÇÃO, {len(palavra_correta)} Letras')

        print(f'\n {palavra_correta} ')

        resposta = input("\nDigite alguma letra da palavra: ").upper()

        if resposta in palavra:
            
            print(f"\nMuito bem, a letra {resposta} existe nessa palavra!!!\n")

            for index, i in enumerate(palavra):
                
                if palavra[index] == resposta:
                    lista_palavra_correta[index] = resposta
                        
            palavra_correta = "".join(lista_palavra_correta)

            if "".join(lista_palavra_correta) == palavra:
                print("\nMeus parabéns, você conseguiu vencer o jogo da forca!!!")
                print(f"\nA palavra era {palavra}\n")
                print("Jubileu deve à vida a você, veja sua comemoração!!!")
                print(f' {jubileu_ganhou[0]} \n {jubileu_ganhou[1]} \n {jubileu_ganhou[2]} \n {jubileu_ganhou[3]} \n ')
                break

        else:
            print(f'\n \nNegativo!!! a letra {resposta} não existe nessa palavra, Jubileu está mais perto do seu fim!!! >:D ')
            count-=1
            print(f'\n Você tem {count} tentativas\n')

            time.sleep(1)

        if count == 0:
            print(f'Hehehe a forca venceu como era previsto, era uma vez Jubileu...')
            print(f'\n {jubileu_perdeu[0]} \n {jubileu_perdeu[1]} \n {jubileu_perdeu[2]} \n {jubileu_perdeu[3]} \n {jubileu_perdeu[4]} \n {jubileu_perdeu[5]} \n {jubileu_perdeu[6]} \n')
            print(f'\n A palavra correta era: {palavra}\n')
            break


iniciar_jogo()