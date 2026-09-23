import os
import urllib.parse

EXTENSOES_IMAGEM = (".png", ".jpg", ".jpeg", ".webp", ".gif")
PASTA_RAIZ = "."
README_PATH = "README.md"

def gerar_tabela():
    linhas_tabela = []
    
    for arquivo in sorted(os.listdir(PASTA_RAIZ)):
        if arquivo.lower().endswith(EXTENSOES_IMAGEM):
            # Codifica corretamente espaços e caracteres especiais para a URL
            arquivo_url = urllib.parse.quote(arquivo)
            link_raw = f"https://raw.githubusercontent.com/alexpietro2007/Imagens/refs/heads/main/{arquivo_url}"
            
            # Limpa o nome amigável para exibir na coluna do meio
            nome_limpo = arquivo.rsplit('.', 1)[0].replace('—', '').replace('-', ' ').strip()
            nome_amigavel = nome_limpo.title() if nome_limpo else arquivo
            
            # Monta a linha com o link encapsulado corretamente
            linha = f'| <img src="{link_raw}" width="100"> | `{nome_amigavel}` | [Clique aqui]({link_raw}) |'
            linhas_tabela.append(linha)

    return "\n".join(linhas_tabela)

def atualizar_readme():
    tabela_gerada = gerar_tabela()
    
    conteudo_novo = f"""# 📦 Repositório de Assets | Imagens Online

Este repositório serve exclusivamente para hospedagem de imagens e recursos visuais, atualizado automaticamente.

---

## 🖼️ Galeria de Imagens

| Visualização | Nome do Arquivo | Link Direto (Raw) |
| :---: | :--- | :--- |
{tabela_gerada}

---

## 🚀 Como usar uma imagem deste repo
Para usar as imagens em bots ou sites, você precisa do link **Raw**:
1. Clique no arquivo da imagem dentro do GitHub.
2. Clique no botão **"Raw"** no canto superior direito da imagem.
3. Copie a URL do navegador. Ela deve começar com `https://raw.githubusercontent.com/...`

---
<p align="right">Organizado por Solo Nosso</p>
"""

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(conteudo_novo)

if __name__ == "__main__":
    atualizar_readme()