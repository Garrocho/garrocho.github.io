/* OPERADOR LIMIT (LIMITA A BUSCA) */
SELECT * FROM nome_tabela LIMIT valor;

/* OPERADOR OFFSET (DEFINE POR ONDE COMEÇAR A BUSCA) */
SELECT * FROM nome_tabela LIMIT valor OFFSET 8;

/* OPERADOR LIKE (COMPARA CARACTERES E SEQUENCIAS EM TEXTOS DE COLUNAS) */
SELECT * FROM nome_tabela WHERE nome LIKE "%charles%";
/*
_ para caracter
% para sequencia de caracteres
OPERADOR ILIKE é n insensitive
*/

/* OPERADOR UNION (JUNTA TUDO E REMOVE AS DUPLICIDADES) */
SELECT CodPeca FROM Peca WHERE CidadePeca = 'GOIOERE'
UNION
SELECT CodPeca FROM Fornecedor WHERE CodFornecedor = "10";

/* OPERADOR INTERSECT (PEGA APENAS COLUNAS DUPLICADAS) */
SELECT CodPeca FROM Peca WHERE CidadePeca = 'GOIOERE'
INTERSECT
SELECT CodPeca FROM Fornecedor WHERE CodFornecedor = "10";

/* OPERADOR EXCEPT (PEGA APENAS COLUNAS NÃO DUPLICADAS QUE NÃO APARECEM NA SEGUNDA COLUNA) */
SELECT CodPeca FROM Peca WHERE CidadePeca = 'GOIOERE'
EXCEPT
SELECT CodPeca FROM Fornecedor WHERE CodFornecedor = "10";

/* OPERADOR INTO (CRIA UMA NOVA TABELA A APARTIR DE UMA BUSCA) */
SELECT CodFornecedor, NomeFornecedor INTO Forn_Goioere FROM Fornecedor WHERE cidade = "GOIOERE";

/* SUBCONSULTAS (IGUAL A VERMELHA)*/
SELECT CodFornecedor FROM Fornecedor WHERE CodPeca IN (SELECT CodPeca FROM Peca WHERE CorPeca = "Vermelha");

/* SUBCONSULTAS (DIFERENTE DE VERMELHA)*/
SELECT CodFornecedor FROM Fornecedor WHERE CodPeca NOT IN (SELECT CodPeca FROM Peca WHERE CorPeca = "Vermelha");


/* Exercícios:
1) Considere as tabelas abaixo:
Cliente (CPF, NOME)
Cartao  (ID, CPF, LIMITE)

2) Liste os 25 primeiros clientes.

3) Liste 40 cartões ordenados pelo maior limite.

4) Liste 2 clientes ordenados pelo nome de forma crescente, começando pelo décimo cliente.

5) Liste os CPF que estão cadastrados no sistema.

6) Liste os clientes que possuam cartões.

7) Liste os clientes que não possuam cartões.

8) Liste os clientes que possuem cartão e limite maior que 50.

9) Crie uma nova Tabela de Clientes que possuem Cartões com limite inferior a 100.
*/
