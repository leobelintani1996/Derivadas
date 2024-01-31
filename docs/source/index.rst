
**Derivadas: do básico ao avançado.**
-------------------------------------

Trabalho de conclusão de curso abordando os temas de derivadas analíticas, numéricas e diferenciação automática.

Autor: Leonardo Cardoso Belintani

Orientador: João Teles de Carvalho Neto

Instituição: UFSCar Araras

Curso: Física Licenciatura

**[Incluir mais referências ao longo do material para dar mais rigor e credibilidade ao texto.]**

**[Fora dos ambientes em Python seria bom usar como separador decimal a vírgula ao invés do ponto, para seguir a norma brasileira. No modo matemático em LaTeX isso pode ser feito com o comando {,} de forma a evitar que automaticamente seja incluída um espaço após a vírgula.]** Exemplo: :math:`0{,}923`

----------------------------------------------------------------------------------------------------

**Motivação inicial**
=====================

O presente trabalho surge no formato de um material didático e **[que tal online e computacional ao invés de didático e interativo? Quem faria um material anti didático? Ressaltar que o material foi desenvolvido em Sphynx e ao clicar em View Source outras pessoas podem usar os mesmos recursos em python e rst como exemplo para outros projetos]** interativo buscando entrelaçar os conhecimentos da matemática, física e computação. 
Um dos objetivos principais do trabalho é fornecer o ferramental teórico necessário para o leitor se aproximar de novas tecnologias e métodos matemáticos 
computacionais, que estão sendo utilizadas nos principais algoritmos de machine learning (aprendizado de máquina) e deep learning (aprendizado profundo) do mundo todo.
O crescimento relacionado à área de machine learning e deep learning muito se deve aos constantes esforços tecnológicos das iniciativas público e privadas 
de diversas esferas da sociedade. Estes esforços não poderiam resultar em algo diferente a não ser um grandioso sucesso dos envolvidos. Podemos atribuir boa parte deste sucesso aos algoritmos de otimização teorizados e implementados, 
e por trás destes algoritmos temos uma peça central e fundamental que faz com que cálculos computacionais sejam realizados de uma forma extremamente rápida e precisa. Algoritmos de machine learning voltados para o estudo de redes neurais artificiais 
por exemplo, buscam minimizar uma função conhecida como custo e esta função é minimizada através de técnicas como o gradiente descendente (utilizado para atualizar os parâmetros de uma rede neural artificial) e a retro propagação (utilizado para retro propagar a função custo), 
por exemplo. Um fator central por trás de todas estas técnicas é a utilização do método da diferenciação automática. Quando buscamos minimizar algo, seja na física, engenharia ou na matemática, estamos falando em derivar uma determinada função e igualarmos o resultado 
a zero. Logo, se temos um algoritmo que busca minimizar a função custo, estamos falando do cálculo de derivadas.
Por fim, este trabalho chega com a proposta de se criar uma base sólida envolvendo um estudo teórico/aplicado sob o escopo do cálculo analítico/simbólico, 
percorrendo temas como limites e derivadas, apresentando recursos computacionais e bibliotecas conhecidas na esfera do cálculo e então um estudo 
teórico a respeito das principais técnicas de diferenças finitas envolvendo as diferenças avançadas, atrasadas e centrais – assim como um entendimento do erro numérico 
associado a estas técnicas, a apresentação da elegante técnica da diferenciação automática incluindo como se dá seu funcionamento e implementação, contabilizando os 
3 pilares da derivação – analítica/simbólica, numérica e automática. Por fim, o material apresentado não busca em sua essência tratar a fundo ou definir conceitos primordiais sobre redes neurais artificiais. O objetivo é aproximar o leitor
o máximo possível do conceito de diferenciação automática e mostrar como as derivadas de fato se relacionam com a área do machine learning.

----------------------------------------------------------------------------------------------------



Sumário
-------
.. toctree::
   :maxdepth: 3

   Parte1
   Parte2
   Parte3
   Parte4

  
   






