import os

EXTENSOES_IMAGEM = (".png", ".jpg", ".jpeg", ".webp", ".gif")
PASTA_RAIZ = "."
README_PATH = "README.md"

def gerar_tabela():
    linhas_tabela = []
    
    # Lista os arquivos do repositório
    for arquivo in sorted(os.listdir(PASTA_RAIZ)):
        if arquivo.lower().endswith(EXTENSOES_IMAGEM):
            # Monta o link raw padrão do GitHub para o usuário atual
            link_raw = f"https://raw.githubusercontent.com/alexpietro2007/Imagens/refs/heads/main/{arquivo}"
            nome_amigavel = arquivo.rsplit('.', 1)[0].replace('-', '_').title()
            
            # Linha da tabela no formato que você usa
            linha = f'| <img src="{link_raw}" width="100"> | `{nome_amigavel}` | [Clique aqui]({link_raw}) |'
            linhas_tabela.append(linha)

    return "\n".join(linhas_tabela)

def atualizar_readme():
    tabela_gerada = gerar_tabela()
    
    # Conteúdo estruturado do README
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