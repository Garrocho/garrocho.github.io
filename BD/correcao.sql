/*01*/
CREATE TABLE Empregado (NumEmp INTEGER, NomeEmp VARCHAR, Salario INTEGER, Dept INTEGER);
CREATE TABLE Departamento (CodDept INTEGER, NomeDept VARCHAR, Ramal INTEGER);

/*02*/
INSERT INTO Departamento (CodDept, NomeDept, Ramal) VALUES (21, "Pessoal", 142);
INSERT INTO Departamento (CodDept, NomeDept, Ramal) VALUES (25, "Financeiro", 143);
INSERT INTO Departamento (CodDept, NomeDept, Ramal) VALUES (25, "Tecnico", 144);
INSERT INTO Empregado (NumEmp, NomeEmp, Salario, Dept) VALUES (032, "J Silva", 380, 21);
INSERT INTO Empregado (NumEmp, NomeEmp, Salario, Dept) VALUES (074, "M Reis", 400, 25);

/*03*/
SELECT NomeEmp FROM Empregado WHERE Dept = 21;

/*04*/
SELECT NomeEmp FROM Empregado WHERE Salario > 500 AND Dept = 28;

/*05*/
SELECT COUNT (*)FROM Empregado WHERE Dept = 25;

/*06*/
UPDATE Empregado SET Salario = 1000 WHERE Dept = 25;

/*07*/
DELETE FROM Empregado WHERE Salario > 350 AND Dept = 25; 

/*08*/
ALTER TABLE Departamento ADD COLUMN DataDeCriacao DATE;

/*09*/
ALTER TABLE Empregado DROP COLUMN Salario;

/*10*/
DROP TABLE IF EXISTS Empregado;
DROP TABLE IF EXISTS Departamento;
