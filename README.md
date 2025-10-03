# API de Previsão de Diabetes

## Objetivo

Este projeto foi desenvolvido como uma forma de aplicar e aprofundar os conhecimentos em Machine Learning, focando na criação de um modelo preditivo para o diagnóstico de diabetes e na sua implementação através de uma API.

## Técnicas e Tecnologias Utilizadas

### Análise e Pré-processamento de Dados

* **Análise Exploratória de Dados (EDA):** A fase inicial consistiu em uma análise para entender a estrutura do dataset. Foram verificados os tipos de dados, a presença de valores nulos e a distribuição estatística de cada variável utilizando funções como `.info()`, `.isnull().sum()` e `.describe()`.

* **Padronização dos Dados (Scaler):** Foi utilizada a técnica `StandardScaler` da biblioteca Scikit-learn para reescalar os dados. Esse processo transforma os dados para que tenham uma média de 0 e um desvio padrão de 1, o que é fundamental para que o modelo de Machine Learning não seja enviesado por features com escalas de valores muito diferentes.

### Modelagem

* **Linguagem de Programação:** Python
* **Bibliotecas Principais:**
    * **Pandas:** Para manipulação e análise dos dados.
    * **Scikit-learn:** Para a criação e avaliação do modelo de Machine Learning.
    * **FastAPI:** Para a construção da API que serve o modelo.
    * **Joblib:** Para carregar o modelo treinado.
    * **Numpy:** Para manipulação de arrays.
* **Algoritmo de Machine Learning:** Foi utilizado o `RandomForestClassifier`, um método de ensemble learning que opera construindo uma infinidade de árvores de decisão no momento do treinamento e emitindo a classe que é o modo das classes (classificação) ou a previsão média (regressão) das árvores individuais.

* **Avaliação do Modelo:** O desempenho do modelo foi avaliado utilizando métricas como a matriz de confusão e o relatório de classificação, que inclui precisão, recall e f1-score, alcançando uma acurácia de aproximadamente 83%.

## Como a API Funciona

A API expõe o modelo de previsão de diabetes, permitindo que previsões sejam feitas através de requisições HTTP.

### Endpoints

* **`GET /`**
    * **Descrição:** Retorna uma mensagem de boas-vindas.
    * **Exemplo de Resposta:**
        ```json
        {
          "message": "API de Previsão de Diabetes"
        }
        ```

* **`POST /predict`**
    * **Descrição:** Realiza a previsão de diabetes com base nos dados do paciente enviados no corpo da requisição em formato JSON.
    * **Corpo da Requisição (JSON):**
        ```json
        {
          "Pregnancies": 6,
          "Glucose": 148,
          "BloodPressure": 72,
          "SkinThickness": 35,
          "Insulin": 0,
          "BMI": 33.6,
          "DiabetesPedigreeFunction": 0.627,
          "Age": 50
        }
        ```
    * **Exemplo de Resposta:**
        ```json
        {
          "Resultado": "Positivo para diabetes"
        }
        ```
    * **Exemplo com cURL:**
        ```bash
        curl -X POST "[http://127.0.0.1:8000/predict](http://127.0.0.1:8000/predict)" -H "Content-Type: application/json" -d '{"Pregnancies": 6, "Glucose": 148, "BloodPressure": 72, "SkinThickness": 35, "Insulin": 0, "BMI": 33.6, "DiabetesPedigreeFunction": 0.627, "Age": 50}'
        ```

* **`GET /predict/{Pregnancies}/{Glucose}/{BloodPressure}/{SkinThickness}/{Insulin}/{BMI}/{DiabetesPedigreeFunction}/{Age}`**
    * **Descrição:** Realiza a previsão de diabetes com base nos dados do paciente enviados como parâmetros na URL.
    * **Exemplo de URL:**
        ```
        https://api-diabetes.v1nimendes.com.br/predict/6/148/72/35/0/33.6/0.627/50
        ```
    * **Exemplo de Resposta:**
        ```json
        {
          "Resultado": "Positivo para diabetes"
        }
        ```
