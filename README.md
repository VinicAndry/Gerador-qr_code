# 🚀 Gerador de QR Code Avançado

Um script Python simples mas poderoso para gerar QR Codes personalizados com diversas opções de configuração.

## 📦 Pré-requisitos
- Python 3.6+
- Pacotes necessários:
  ```bash
  pip install qrcode[pil] pillow
🛠️ Como usar
Clone o repositório:

bash
git clone https://github.com/VinicAndry/Gerador-qr_code.git
Navegue até a pasta:

bash
cd Gerador-qr_code
Execute o script:

bash
python qr_generator.py
✨ Funcionalidades
✅ Gera QR Codes a partir de URLs
✅ Personalização avançada:

Escolha de cores (hexadecimal ou nomes)

Tamanho ajustável

Nome personalizado para o arquivo
✅ Cria automaticamente a pasta qrcodes
✅ Visualização imediata do QR Code gerado

📝 Exemplo de Uso
========================
GERADOR DE QR CODE AVANÇADO
========================

🔗 Digite a URL (ex: google.com): github.com/VinicAndry
📝 Nome do arquivo (sem .png): meu-github

🎨 Personalização (deixe em branco para padrão):
Cor do QR Code (ex: black, #FF0000): #FF5733
Cor de fundo (ex: white, #FFFFFF): 
Tamanho (1-40, padrão=10): 15

════════════════════════
✅ QR Code gerado com sucesso!
📂 Pasta: /caminho/do/projeto/qrcodes
📄 Arquivo: meu-github.png
🔗 Link: https://github.com/VinicAndry
🎨 Cores: #FF5733 sobre white
════════════════════════
🏗️ Estrutura do Projeto
Gerador-qr_code/
├── qr_generator.py  # Script principal
├── qrcodes/         # Pasta com QR Codes gerados
├── README.md        # Este arquivo
└── requirements.txt # Dependências
🤝 Como Contribuir
Faça um fork do projeto

Crie sua branch (git checkout -b feature/nova-funcionalidade)

Commit suas mudanças (git commit -m 'Adiciona nova funcionalidade')

Push para a branch (git push origin feature/nova-funcionalidade)

Abra um Pull Request

📄 Licença
Este projeto está sob a licença MIT - veja o arquivo LICENSE para detalhes.

Feito por Vinicius Andrade



### Dicas extras:
1. Crie um arquivo `requirements.txt` com:
qrcode[pil]
pillow


2. Adicione um arquivo `.gitignore` para evitar upload de arquivos desnecessários:
pycache/
*.pyc
qrcodes/


3. Para deixar ainda mais profissional, você pode:
- Adicionar um arquivo LICENSE
- Criar um executável (.exe) usando PyInstaller
- Fazer deploy como um pacote PyPI

📦 Pacotes Necessários (Instale via pip)
Execute este comando no terminal/prompt:

bash
pip install qrcode[pil] pillow
Isso instalará:

qrcode (com suporte a PIL) - Biblioteca principal para gerar QR Codes

pillow (PIL) - Para manipulação de imagens (salvar/visualizar os QR Codes)
