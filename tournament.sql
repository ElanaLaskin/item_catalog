-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament

create table players(
player_id serial PRIMARY KEY,
name text
);

create table matches(
match_id serial PRIMARY KEY,
winner int references players(player_id),
loser int references players(player_id)
);

create view scores as 
	select players.player_id, players.name,
    count(a.winner) as wins,
    (count(a.winner) + count(b.loser)) as matches
    from players
    left outer join matches a
    on a.winner = players.player_id
    left outer join matches b
    on b.loser = players.player_id
    group by players.player_id;
