DROP TABLE IF EXISTS Pessoa;

DROP TABLE IF EXISTS Aviao;

DROP TABLE IF EXISTS Classe;

DROP TABLE IF EXISTS Assento;

DROP TABLE IF EXISTS Voo;

DROP TABLE IF EXISTS Aeroporto;

DROP TABLE IF EXISTS Passagem;

DROP TABLE IF EXISTS Refeicao;

CREATE TABLE Pessoa (
	Identidade string,
	Nome string
);

CREATE TABLE Aviao (
	NumeroSerie string,
	Modelo string
);

CREATE TABLE Classe (
	Codigo integer PRIMARY KEY AUTOINCREMENT,
	Nome string,
	Refeicao integer
);

CREATE TABLE Assento (
	Numero integer PRIMARY KEY AUTOINCREMENT,
	Classe integer
);

CREATE TABLE Voo (
	Codigo integer PRIMARY KEY AUTOINCREMENT,
	Aviao string,
	Piloto string,
	Origem string,
	Destino string,
	HorarioPartida timestamp,
	HorarioChegada timestamp
);

CREATE TABLE Aeroporto (
	Codigo string,
	Nome string
);

CREATE TABLE Passagem (
	Passageiro string,
	Voo string,
	Assento integer
);

CREATE TABLE Refeicao (
	Codigo integer PRIMARY KEY AUTOINCREMENT,
	Nome string
);

