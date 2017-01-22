-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
create database tournament;

\c tournament

DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS matches;

create table players(
player_id serial PRIMARY KEY,
name text,
wins int default 0,
matches int default 0
);

create table matches(
match_id serial PRIMARY KEY,
winner int,
loser int
);

