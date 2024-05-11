Resumo do Projeto: Predição de Vagas de Administração com Redes Neurais e Spark
O projeto utiliza dados de vagas de emprego coletados com Scrapy e aplica técnicas de Machine Learning para predizer se uma vaga pertence à área de Administração.
Etapas do projeto:
Coleta de Dados: O código usa o framework Scrapy para extrair informações sobre vagas de emprego de sites como Catho.
Pré-processamento: Os dados coletados são organizados em um DataFrame Pandas e codificados com One-Hot Encoding para representar categorias como "cargo", "empresa", "localização" e "requisitos".
Treinamento do Modelo: Uma rede neural simples é construída com Keras/TensorFlow. O modelo é treinado para identificar padrões nos dados codificados e aprender a classificar vagas como "Administração" ou "Não Administração".
Avaliação e Visualização: A acurácia do modelo é avaliada usando dados de teste. Gráficos comparando as previsões do modelo com os valores reais são gerados com Matplotlib.
Integração com Spark: O projeto integra o Spark para processar os dados de forma distribuída. O DataFrame codificado é carregado no Spark e seu esquema é exibido.
Resultados:
O modelo demonstra alta acurácia na classificação de vagas de Administração. As previsões se aproximam dos valores reais, indicando que a rede neural aprendeu com sucesso a identificar os padrões relevantes nos dados.
Observações:
O código apresenta algumas redundâncias, como a repetição da construção e treinamento do modelo em células diferentes.
A integração com Spark está incompleta, mostrando apenas o carregamento dos dados e a visualização do esquema.
O projeto se concentra na predição de vagas de Administração, mas a metodologia pode ser facilmente adaptada para outras áreas ou para predizer outras características das vagas, como salário.
Próximos passos:
Aprimorar o pré-processamento dos dados para incluir informações mais relevantes e melhorar a qualidade das previsões.
Experimentar com diferentes arquiteturas de redes neurais e hiperparâmetros para otimizar a acurácia do modelo.
Implementar análises mais complexas com Spark para explorar os dados de forma mais abrangente.
Criar uma interface para interagir com o modelo e obter previsões para novas vagas de emprego.
Este projeto demonstra o potencial do uso de Big Data e Machine Learning na análise de dados de vagas de emprego, abrindo caminho para diversas aplicações na área de recrutamento e seleção.
