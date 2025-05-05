import qrcode
from PIL import Image
import os

def gerar_qrcode():
    try:
        # Configurações iniciais
        os.makedirs("qrcodes", exist_ok=True)  # Cria pasta se não existir
        
        print("\n" + "="*40)
        print("GERADOR DE QR CODE AVANÇADO".center(40))
        print("="*40)
        
        # Inputs do usuário
        url = input("\n🔗 Digite a URL (ex: google.com): ").strip()
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
            
        nome = input("📝 Nome do arquivo (sem .png): ").strip() or "qrcode"
        nome_arquivo = os.path.join("qrcodes", f"{nome}.png")  # Salva na pasta /qrcodes/
        
        # Personalização avançada
        print("\n🎨 Personalização (deixe em branco para padrão):")
        cor = input("Cor do QR Code (ex: black, #FF0000): ") or "black"
        fundo = input("Cor de fundo (ex: white, #FFFFFF): ") or "white"
        tamanho = int(input("Tamanho (1-40, padrão=10): ") or 10)

        # Geração do QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=tamanho,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color=cor, back_color=fundo)
        img.save(nome_arquivo)
        
        # Resultado
        print("\n" + "═"*40)
        print(f"✅ QR Code gerado com sucesso!")
        print(f"📂 Pasta: {os.path.abspath('qrcodes')}")
        print(f"📄 Arquivo: {os.path.basename(nome_arquivo)}")
        print(f"🔗 Link: {url}")
        print(f"🎨 Cores: {cor} sobre {fundo}")
        print("═"*40)
        
        img.show()  # Abre a imagem
        
    except ValueError:
        print("\n❌ Erro: Tamanho deve ser um número entre 1 e 40!")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")

if __name__ == "__main__":
    gerar_qrcode()