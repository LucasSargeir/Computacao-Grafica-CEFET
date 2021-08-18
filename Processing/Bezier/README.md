# Curva de Bézier

A curva de Bezier é uma curva plinomial, que é construida através de alguns pontos. Dependendo da quantidade de pontos a curva pode ser: linear, cúbica,  quadrática, etc. Essa curva é muito importante no mundo de computação gráfica, sendo utilizada em diversos programas como Ilustrator, GIMP e Photoshop.

 <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/B%C3%A9zier_3_big.gif/240px-B%C3%A9zier_3_big.gif"/>

 <br/>

### Tecnologia Utilizada
- Python 3.8.
- Processing 3.

<br/>

### Trabalho
A proposta do trabalho foi construir uma curva de Bézier cúbica, baseada na posição do mouse. Como uma cúrva cúbica possui 4 pontos, foi escolhido manter 2 pontos fixos, e através do botão do mouse alterar os outros pontos a serem modificado. Por exemplo:


- Se o botão da esquerda for pressionado, o ponto P1 será alterado;
- Já se o botão da direita for pressionado, o ponto P2 será alterado.

<img src="https://github.com/LucasSargeir/Computacao-Grafica-CEFET/blob/main/imagens/Processing/bezier_01.png" width="35%" height="35%"/>

Através do indicador no canto superior esquerdo é possível saber qual ponto está sendo alterado. Além disso, se o usuário desejar ver as linhas que geram a curva, basta pressionar o botão do meio do mouse, para ativar ou desativar as linhas. Veja:

<img src="https://github.com/LucasSargeir/Computacao-Grafica-CEFET/blob/main/imagens/Processing/bezier_02.png" width="35%" height="35%"/>

