DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quakedate time,
  quaketime time with time zone,
  quakedepth real,
  mag real,
  magType text,
  place text,
  quaketype text
);