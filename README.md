# Envelope dos resíduos de um GLM em Python

Baseado no código em R do livro Modelos de Regressão com Apoio Computacional, de Gilberto A. Paula.

## Introdução

Os modelos lineares generalizados (GLM) são utilizados em diversas aplicações em problemas de aprendizado estatístico, como por exemplo em tarefas de regressão ou classificação. 

Uma etapa importante na análise de um modelo ajustado é uma verificação das pressuposições feitas, principalmente para o componente aleatório, e para a existência de observações discrepantes com interferência desproporcional nos resultados do ajuste.

Nessa análise, é comum a utilização dos denominados *envelopes* para observar o tamanho da influência de cada resíduo.

## Metodologia

Seja um Modelo Linear Generalizado definido como:

$$\boldsymbol{Y} = \boldsymbol{X} \beta +  \epsilon$$

em que:

 - $\boldsymbol{Y} = (y_1, ..., y_n)*$ corresponde ao vetor da variável resposta
 - $\boldsymbol{X} = (\boldsymbol{1}, \boldsymbol{X_1}, ... \boldsymbol{X_{p-1}}$ é a matriz de covariáveis do modelo
 - $\boldsymbol{\\beta} = (\beta_0, ..., \beta_n)$ vetor de parâmetros,
 - $\boldsymbol{\epsilon} = (\epsilon_1, ..., \epsilon_n)$ é o vetor de erros
 - $n$ é o número de observações, e $p$ o número de parâmetros.
 
### Suposições

#### Normalidade
#### Independência
#### Homocedasticidade

## Conjunto de dados utilizado

## Conclusões

## Códigos

## Referências

https://www.ime.usp.br/~giapaula/textoregressao.htm
