-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
create database tournament;

\c tournament

DROP TABLE IF EXISTS players, matches;

create table players(
player_id serial primary key,
name text,
score int
);

create table matches(
match_id decimal primary key,
player_1 int,
player_2 int,
winner int
);

