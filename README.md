# Manipulador de Imagens BMP

## Execução
Para executar o programa, digite na linha de comando
```
python3 app.py < 'arquivo_com_comandos'
```
Quase um arquivo de comandos não seja passado, você ainda podera digitar digitar os comandos um por um no modo interativo. O Arquivo 'example.txt' possui alguns comandos básicos e pode ser usado como um arquivo de comandos.

## Comandos
  * I M N: Cria uma nova matriz com M linhas e N colunas. Todos os pixels são brancos (0, 0, 0).
  * C: Limpa a matriz. O tamanho permanece o mesmo.
  * L X Y C: Colore um pixel na linha X e coluna Y na cor C.
  * V X Y1 Y2 C: Desenha um segmento vertical na coluna X nas linhas de Y1 a Y2 (intervalo
inclusivo) na cor C.
  * H X1 X2 Y C: Desenha um segmento horizontal na linha Y nas colunas de X1 a X2 (intervalo
inclusivo) na cor C.
 * K X1 Y1 X2 Y2 C: Desenha um retangulo de cor C. (X1,Y1) é o canto superior esquerdo e (
 X2,Y2) o canto inferior direito.
 * F X Y C: Preenche a região com a cor C. A região R é definida da seguinte forma:
O pixel (X,Y) pertence à região. Outro pixel pertence à região, se e somente se,
ele tiver a mesma cor que o pixel (X,Y) e tiver pelo menos um lado em comum com
um pixel pertencente à região.
 * S name: Escreve a imagem em um arquivo de nome name.
 * X: Encerra o programa.

## Restrições
 * Os valores das cordenadas devem estar entre 0 o número de linhas/colunas da matriz - 1.
 * Os valores das cores deve ser passado sem parenteses e sem virgula. Por exemplo, se a cor em questão for (255, 255, 255), éla deverá ser passada como 255 255 255

## Testes
Para executar os testes, basta digitar na linha de comando:
```
python3 -m unittest discover tests/
```