
-- Remove existing database
DROP DATABASE CANARYAIRLINES;

-- Create fresh database
CREATE DATABASE CANARYAIRLINES
  DEFAULT CHARACTER SET utf8
  DEFAULT COLLATE utf8_general_ci;

-- Create tables
SOURCE /home/milosz/Documents/SQL_w_24h/Working_scripts/CreateTables.sql

-- Populate tables
SOURCE /home/milosz/Documents/SQL_w_24h/Working_scripts/Aircraft.sql
SOURCE /home/milosz/Documents/SQL_w_24h/Working_scripts/AircraftFleet.sql
SOURCE /home/milosz/Documents/SQL_w_24h/Working_scripts/Airports.sql
SOURCE /home/milosz/Documents/SQL_w_24h/Working_scripts/Countries.sql
SOURCE /home/milosz/Documents/SQL_w_24h/Working_scripts/EmployeePositions.sql

