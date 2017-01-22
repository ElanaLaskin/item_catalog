## Swiss Tournament

*A database schema to store the game matches between players with code to query this data and determine the winners of various games.*

SETUP:

1) cd to the directory where you want to clone my repository and type `git clone https://github.com/ElanaLaskin/fullstack-nanodegree-vm.git`

2) `cd /vagrant`

3) `vagrant up` (start virtual machine, this may take a little while)

4) `vagrant ssh`

5) `cd /vagrant/tournament`

6) `psql` 

7) `\i tournament.sql` to initialize the database

8) from here you can run querries directly or quit with `\q`

9) you can interact with the database using the functions that I wrote in tournament.py
first run python: `python` and import all the files: `from tournament import *`

10) Its a good idea to take a look at tournament.py to get an idea of what functions exist.
To run a function, simply call the function from within the python shell like so:
*Add new player:* `registerPlayer('Ronald Dump')`