# ProcessingPy CLI

O processing disponibiliza no site deles, um pacote para executar os programas no modo Python por linha de comando. Dessa forma, você não fica preso a utilizar a IDE disponibilizada por eles, e consegue uma melhor integração com algumas ferramentas.



### Pre requisitos

- Java 8.



### Download

Para utilizar a versão por linha de comando é necessário fazer o dowload da versão de único arquivo do Processing, no [site](https://py.processing.org/tutorials/command-line/) deles. A versão para Linux 64-Bits está disponível nesse repositório. O arquivo baixado será utilizado para compilar os arquivos `.pyde`.



### Compilação

Para compilar os programas precisaremos executar o `processing-py.jar`, baixado anteriormente, passando o nosso programa como parâmetro. Veja o comando de compilação abaixo:

```bash
java -jar processing-py.jar <MEU_PROGRAMA>.pyde
```



### Binário para Linux

Se você quiser compilar os programas de forma mais fácil, utilizando o comando `propy` de qualquer lugar da sua máquina. Baixe o arquivo `propy` desse diretório e execute os comandos abaixo:

```bash
sudo chmod 777 propy
sudo cp propy /bin/propy
```



Agora basta utiliza o comando abaixo para compilar os seus arquivos `.pyde`:

```bash
propy <MEU_PROGRAMA>.pyde
```

