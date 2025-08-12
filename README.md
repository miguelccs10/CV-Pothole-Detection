# 🚧 Detecção de Buracos de Asfalto com YOLO 🚧

## 📌 Visão Geral

Este projeto foi desenvolvido no âmbito da disciplina de **Laboratório de Inovação e Automação (LIA)** da Escola de Engenharia Elétrica, Mecânica e de Computação (EMC) da Universidade Federal de Goiás (UFG). O foco é a aplicação de técnicas de visão computacional, utilizando um modelo YOLO (You Only Look Once), para a detecção de buracos em superfícies asfaltadas.

## 🚀 Objetivos

Os principais objetivos deste projeto são:

* Implementar um sistema de detecção de buracos em tempo real ou a partir de vídeos.
* Utilizar o modelo YOLO para identificação precisa dos buracos.
* Aplicar o conhecimento adquirido na disciplina para desenvolver uma solução prática para um problema de infraestrutura urbana.
* Documentar o processo de desenvolvimento e a estrutura do projeto.

## 📊 Dataset

O treinamento e a validação do modelo de detecção foram realizados utilizando o dataset **"OmdenaKolkatta - Pothole Detection"**. Este conjunto de dados está disponível publicamente na plataforma Roboflow e pode ser acessado [aqui](https://universe.roboflow.com/tcr/omdenakolkatta).

## 🛠️ Tecnologias Utilizadas

As seguintes tecnologias e ferramentas foram empregadas no desenvolvimento deste projeto:

* **Python:** Linguagem de programação principal.
* **YOLO (You Only Look Once):** Arquitetura de detecção de objetos em tempo real (via biblioteca `ultralytics`).
* **Google Colab:** Ambiente de desenvolvimento e treinamento do modelo, com suporte a GPUs.
* **Roboflow:** Plataforma utilizada para gerenciamento e acesso ao dataset.
* **OpenCV:** Utilizado para processamento de vídeo (implícito pela `ultralytics` e em possíveis customizações).

## 📂 Estrutura do Projeto

O repositório está organizado com a seguinte estrutura de diretórios, refletindo os componentes do projeto:

```text
.
├── images/       # Contém imagens utilizadas ou geradas pelo projeto.
├── include/      # Diretório para arquivos de inclusão (ex: cabeçalhos, se aplicável).
├── Lib/          # Bibliotecas ou módulos customizados.
├── model/        # Arquivos do modelo treinado (ex: yolo_em_casa_portugues.pt).
├── runs/         # Resultados de execuções/treinamentos do modelo YOLO.
├── Scripts/      # Scripts principais do projeto.
├── share/        # Arquivos diversos ou compartilhados.
├── videos/       # Vídeos de entrada ou saída (ex: demonstrações).
└── yolo-model/   # Arquivos específicos do modelo YOLO (configs, pesos alternativos, etc.).
```

## 🎬 Resultados e Demonstração

O modelo treinado foi capaz de detectar buracos em vídeos. Como demonstração prática, o sistema foi testado no estacionamento da **Escola de Engenharia Elétrica, Mecânica e de Computação da UFG**.

Você pode assistir à demonstração do projeto no YouTube clicando na imagem abaixo:

[![Demonstração do Projeto de Detecção de Buracos](https://img.youtube.com/vi/3hrs6ikKXnE/hqdefault.jpg)](https://youtube.com/shorts/3hrs6ikKXnE?feature=share)

---
