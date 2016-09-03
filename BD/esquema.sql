DROP TABLE IF EXISTS Programador;

DROP TABLE IF EXISTS Programa;

DROP TABLE IF EXISTS Analista;

DROP TABLE IF EXISTS Faz;

CREATE TABLE Programador (
	Codigo integer PRIMARY KEY AUTOINCREMENT,
	Nome text
);

CREATE TABLE Programa (
	Codigo integer PRIMARY KEY AUTOINCREMENT,
	Nome text
);

CREATE TABLE Analista (
	Codigo integer PRIMARY KEY AUTOINCREMENT,
	Nome text
);

CREATE TABLE Faz (
	CodigoProgramador integer,
	CodigoPrograma integer,
	CodigoAnalista integer,
	Nota integer,
	FOREIGN KEY(CodigoProgramador) REFERENCES Programador(Codigo),
	FOREIGN KEY(CodigoPrograma) REFERENCES Programa(Codigo),
	FOREIGN KEY(CodigoAnalista) REFERENCES Analista(Codigo)
);

