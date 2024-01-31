2. **Diferenciação Numérica**
=============================

2.1. **Motivação** 
------------------

Em diversos cenários somos capazes de derivar funções analiticamente para entender seu comportamento. 
No entanto, na prática encontramos situações onde a função não é conhecida, e o que temos são conjuntos de pontos discretos, a função não é diferenciável 
em algum ponto, por exemplo, ou a sua derivada não é trivial.
É aqui que as derivadas numéricas nos auxiliam, servindo como uma ferramenta para aproximar numericamente a derivada 
de uma função quando não podemos determiná-la analiticamente.

As derivadas numéricas são baseadas na ideia de aproximar a inclinação de uma função em um ponto usando os valores da função em pontos próximos. 
Em vez de considerar o limite de uma taxa de variação conforme a diferença entre os pontos se aproxima de zero (o que fizemos no capítulo anterior), 
usamos uma diferença finita para estimar essa taxa.

Existem vários métodos para realizar a diferenciação numérica, cada um com suas vantagens e limitações. As técnicas mais comuns incluem a diferença para 
a frente(avançada), a diferença para trás(atrasada), a diferença central e técnicas um pouco mais avançadas como a extrapolação de Richardson. A escolha do método e o tamanho
do passo de diferenciação, ou o intervalo entre os pontos de dados usados, são parâmetros críticos e influenciam na precisão do resultado estimado.

Além disso, duas fontes principais de erro são intrínsecas à diferenciação numérica: o erro de aproximação(ou truncamento), que surge da própria 
aproximação da derivada, e o erro de arredondamento, que resulta das limitações(números de dígitos significativos) de cada máquina. 
O equilíbrio entre esses erros apresenta um papel importante na determinação de um passo ótimo para a diferenciação numérica.

À medida que avançamos para um estudo mais detalhado da diferenciação numérica vamos explorar esses métodos, aprender a otimizar os erros e aplicar 
essas técnicas.


2.2. **Diferença Finita**
-------------------------

A técnica de diferença finita é amplamente utilizada para aproximar a derivada de uma função quando a abordagem analítica é impraticável 
ou impossível. Ao invés de depender de incrementos infinitesimais, que são conceituais e não computacionalmente viáveis, a diferença finita 
utiliza incrementos finitos para calcular uma aproximação da taxa de variação.

.. admonition:: Passo 

    O "passo", denotado por :math:`h`, é a distância entre os pontos no domínio da função usados para calcular a derivada. Na diferenciação analítica, 
    a derivada :math:`f'(x)` é definida como o limite quando :math:`h` tende a zero, da seguinte forma:

    .. math::

        \begin{align}
        &f'(x) = \displaystyle \lim_{h \to 0}\frac{f(x+h)-f(x)}{h} \tag{38} \\ \\
        \end{align}

    No contexto da diferença finita, :math:`h` é um valor finito positivo que escolhemos com base em um compromisso entre precisão e estabilidade numérica. Um 
    :math:`h` muito pequeno pode aumentar o erro de arredondamento devido à precisão finita dos cálculos computacionais, enquanto um :math:`h` muito grande pode 
    aumentar o erro de truncamento da nossa aproximação. O objetivo é utilizar um :math:`h` que minimize o erro total.
    


.. admonition:: Erro total 

    Quando aplicamos métodos numéricos, como a diferenciação por diferenças finitas, é crucial entender que os resultados são aproximações e, como tais, 
    estão sujeitos a erros. Esses erros podem ser categorizados e analisados para melhorar a precisão das nossas aproximações.
    
    **1. Erro de truncamento**

    O erro de aproximação, ou erro de truncamento, ocorre quando uma série infinita é substituída por uma soma finita. Na diferenciação numérica, 
    isso acontece quando expressamos a derivada usando diferenças finitas. Por exemplo, a expressão da diferença finita avançada é uma aproximação que 
    pode ser expressa como:

    .. math::
        
        \begin{align}
        &f'(x) \approx \frac{f(x+h)-f(x)}{h} + O(h) \tag{39} \\ \\
        \end{align}
    

    A notação :math:`O(h)` representa os termos de erro de ordem superior que são negligenciados na aproximação. 
    Geralmente, estes termos são proporcionais a potências mais altas de :math:`h` , como :math:`O(h) = Ah + \frac{Ah^2}{2} + \frac{Ah^2}{3} + \frac{Ah^2}{4} + ...`

    À medida que :math:`h` se torna menor, espera-se que o erro de truncamento também diminua. No entanto, deve-se ter cuidado com o erro de arredondamento, 
    que pode se tornar significativo para valores muito pequenos de :math:`h`.


    **2. Erro de arredondamento**

    Este erro é o resultado das limitações na precisão com que os números são representados e calculados em computadores. Devido à precisão finita, quando as
    operações  são realizadas, os resultados muitas vezes precisam ser arredondados, introduzindo pequenos erros. Estes erros podem se acumular 
    ao longo de cálculos repetidos e se tornar significativos. Interessantemente, se :math:`h` for escolhido muito pequeno na tentativa de reduzir o erro de truncamento
    , o erro de arredondamento pode se tornar dominante, anulando os benefícios de um :math:`h` menor. Por exemplo, em cálculos de 
    diferenciação numérica, um :math:`h` excessivamente pequeno pode levar a uma perda de dígitos significativos, onde a subtração de dois números quase 
    iguais resulta em um erro de arredondamento maior.

    **3. Erro total**

    Podemos então dizer que o erro total relacionado a diferenças finitas vai ser dado por:

    .. math:: 

        \begin{align}
        &\displaystyle E_{total} = E_{aprox} + E_{arred} \tag{40} \\ \\
        \end{align}
    
    As expressões para os erros de truncamento e arredondamento serão apresentadas nas subseções abaixo. Os erros relacionados ao truncamento variam conforme mudamos
    o método de diferença finita, enquanto o erro de arredondamento não se altera.

2.2.1. **Método da Diferença Avançada e Atrasada**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Os métodos apresentados abaixo podem ser chamados de métodos de diferenças não centrais, uma vez que são métodos em que se estima o limite um passo a frente(avançada)
ou atrás(atrasado).



.. admonition:: Diferença Avançada

    O método da diferença avançada, como o nome sugere, consiste em utilizarmos um ponto avançado ao calcularmos nosso limite. Em outras palavras:

    .. math::

        \begin{align}
        &\frac{d}{dx}f(x)\bigg|_{x_{0^{+}}}= \displaystyle \lim_{h \to 0}\frac{f(x_{0}+h)-f(x_{0})}{h} \tag{41} \\ \\
        \end{align}

    A imagem abaixo ilustra a intuição da diferença avançada.

    .. figure:: images/image_9.png
        
        Figura 9     
    
    Como não podemos utilizar :math:`h = 0` (uma vez que nos resultaria em uma divisão por zero), podemos simplesmente dizer que :math:`h` é um número tão pequeno o quanto quisermos, de modo que o limite apresentado se torna uma aproximação. 
    Mas qual seria um valor ideal para :math:`h` ?

    Não possuímos uma expressão analítica que envolva os erros e o parâmetro :math:`h`, contudo, podemos encontrar tal expressão.
 
    Vamos começar utilizando a expansão em série de Taylor de :math:`f(x_{0}+h)` em torno de :math:`x_0` ,para de fato entendermos como :math:`h` 
    se comporta em função dos erros associados.

    .. math::

        \begin{align}
        &f(x_{0}+h) = f(x_{0}) + hf'(x_{0}) + \frac{h^{2}}{2}f''(x_{0}) + \frac{h^{3}}{6}f'''(x_{0}) + ...  \tag{42} \\ \\
        \end{align}

    Podemos isolar :math:`f'(x_{0})` e rearranjar a expressão

    .. math::

        \begin{align}
        &f(x_{0})' = \frac{f(x_{0}+h)-f(x_{0})}{h} - \frac{h}{2}f''(x_{0}) - \frac{h^{2}}{6}f'''(x_{0}) + ... \tag{43} \\ \\
        \end{align}

    Vamos então fazer uma aproximação de primeira ordem para :math:`O(h)`

    .. math::

        \begin{align}
        &f(x_{0})' \approx \frac{f(x_{0}+h)-f(x_{0})}{h} + O(h) \tag{44} \\ \\
        \end{align}

    Ou seja, o erro de primeira ordem O(h) para a diferença avançada, é

    .. math::

        \begin{align}
        &E_{aprox} = O(h) \approx - \frac{h}{2}f''(x_{0}) \tag{45}\\ \\
        \end{align}





Faremos o mesmo processo para o método da diferença atrasada, discutiremos o erro de arredondamento para ambos os casos e então encontraremos um erro total que irá nos indicar
valores ótimos para :math:`h` .



.. admonition:: Diferença Atrasada

    O método da diferença atrasada, como o nome sugere, consiste em utilizarmos um ponto atrasado ao calcularmos nosso limite. Em outras palavras:

    .. math::

        \begin{align}
        &\frac{d}{dx}f(x)\bigg|_{x_{0^{-}}}= \displaystyle \lim_{h \to 0}\frac{f(x_{0})-f(x_{0} - h)}{h} \tag{46} \\ \\
        \end{align}
    
    A imagem abaixo ilustra a intuição da diferença atrasada.


    .. figure:: images/image_10.png
        
        Figura 10 
    
    Como não podemos utilizar :math:`h = 0`, podemos simplesmente dizer que :math:`h` é um número tão pequeno o quanto quisermos de modo que o limite se torna uma aproximação.

    Não possuímos uma expressão analítica que envolva os erros e o parâmetro :math:`h`, contudo, podemos encontrar tal expressão.
 
    Vamos começar utilizando a expansão em série de Taylor de :math:`f(x_{0}-h)` em torno de :math:`x_0` ,para de fato entendermos como :math:`h` 
    se comporta em função dos erros associados.

    .. math::

        \begin{align}
        &f(x_{0}-h) = f(x_{0}) - hf'(x_{0}) + \frac{h^{2}}{2}f''(x_{0}) - \frac{h^{3}}{6}f'''(x_{0}) + ... \tag{47} \\ \\
        \end{align}
    
    Podemos isolar :math:`f'(x_{0})` e rearranjar a expressão:

    .. math::

        \begin{align}
        &f(x_{0})' = \frac{f(x_{0})-f(x_{0}-h)}{h} + \frac{h}{2}f''(x_{0}) - \frac{h^{2}}{6}f'''(x_{0}) + ... \tag{48} \\ \\
        \end{align}
    
    Vamos então fazer uma aproximação de primeira ordem para :math:`O(h)`
    
    .. math::

        \begin{align}
        &f(x_{0})' \approx \frac{f(x_{0}-h)-f(x_{0})}{h}  + O(h) \tag{49} \\ \\
        \end{align}
    
    Ou seja, o erro de primeira ordem :math:`O(h)` para a diferença atrasada, é

    .. math::

        \begin{align}
        &E_{aprox} = O(h) \approx  \frac{h}{2}f''(x_{0}) \tag{50} \\ \\
        \end{align}


**[Este quadro de diferença atrasada ficou muito repetitivo. Parece um copia e cola e dá uma sensação de deja vu ruim para o leitor. Tente dar uma quebrada nisso. Por exemplo, dizendo algo: da mesma forma como na diferença adiantada, podemos expandir em série de Taylor que resulta em ... e pular o passo intermediário que é idêntico.]**

É importante notar que a aproximação de primeira ordem dos dois métodos acima possuem um erro de truncamento da ordem de :math:`O(h)\approx \frac{h}{2}f''(x)` .
O resultado acima nos induz a pensar que quanto menor o parâmetro :math:`h` menor o erro associado e, por consequência, o resultado da derivada numérica tende a ser 
mais preciso, contudo, isso só é verdade até certo ponto. Isso ocorre devido ao erro de arredondamento compor o erro total. 
Vamos estimá-lo abaixo para os dois métodos apresentados.

.. admonition:: Arredondamento em diferenças não centrais

    O erro de arredondamento surge devido a sucessivas operações de subtração e divisão envolvidas na aproximação da diferença finita (seja ela avançada ou atrasada). O módulo deste erro é dado por:

    .. math::

        \begin{align}
        &E_{arred} = \frac{2|f(x_0)|\epsilon_{m}}{h} \tag{51} \\ \\
        \end{align}
    
    Onde :math:`\epsilon_{m}` é chamado de erro da máquina e é uma característica do hardware do computador e do software do sistema operacional, e é geralmente o mesmo para qualquer computador 
    e vale cerca de :math:`\epsilon_{m} = 2.220446049250313.10^{-16}` .

    Por fim, o que buscamos é estimar um valor razoável para :math:`h` de modo que o erro de aproximação seja pequeno e o erro de arredondamento também. Podemos dizer então
    que existe um :math:`h` que minimiza o erro total.


**[Em várias partes está faltando indicação de referências, mas no quadro acima em especial por apresentar uma expressão sem demonstração]**

.. admonition:: Minimizando :math:`E_{total}`

    Podemos sintetizar os erros obtidos acima em uma única expressão:

    .. math::

        \begin{align}
        &E_{tot} = E_{aprox} + E_{arred} = \frac{h}{2}f''(x_{0}) + \frac{2|f(x_0)|\epsilon_{m}}{h} \tag{52} \\ \\
        \end{align}
    
    Mas o que buscamos de fato é um valor de :math:`h` que minimiza o erro total. Podemos então derivar a expressão de :math:`E_{tot}` em relação ao parâmetro :math:`h`
    e a igualarmos a zero, da seguinte forma:

    .. math::

        \begin{align}
        &\frac{d}{dh}E_{tot} = \frac{d}{dh}\left[\frac{h}{2}f''(x_{0})\right] + \frac{d}{dh}\left[\frac{2|f(x_0)|\epsilon_{m}}{h}\right] = 0 \tag{53} \\ \\
        \end{align}

    Logo, obtemos que

    .. math::

        \begin{align}
        &\frac{d}{dh}\left[\frac{h}{2}f''(x_{0})\right] = - \frac{d}{dh}\left[\frac{2|f(x_0)|\epsilon_{m}}{h}\right] \tag{54} \\ \\
        \end{align}

    Ao aplicarmos a derivada em relação a :math:`h` ,iremos obter um :math:`h_{ótimo}` que minimiza o erro total

    .. math::

        \begin{align}
        &\frac{1}{2}|f''(x_0)| = \frac{2f(x_0)\epsilon_{m}}{h_{ótimo}^{2}} \tag{55} \\ \\
        \end{align}
    
    Isolando :math:`h_{ótimo}` , obtemos que 

    .. math::

        \begin{align}
        &h_{ótimo} = \sqrt{4\epsilon{m}\frac{|f(x)|}{|f''(x)|}} \tag{56} \\ \\
        \end{align}
    
    Logo, podemos substituir o valor de :math:`h_{ótimo}` na equação do :math:`E_{total}` e obter o :math:`E_{ótimo}` , da seguinte forma:

    .. math::

        \begin{align}
        &E_{ótimo} = \frac{h_{ótimo}}{2}|f''(x)| + \frac{2|f(x)|\epsilon_{m}}{h_{ótimo}} \tag{57} \\ \\ 
        &E_{ótimo} = \sqrt{4\epsilon_{m}|f(x)||f''(x)|} \tag{58} \\ \\
        \end{align}

    Que é a expressão que minimiza o erro total na diferença avançada ou atrasada.

    Você deve se perguntar: Bom, temos os valores de :math:`h_{ótimo}` e :math:`E_{ótimo}` , mas e agora? O que 
    faremos com estes valores?

    A resposta é simples. Vamos "chutar" ordens de grandeza para :math:`f(x)` e :math:`f''(x)` de modo que iremos encontrar estimativas para :math:`h_{ótimo}` e :math:`E_{ótimo}` 
    tal que, quando de fato utilizarmos o método para calcular a derivada numérica por diferença finita, tenhamos de fato um ponto de partida para estes parâmetros.

    Surge a seguinte dúvida: Mas porque precisamos deste ponto de partida? 

    Como foi apresentado, os métodos de diferença avançada e atrasada não possuem uma variação linear para  :math:`h_{ótimo}` e :math:`E_{ótimo}` , na maioria das aplicações nós chutamos valores para estes 
    parâmetros e observamos o comportamento do erro total. O objetivo aqui é mostrar que conhecendo :math:`f(x)` e :math:`f''(x)` podemos estimar estes parâmetros. A maioria das bibliotecas de diferenças finitas  
    disponíveis em Python utilizam um valor padrão para o parâmetro :math:`h` e não estão tão preocupadas com a precisão numérica.

    Por fim, se estimarmos que :math:`f(x)` e :math:`f''(x)` tem ordem :math:`1` , podemos dizer que:

    .. math::

        \begin{align}
        &h_{ótimo} = \sqrt{4\epsilon_{m}} = 10^{-8} \tag{59}\\ \\
        &E_{ótimo} = \sqrt{4\epsilon_{m}} = 10^{-8} \tag{60}\\ \\
        \end{align}

    Abaixo faremos uma estimativa no cálculo da derivada numérica de uma função com base nos resultados obtidos acima.

.. admonition:: Aplicação Diferença Avançada 

    Dada a função :math:`f(x) = x^{2}e^{(sen(2x)cos(2x))}` calcule sua derivada no ponto :math:`x = 2` .

    Primeiro vamos encontrar a derivada analítica da função acima. Para isso podemos utilizar as técnicas de derivação ou podemos utilizar a biblioteca Sympy e derivar simbolicamente.

    Utilizando a biblioteca Sympy:

    Entrada:

    .. code::

        from sympy import symbols, diff, sin, exp, cos

        # Define a variável simbólica
        x = symbols('x')

        # Define as funções
        f1 = x*x*exp(sin(2*x)*cos(2*x))


        # Calcula as derivadas
        df1 = diff(f1, x)

        # Avalia a derivada no ponto x = 2
        df1_at_2 = df1.subs(x, 2)

        # Mostra os resultados
        print(f"f'(x) = {df1}")
        print(f"f'(2) = {df1_at_2.evalf()}")



    Saída:

    .. figure:: images/image_11.png
        
        Figura 11 

    Agora vamos calcular a derivada numérica utilizando o método da diferença avançada. Iremos utilizar o resultado de que :math:`h_{ótimo} = \sqrt{4\epsilon_{m}} = 10^{-8}` .

    Entrada:

    .. code::

        import numpy as np

        # Define a função e sua derivada analítica
        def f(x):
            return x*x*np.exp(np.sin(2*x)*np.cos(2*x))

        def df_analytic(x):
            return x**2*(-2*np.sin(2*x)**2 + 2*np.cos(2*x)**2)*np.exp(np.sin(2*x)*np.cos(2*x)) + 2*x*np.exp(np.sin(2*x)*np.cos(2*x))

        # Ponto de interesse e valor de h
        x0 = 2
        h = 1e-8

        # Calcula a derivada usando a diferença avançada
        df_forward = (f(x0 + h) - f(x0)) / h

        # Calcula o resultado da derivada analítica
        df_analytic_result = df_analytic(x0)


        # Mostra o resultado da derivada aproximada
        print(f"f'({x0}) aproximado = {df_forward}")

        # Mostra o resultado da derivada analítica
        print(f"f'({x0}) analítico = {df_analytic_result}")

        # Calcula e mostra o erro absoluto
        erro = abs(df_forward - df_analytic_result)
        print(f"Erro absoluto = {erro}")

    
    Saída:

    .. figure:: images/image_12.png
        
        Figura 12 
      

    É importante notar que o valor esperado para o erro era da ordem de :math:`10^{-8}` para um valor de :math:`h_{ótimo} = 10^{-8}` . O erro absoluto encontrado foi da ordem de 
    :math:`10^{-7}` nos indicando que os chutes para :math:`f(x)` e :math:`f''(x)` não foram precisos, contudo, o erro encontrado está relativamente próximo da estimativa feita, nos dando
    um indício positivo em relação a teoria apresentada até então.


A depender do tipo de precisão que sua aplicação exigir, um erro absoluto da ordem de :math:`10^{-7}` não é algo tão bom quanto parece. Afim de melhoramos isso, 
iremos apresentar abaixo o método da diferença central, que traz em sua proposição a ideia de se utilizar um valor médio para o cálculo numérico da derivada.

2.2.3. **Método da Diferença Central**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

O método apresentado abaixo pode ser chamado de método da diferença central, uma vez que estamos tratando de um método 
em que se estima o limite um passo a frente de  :math:`h` e em um passo atrás de :math:`h` .
Em outras palavras, esta técnica é a combinação do método da diferença avançada com o método da diferença atrasada que foram demonstradas na subseção acima.



.. admonition:: Diferença Central

    O método da diferença central, consiste em se tirar a média aritmética de duas diferenças finitas, a avançada e a atrasada. Sabemos que a diferença avançada pode ser escrita como:


    .. math::

        \begin{align}
        &\frac{d}{dx}f(x)\bigg|_{x_{0^{+}}}= \displaystyle \lim_{h \to 0}\frac{f(x_{0}+h)-f(x_{0})}{h} \tag{61} \\ \\
        \end{align}

    E a diferença atrasada pode ser expressa da seguinte maneira:   

    .. math::
        
        \begin{align}
        &\frac{d}{dx}f(x)\bigg|_{x_{0^{-}}} = \displaystyle \lim_{h \to 0}\frac{f(x_{0})-f(x_{0}-h)}{h} \tag{62} \\ \\
        \end{align}
    
    Podemos tirar a média dos dois métodos e definir a diferença central da seguinte forma:

    .. math::


        \begin{align}
        &\frac{d}{dx}f(x)\bigg|_{x_{0^{\pm}}} = \frac{1}{2}\left[\frac{d}{dx}f(x)\bigg|_{x_{0^{+}}} + \frac{d}{dx}f(x)\bigg|_{x_{0^{-}}}\right]=  \displaystyle \frac{1}{2} \displaystyle \lim_{h \to 0}\frac{f(x_{0}+h)-f(x_{0})}{h} + \lim_{h \to 0}\frac{f(x_{0})-f(x_{0}-h)}{h} \\ \\
        &\frac{d}{dx}f(x)\bigg|_{x_{0^{\pm}}} = \displaystyle \frac{1}{2} \displaystyle \lim_{h \to 0}\frac{f(x_{0}+h)-f(x_{0}) + f(x_{0})-f(x_{0}-h)}{h}  \\ \\
        &\frac{d}{dx}f(x)\bigg|_{x_{0^{\pm}}} = \displaystyle \lim_{h \to 0}\frac{f(x_{0}+h)-f(x_{0}-h)}{2h} \tag{63}  \\ \\
        \end{align}
    
    A imagem abaixo ilustra a intuição da diferença central.

    .. figure:: images/image_13.png
        
        Figura 13 
    
    Como já discutido anteriormente, não podemos utilizar :math:`h = 0` (com isso podemos tomar uma aproximação para o limite) e também 
    não possuímos uma expressão analítica que envolva os erros e o parâmetro :math:`h` , vamos adotar a mesma estratégia anterior e deduzir as expressões.
 
    Vamos começar utilizando a expansão em série de Taylor para :math:`f(x_{0}+h)` em torno de :math:`x_0` e 
    para :math:`f(x_{0}-h)` em torno de :math:`x_0`  para para de fato entendermos 
    como :math:`h` se comporta em função dos erros associados.

    .. math::

        \begin{align}
        &f(x_{0}+h) = f(x_{0}) + hf'(x_{0}) + \frac{h^{2}}{2}f''(x_{0}) + \frac{h^{3}}{6}f'''(x_{0}) + ... \\ \\
        &f(x_{0}-h) = f(x_{0}) - hf'(x_{0}) + \frac{h^{2}}{2}f''(x_{0}) - \frac{h^{3}}{6}f'''(x_{0}) + ... \\ \\
        \end{align}

    Ao observarmos as equações acima, podemos notar que ao subtrairmos uma da outra, podemos encontrar um padrão interessantemente
    uma vez que os termos de derivadas pares se cancelam. Vamos subtrair :math:`f(x_{0}+h)` de :math:`f(x_{0}-h)` da seguinte forma:

    .. math::

        \begin{align}
        &f(x_{0}+h) - f(x_{0}-h) =  2hf'(x_{0}) + f'''(x_{0})\frac{h^{3}}{6} + ...  \\ \\
        \end{align}

    
    Vamos isolar :math:`f'(x_{0})` e rearranjar a expressão acima:

    .. math::

        \begin{align}
        &f'(x_{0}) = \frac{f(x_{0}+h)-f(x_{0}-h)}{2h} + O(h^{2}) \tag{64} \\ \\
        \end{align}
    
    Logo, podemos dizer que o erro de aproximação de primeira ordem é igual a:

    .. math::

        \begin{align}
        &E_{aprox} = O(h^{2}) \approx -f'''(x_{0})\frac{h^{2}}{12} \tag{65}\\ \\
        \end{align}

É importante notar que a aproximação de primeira ordem da diferença central possui um erro de aproximação da ordem de :math:`O(h^{2}) \approx -f'''(x_{0})\frac{h^{2}}{12}` .
Como discutido nas subseções acima, o erro de arredondamento também possui sua componente no cálculo do erro total e não deve ser desprezado.
Vamos estimá-lo abaixo para o método da diferença central.

.. admonition:: Arredondamento em diferenças centrais

    O erro de arredondamento surge devido a sucessivas operações de subtração e divisão envolvidas na aproximação da diferença finita (seja ela avançada, atrasada ou central). O módulo deste erro é dado por:

    .. math::

        \begin{align}
        &E_{arred} = \frac{2|f(x_0)|\epsilon_{m}}{h} \tag{66} \\ \\
        \end{align}
    

    Por fim, o que buscamos é estimar um valor razoável para :math:`h` de modo que o erro de aproximação seja pequeno e o erro de arredondamento também. Podemos dizer então
    que existe um :math:`h` que minimiza o erro total.

**[Esse quadro de cima também é idêntico ao da diferença avançada. Então é bo mdar uma qubrada nisso. Por exemplo, mencionando "da mesma forma que na equação x" ou simplesmente mencionando que a mesma equação se aplica na diferença central sem precisar criar um quadro só para isso.]**

.. admonition:: Minimizando :math:`E_{total}`

    Podemos sintetizar os erros obtidos acima em uma única expressão:

    .. math::

        \begin{align}
        &E_{tot} = E_{aprox} + E_{arred} = \frac{h^{2}}{12}f'''(x_{0}) + \frac{2|f(x_0)|\epsilon_{m}}{h} \tag{67} \\ \\
        \end{align}
    
    Mas o que buscamos de fato é um valor de :math:`h` que minimiza o erro total. Ao derivarmos a expressão do erro total em relação a :math:`h` igual a zero, seguirmos o mesmo caminho algébrico dos outros métodos apresentados acima e assumirmos que :math:`f(x)` e :math:`f'''(x)` são de ordem 1,
    obtemos a seguinte expressão para :math:`h_{ótimo}` e :math:`E_{ótimo}` :

    .. math::


        \begin{align}
        &h_{ótimo} = (12\epsilon_{m})^{1/3} \approx 10^{-5} \tag{67} \\ \\
        &E_{ótimo} = \left(\frac{9}{16}\epsilon_{m}^{2}\right)^{1/3} \approx 10^{-11} \tag{68} \\ \\
        \end{align}

    Que ao compararmos com o resultado da diferença avançada, de fato se mostra um resultado mais preciso e ainda mais: um resultado em que o passo :math:`h` pode ser maior, ou seja, 
    o custo computacional (tempo gasto pelo computador ao executar um programa) será menor uma vez que o valor do passo é maior.

    A tabela abaixo sintetiza os resultados.

    .. list-table::
        :widths: 45 45

        * - Diferença avançada/atrasada
          - Diferença central
        * - :math:`h_{ótimo} \approx 10^{-8}`
          - :math:`h_{ótimo} \approx 10^{-5}`
        * - :math:`E_{ótimo} \approx 10^{-8}`
          - :math:`E_{ótimo} \approx 10^{-11}`


Podemos resolver a aplicação que resolvemos anteriormente com o método da diferença central e comparar os resultados.

.. admonition:: Aplicação Diferença Central

    Dada a função :math:`f(x) = x^{2}e^{(sen(2x)cos(2x))}` calcule sua derivada no ponto :math:`x = 2` .

    Primeiro vamos encontrar a derivada analítica da função acima. Para isso, podemos utilizar as técnicas de derivação ou podemos utilizar a biblioteca Sympy e derivar simbolicamente.
    Logo depois podemos utilizar a técnica da diferença central e comparar os resultados através do erro absoluto.

    Utilizando a biblioteca Sympy:

    Entrada:

    .. code::

        import numpy as np

        # Define a função e sua derivada analítica
        def f(x):
            return x*x*np.exp(np.sin(2*x)*np.cos(2*x))

        def df_analytic(x):
            return x**2*(-2*np.sin(2*x)**2 + 2*np.cos(2*x)**2)*np.exp(np.sin(2*x)*np.cos(2*x)) + 2*x*np.exp(np.sin(2*x)*np.cos(2*x))

        # Ponto de interesse e valor de h
        x0 = 2
        h = 1e-5

        # Calcula a derivada usando a diferença central
        df_central = (f(x0 + h) - f(x0 - h)) / (2 * h)

        # Calcula o resultado da derivada analítica
        df_analytic_result = df_analytic(x0)

        # Mostra o resultado da derivada aproximada
        print(f"f'({x0}) aproximado = {df_central}")

        # Mostra o resultado da derivada analítica
        print(f"f'({x0}) analítico = {df_analytic_result}")

        # Calcula e mostra o erro absoluto
        erro = abs(df_central - df_analytic_result)
        print(f"Erro absoluto = {erro}")

    
    Saída:

    .. figure:: images/image_14.png
        
        Figura 14 
      


    É importante notar que o valor esperado para o erro era da ordem de :math:`10^{-11}` para um valor de :math:`h_{ótimo} = 10^{-5}` e isso não ocorreu exatamente como o esperado.
    Muito se deve a estimativa que fizemos de :math:`f'''(x)` e :math:`f(x)` . Contudo, o valor do erro encontrado não está longe :math:`10^{-9}` nos mostrando
    que a teoria se alinha com os resultados obtidos frente as estimativas que fizemos.

Por fim, podemos comparar os resultados através da imagem abaixo. O gráfico apresentado advém de um algoritmo em Python que percorre os valores
de :math:`h = 10^{-18}` até :math:`h = 1` e os erros são plotados em função de :math:`h` para a derivada da função :math:`f(x) = x^{2}e^{(sen(2x)cos(2x))}` no ponto :math:`x = 2`
para o método da diferença central e avançada.

Entrada:

.. code::

        import numpy as np
        import matplotlib.pyplot as plt

        # Define a função e sua derivada analítica
        def f(x):
            return x*x*np.exp(np.sin(2*x)*np.cos(2*x))

        def df_analytic(x):
            return x**2*(-2*np.sin(2*x)**2 + 2*np.cos(2*x)**2)*np.exp(np.sin(2*x)*np.cos(2*x)) + 2*x*np.exp(np.sin(2*x)*np.cos(2*x))

        # Ponto de interesse
        x0 = 2

        # Valores de h
        h_values = np.logspace(-18, 0, 15)

        # Listas para armazenar erros
        errors_forward = []
        errors_central = []

        # Calcula as derivadas e erros para cada h
        for h in h_values:
            df_forward = (f(x0 + h) - f(x0)) / h
            df_central = (f(x0 + h) - f(x0 - h)) / (2 * h)
            errors_forward.append(abs(df_forward - df_analytic(x0)))
            errors_central.append(abs(df_central - df_analytic(x0)))

        # Plotando o gráfico
        plt.loglog(h_values, errors_forward, label='Erro Diferença Avançada')
        plt.loglog(h_values, errors_central, label='Erro Diferença Central')
        plt.xlabel('h')
        plt.ylabel('Erro Absoluto')
        plt.title('Erro Absoluto da Derivada Numérica em Função de h')
        plt.legend()
        plt.show()

Saída:

    .. figure:: images/image_15.png
        
        Figura 15


É importante analisarmos que o erro cai quase que linearmente com :math:`h` até certo ponto. **[Não sei se dá para afirmar que o gráfico apresenta comportamento linear, pois você está usando uma escala dilog.]** Essa diminuição se da devido ao erro de aproximação que é diretamente proporcional a :math:`h`.
A partir deste valor mínimo do erro, o mesmo começa a subir devido a contribuição do erro de arredondamento que é inversamente proporcional ao parâmetro :math:`h` .


Mais uma vez, a depender da sua aplicação, o valor do erro ser aceitável ou não vai depender do rigor numérico que você busca em seus resultados. 
Você pode seguir o mesmo caminho algébrico apresentado nesta seção e encontrar erros de ordens superiores simplesmente truncando a série infinita proveniente da expansão em série de Taylor nos próximos termos. 
Isso vai nos fornecer erros menores, contudo o custo computacional vai aumentar significativamente. Um caminho algébrico similar pode ser adotado para o cálculo numérico de derivadas de segunda ou terceira ordem.

Por fim, podemos discutir o método de pontos em uma grade, que leva em consideração o cenário em que não temos a função :math:`f(x)` para calcularmos sua derivada, o que temos 
são apenas conjuntos de pontos :math:`(x_{i}, y_{i})` onde :math:`y_{i}` é o valor da função no ponto :math:`x_{i}` .



2.3. **Pontos em uma grade**
----------------------------

Em cenários experimentais, muitas vezes não possuímos expressões do tipo :math:`f(x)` a nossa disposição para calcularmos a sua derivada em um ponto específico. O que de fato possuímos
são os chamados pontos em uma grade (ou malha -- quando estes pontos são igualmente espaçados) -- que são essencialmente dados discretos do tipo :math:`(x_{i}, y_{i})` onde :math:`y_{i}` é o valor da função no ponto :math:`x_{i}` .


.. admonition:: Grade igualmente espaçada 

    Quando esta grade é igualmente espaçada, podemos definir nosso domínio como 

    .. math::

        \begin{align}
        &x_{i} = x_{0} + ih \tag{69} \\ \\
        \end{align}
    
    Onde :math:`h=\frac{x_{f}-x_{0}}{n-1}` e :math:`x_{i}` é o seu domínio,  :math:`x_{0}` é seu ponto inicial,  :math:`x_{f}` é seu ponto final,  :math:`i` é um número inteiro que vai de 
    :math:`0` até :math:`n-1` ,  :math:`h` é o passo e  :math:`n` é o número total de pontos disponíveis.

    Já os pontos relacionados à imagem da função, são os pontos discretos obtidos na sua aplicação (seja ela experimental ou não).

    Vamos demonstrar um exemplo para fixarmos o conceito. 

    Imagine que realizamos diversas medidas em um laboratório e obtivemos os seguintes dados:
 
    .. list-table::
        :widths: 45 45

        * - :math:`y_i`
          - :math:`x_i`
        * - :math:`y_1 = -0.9905465359667132`
          - :math:`x_1 = 4.85`
        * - :math:`y_2 = -0.9824526126243325`
          - :math:`x_2 = 4.90`
        * - :math:`y_3 = -0.9719030694018208`
          - :math:`x_3 = 4.95`
        * - :math:`y_4 = -0.9589242746631385`
          - :math:`x_4 = 5.00` 
  

    Ou seja, nossos pontos estão discretizados da seguinte maneira: :math:`n = 4` ,  :math:`x_{0} = 4.85` e :math:`x_{f} = 5` , ou seja, temos 4 pontos dispostos de 4.85 até 5. Para encontrarmos nosso passo :math:`h` precisamos utilizar a expressão
    que foi apresentada acima. Perceba que diferentemente das técnicas apresentadas nesta seção, agora, o passo :math:`h` é variável e depende de como nossos pontos são apresentados.

    Podemos calcular :math:`h` da seguinte forma 

    .. math::

        \begin{align}
        &h=\frac{x_{f}-x_{0}}{n-1} \\ \\
        &h = \frac{5-4.85}{4-1} = 0.05 \\ \\
        \end{align}
    
    Nosso objetivo é calcular a primeira derivada de :math:`f(x)` no ponto  :math:`f(4.90)` onde :math:`f(x)` não é fornecida explicitamente, apenas seus pontos discretizados.

    Os métodos da diferença avançada, atrasada e central suprem nossas necessidades neste caso. Podemos simplesmente utilizar algum destes métodos para estimar a derivada no ponto 
    específico, com base no ponto anterior, posterior ou central.

.. admonition:: Diferença avançada, atrasada e central em grades

    Podemos simplesmente utilizar as mesmas expressões dos métodos de diferenças finitas utilizados neste capitulo.
    
    **Para a diferença avançada:**

    .. math::

        \begin{align}
        &f(x_{0^{+}})' \approx \frac{f(x_{0}+h)-f(x_{0})}{h} \\ \\
        \end{align}

    Onde o erro total é dado por 

    .. math::

        E_{tot^{+}} = E_{aprox} + E_{arred} = \frac{h}{2}f''(x_{0}) + \frac{2|f(x_0)|\epsilon_{m}}{h}

    **Para a diferença atrasada:**

    .. math::

        \begin{align}
        &f(x_{0^{-}})' \approx \frac{f(x_{0}-h)-f(x_{0})}{h} \\ \\
        \end{align}
    
    Onde o erro total é dado por 

    .. math::

        E_{tot^{-}} = E_{aprox} + E_{arred} = \frac{h}{2}f''(x_{0}) + \frac{2|f(x_0)|\epsilon_{m}}{h}

    **Para a diferença central:**

    .. math::

        \begin{align}
        &f'(x_{0^{\pm}}) = \frac{f(x_{0}+h)-f(x_{0}-h)}{2h}  \\ \\
        \end{align}

    Onde o erro total é dado por

    .. math::

        E_{tot^{\pm}} = E_{aprox} + E_{arred} = \frac{h^{2}}{12}f'''(x_{0}) + \frac{2|f(x_0)|\epsilon_{m}}{h}
    
Podemos estimar o erro total para o exemplo apresentado através das expressões acima.
Como sabemos que :math:`h=0.05` , podemos simplesmente substituir o parâmetro na expressão de cada método e levando em conta que 
:math:`f(x)` , :math:`f'(x)` e :math:`f''(x)` possuem ordem de grandeza igual a um, podemos fazer nossa estimativa para o erro total em cada método discutido.

.. admonition:: Estimativa do erro 

    Para a diferença avançada e atrasada

    .. math::

        \begin{align}
        &E_{tot^{+}} = \frac{h}{2}f''(x_{0}) + \frac{2|f(x_0)|\epsilon_{m}}{h} \approx 10^{-2} \tag{70} \\ \\
        &E_{tot^{-}} = \frac{h}{2}f''(x_{0}) + \frac{2|f(x_0)|\epsilon_{m}}{h} \approx 10^{-2} \tag{71}
        \end{align}
    
    Para a diferença central

    .. math::

        \begin{align}
        &E_{tot^{\pm}} = \frac{h^{2}}{12}f'''(x_{0}) + \frac{2|f(x_0)|\epsilon_{m}}{h} \approx 10^{-5} \tag{72} \\ \\
        \end{align}






.. admonition:: Aplicação de diferenças finitas em grades 

    Afim de resolvermos o exemplo apresentado acima em que queremos calcular :math:`f'(4.90)` onde nossos dados são discretos e estão dispostos no formato abaixo, podemos utilizar 
    dos métodos das diferenças finitas em um ambiente Python. O Script abaixo mostra como se dá a implementação destes métodos no caso em que não possuímos a função explicitamente.

    Dados disponíveis:

    .. list-table::
        :widths: 45 45

        * - :math:`y_i`
          - :math:`x_i`
        * - :math:`y_1 = -0.9905465359667132`
          - :math:`x_1 = 4.85`
        * - :math:`y_2 = -0.9824526126243325`
          - :math:`x_2 = 4.90`
        * - :math:`y_3 = -0.9719030694018208`
          - :math:`x_3 = 4.95`
        * - :math:`y_4 = -0.9589242746631385`
          - :math:`x_4 = 5.00` 

    O código abaixo realiza o cálculo da derivada no ponto :math:`f(4.90)` com base nos pontos fornecidos

    Entrada:

    .. code::

        import numpy as np

        # Pontos dados
        x = [4.85, 4.90, 4.95, 5]
        y = [-0.9905465359667132, -0.9824526126243325, -0.9719030694018208, -0.9589242746631385]

        # Cálculo do passo h
        h = (x[-1] - x[0])/(len(x) - 1)


        # Diferença Avançada
        def diferenca_avancada(x0, x1, y0, y1):

        return (y1 - y0) / h
        

        # Diferença Atrasada
        def diferenca_atrasada(x0, x1, y0, y1):

        return (y0 - y1) / h

        # Diferença Central
        def diferenca_central(x0, x1, y0, y1):

        return (y1 - y0) / (2*h)


        # Estimativas de derivada
        derivada_avancada = diferenca_avancada(x[1], x[2], y[1], y[2])
        derivada_atrasada = diferenca_atrasada(x[1], x[0], y[1], y[0])
        derivada_central = diferenca_central(x[0], x[2], y[0], y[2])

        # Mostra os resultados
        print("Diferença Avançada em f(4.90) = ", derivada_avancada)
        print("Diferença Atrasada em f(4.90) = ", derivada_atrasada)
        print("Diferença Central em f(4.90) = ", derivada_central)
    
    Saída:

    .. figure:: images/image_16.png
        
        Figura 16    
    
    Para fins didáticos e de comparação, os dados relacionados ao eixo :math:`y` foram gerados utilizando-se a função :math:`f(x)=sen(x)` de modo que no final possamos comparar 
    o resultado analítico com o resultado obtido. Repare que na maioria das vezes isso não vai ser possível de ser feito, visto que nem sempre teremos a função em sua forma explícita à nossa disposição.

    Cientes do fato apresentado, podemos calcular o erro absoluto para cada método.

    Podemos diferenciar simbolicamente a função :math:`f(x)=sen(x)` no ponto :math:`x = 4.90` e compararmos os resultados.

    Diferenciando simbolicamente

    Entrada:

    .. code::

        from sympy import symbols, diff, sin

        # Define a variável simbólica
        x = symbols('x')

        # Define a função
        f = sin(x)

        # Calcula a derivada
        df = diff(f, x)

        # Avalia a derivada no ponto x = 4.90
        df_at_490 = df.subs(x, 4.90)

        # Mostra os resultados
        print(f"f'(x) = {df}")
        print(f"f'(4.90) = {df_at_490.evalf()}")
    
    Saída:

    .. figure:: images/image_17.png
        
        Figura 17  
    
    Podemos, por fim, calcular o erro absoluto uma vez que conhecemos a função analítica -- lembre-se que fizemos isso somente para fins didáticos e para mostrarmos que o erro absoluto é da ordem de grandeza do erro total. Em exemplos práticos
    a função não é fornecida e só teremos em mãos os dados discretizados.

    O Script abaixo faz o cálculo do erro absoluto com base nos métodos de diferença finitas em relação a derivada analítica.

    Entrada:

    .. code::

        # Erro absoluto
        erro_abs_avancada = abs(derivada_avancada - 0.186512369422576)
        erro_abs_atrasada = abs(derivada_atrasada - 0.186512369422576)
        erro_abs_central = abs(derivada_central - 0.186512369422576)

        print("Erro absoluto - Diferença Avançada: ", erro_abs_avancada)
        print("Erro absoluto - Diferença Atrasada: ", erro_abs_atrasada)
        print("Erro absoluto - Diferença Central: ", erro_abs_central)

    Saída:

    .. figure:: images/image_18.png
        
        Figura 18 

    Por fim, podemos comparar o erro absoluto com o erro total estimado. A tabela abaixo apresenta estes resultados.

    .. list-table::
        :widths: 45 45

        * - Erro absoluto
          - Erro total estimado
        * - Diferença avançada e atrasada: :math:`E_{abs} \approx 10^{-2}`
          - Diferença avançada e atrasada :math:`E_{tot} \approx 10^{-2}`
        * - Diferença central: :math:`E_{abs}  \approx 10^{-4}`
          - Diferença central: :math:`E_{tot}  \approx 10^{-5}`

    O resultado apresentado acima nos sugere que nossa estimativa é boa, por mais que a diferença de 10x entre o erro absoluto e o total para o método da diferença central esteja evidente. Podemos atribuir
    a esta diferença o fato de assumirmos que :math:`f(x)` e :math:`f'''(x)` possuem ordem de grandeza igual a um.

No segundo capítulo deste material, aprofundamos nosso conhecimento nos fundamentos das diferenças finitas. Exploramos as técnicas de diferença avançada, atrasada e 
central, compreendendo suas aplicações. Além disso, realizamos importantes estimativas a respeito dos erros numéricos, nos mostrando como cada tipo de erro se 
comporta em relação aos cálculos computacionais realizados. 

Ao estudarmos diferenciação numérica, torna-se nítido a relevância desta técnica em diversas aplicações. Ela é uma ferramenta muito útil para aplicações que envolvam o cálculo de derivadas de funções complexas **[novamente, substituir o termo "funções complexas" por outra coisa, exemplo "funções complicadas ou de muitos termos"]** ou de pontos discretos, contudo, precisamos nos atentar para como o erro numérico se comporta em função do custo computacional envolvido.

A capacidade de se estimar derivadas de funções complexas ou desconhecidas, trabalhando com dados discretos e deixando para trás as limitações dos métodos analíticos, nos introduz a uma importante área localizada na fronteira do conhecimento entre a matemática e a computação.
Por fim, no capítulo seguinte, veremos que a diferenciação se torna ainda mais integrada devido aos avanços teóricos computacionais que possibilitaram o desenvolvimento de uma outro técnica, que revolucionou **[eu evitaria termos muito fortes como "revolucionou" e substituiria por algo como "impactou grandemente"]** o cálculo numérico: a diferenciação automática. 
Essencial no universo da computação e aprendizado de máquina, essa técnica nos possibilita calcular derivadas de funções complexas **[a vida é complexa, possui parte real e imaginária (:]** com grande precisão e eficácia, ultrapassando diversos obstáculos encontrados na diferenciação numérica.

Assim, iremos entender **[eu seria mais modesto e substituíria "entender" por "introduzir"]** conceitos como números duais, gradientes numéricos, algoritmos de autodiferenciação e aplicações na area de machine learning.













    






