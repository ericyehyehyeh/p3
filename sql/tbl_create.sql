USE group23db;
DROP TABLE if exists contain, photo, AlbumAccess, album,  user;

#P2: Updated password from TEXT(20) to varchar(256)
CREATE TABLE user (username VARCHAR(20), firstname TEXT(20), lastname TEXT(20), password VARCHAR(256), email TEXT(40), PRIMARY KEY(username));

#P2: updated album to hold an access enum with possible values of public and private
CREATE TABLE album(albumid INTEGER AUTO_INCREMENT, title TEXT(50), created DATETIME DEFAULT CURRENT_TIMESTAMP, lastupdated DATETIME DEFAULT CURRENT_TIMESTAMP, username VARCHAR(20), PRIMARY KEY(albumid), access ENUM('public','private') DEFAULT 'private');



ALTER TABLE album 
	ADD FOREIGN KEY (username) REFERENCES user (username);




CREATE TABLE contain (sequencenum INTEGER, albumid INTEGER, picid TEXT(40), caption TEXT(255), PRIMARY KEY(sequencenum), FOREIGN KEY (albumid) REFERENCES album (albumid));



CREATE TABLE photo (picid VARCHAR(40), format TEXT(3), date DATETIME DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY(picid));

#P2: Added AlbumAccess with foreign key constraints to album and user tables
CREATE TABLE AlbumAccess (albumid INTEGER, username VARCHAR(20));

ALTER TABLE AlbumAccess
	ADD FOREIGN KEY (albumid) REFERENCES album(albumid)
