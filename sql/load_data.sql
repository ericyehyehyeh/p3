#ADD USERS
#TRUNCATE album, user;

#P2 Changes: Added access values to each album - changed password to hashed passwords

#1. Add Sports Guy
INSERT INTO user (username, firstname, lastname, password, email) VALUES ('sportslover', 'Paul', 'Walker', 'sha512$8ec61415f1eb4afba45fa95e164a73e5$a8156f5e122a936e55512ccad145e72581c20853d8ceee8fc4ab535bead173dfb6625dd1d0eaccc9ace73008c135ef5eecb0b452470d007fde088602659ad9a2', 'sportslover@hotmail.com');

#1a. Add Sports Guy's Albums
INSERT INTO album (title, created, lastupdated, username, access) VALUES ('I love sports', NOW(), NOW(), 'sportslover','public');
INSERT INTO album (title, created, lastupdated, username, access) VALUES ('I love football', NOW(), NOW(), 'sportslover','private');


#2. Add Traveler Chica
INSERT INTO user (username, firstname, lastname, password, email) VALUES ('traveler', 'Rebecca', 'Travolta', 'sha512$1c662feb81e84cd78cf8d6a96e912ebb$eed150f49e6669c4aee79b0f1ed238ec557e8a6dc1af8c8b4dd393a1a6f0926b97bb537fc7a7af95db36982eaa90a313d4968cdc03112321e9dbb3c4aba65337', 'rebt@explorer.org');

#2a. Add Traveler Chica's Album
INSERT INTO album (title, created, lastupdated, username, access) VALUES ('Around The World', NOW(), NOW(), 'traveler','public');



#3. Add Space Dude
INSERT INTO user (username, firstname, lastname, password, email) VALUES ('spacejunkie', 'Bob', 'Spacey', 'sha512$523bbfca143d4676b5ecfc8ee42aca6d$fae41640d635cb42c3631e5a66a997e6f6ebfd25f6bb3f9777107d848c24bd2db9767242e803a881dbc5af73ddbf7ee80d1d855db2568061bfb2ca21fcf2dd5f', 'bspace@spacejunkies.net');

#3a. Add Space Dude's Album
INSERT INTO album (title, created, lastupdated, username, access) VALUES ('Cool Space Shots', NOW(), NOW(), 'spacejunkie','private');






#ADD PHOTOS TO DATABASE

#1. Add football photos to photo table
INSERT INTO photo (picid, format) VALUES ('001025dd643b0eb0661e359de86e3ea9', 'jpg');
INSERT INTO photo (picid, format) VALUES ('9a0a7d25af4f7a73f67dde74e8e54cff', 'jpg');
INSERT INTO photo (picid, format) VALUES ('c8e60100f13ffe374d59e39dc4b6a318', 'jpg');
INSERT INTO photo (picid, format) VALUES ('5e8b6207f007338243d3e29d6b82acab', 'jpg');


#2. Add space photos to photo table
INSERT INTO photo (picid, format) VALUES ('4ddba6e2f905e9778c6b6a48b6fc8e03', 'jpg');
INSERT INTO photo (picid, format) VALUES ('09d8a979fa638125b02ae1578eb943fa', 'jpg');
INSERT INTO photo (picid, format) VALUES ('143ba34cb5c7e8f12420be1b576bda1a', 'jpg');
INSERT INTO photo (picid, format) VALUES ('e615a10fc4222ede59ca3316c3fb751c', 'jpg');
INSERT INTO photo (picid, format) VALUES ('65fb1e2aa4977d9414d1b3a7e4a3badd', 'jpg');


#3. Add sports photos to photo table
INSERT INTO photo (picid, format) VALUES ('b94f256c23dec8a2c0da546849058d9e', 'jpg');
INSERT INTO photo (picid, format) VALUES ('01e37cbdd55913df563f527860b364e8', 'jpg');
INSERT INTO photo (picid, format) VALUES ('8d554cd1d8bb7b49ca798381d1fc171b', 'jpg');
INSERT INTO photo (picid, format) VALUES ('2e9e69e19342b98141789925e5f87f60', 'jpg');
INSERT INTO photo (picid, format) VALUES ('298e8943ef1942159ef88be21c4619c9', 'jpg');
INSERT INTO photo (picid, format) VALUES ('cefe45eaeaeb599256dda325c2e972da', 'jpg');
INSERT INTO photo (picid, format) VALUES ('bf755d13bb78e1deb59ef66b6d5c6a70', 'jpg');
INSERT INTO photo (picid, format) VALUES ('5f8d7957874f1303d8300e50f17e46d6', 'jpg');


#4. Add world photos to photo table
INSERT INTO photo (picid, format) VALUES ('bac4fca50bed35b9a5646f632bf4c2e8', 'jpg');
INSERT INTO photo (picid, format) VALUES ('f5b57bd7a2c962c54d55b5ddece37158', 'jpg');
INSERT INTO photo (picid, format) VALUES ('b7d833dd3aae203ca618759fc6f4fc01', 'jpg');
INSERT INTO photo (picid, format) VALUES ('faa20c04097d40cb10793a19246f2754', 'jpg');
INSERT INTO photo (picid, format) VALUES ('aaaadd578c78d21defaa73e7d1f08235', 'jpg');
INSERT INTO photo (picid, format) VALUES ('adb5c3af19664129141268feda90a275', 'jpg');
INSERT INTO photo (picid, format) VALUES ('abf97ffd1f964f42790fb358e5258e8d', 'jpg');
INSERT INTO photo (picid, format) VALUES ('ea2db8b970671856e43dd011d7df5fad', 'jpg');
INSERT INTO photo (picid, format) VALUES ('76d79b81b9073a2323f0790965b00a68', 'jpg');
INSERT INTO photo (picid, format) VALUES ('6510a4add59ef655ae3f0b6cdb24e140', 'jpg');
INSERT INTO photo (picid, format) VALUES ('28d38afca913a728b2a6bcf01aa011cd', 'jpg');
INSERT INTO photo (picid, format) VALUES ('5fb04eb11cbf99429a05c12ce2f50615', 'jpg');
INSERT INTO photo (picid, format) VALUES ('39ee267d13ccd32b50c1de7c2ece54d6', 'jpg');








#LINK PHOTOS TO ALBUMS

#1. Link Football photos
INSERT INTO contain (sequencenum, albumid, picid, caption) VALUES ('0', '2', '001025dd643b0eb0661e359de86e3ea9', '');
INSERT INTO contain (sequencenum, albumid, picid, caption) VALUES ('1', '2', '9a0a7d25af4f7a73f67dde74e8e54cff', '');
INSERT INTO contain (sequencenum, albumid, picid, caption) VALUES ('2', '2', 'c8e60100f13ffe374d59e39dc4b6a318', '');
INSERT INTO contain (sequencenum, albumid, picid, caption) VALUES ('3', '2', '5e8b6207f007338243d3e29d6b82acab', '');


#2. Link Space photos
INSERT INTO contain (sequencenum, albumid, picid, caption) VALUES ('4', '4', '4ddba6e2f905e9778c6b6a48b6fc8e03', '');
INSERT INTO contain (sequencenum, albumid, picid, caption) VALUES ('5', '4', '09d8a979fa638125b02ae1578eb943fa', '');
INSERT INTO contain (sequencenum, albumid, picid, caption) VALUES ('6', '4', '143ba34cb5c7e8f12420be1b576bda1a', '');
INSERT INTO contain (sequencenum, albumid, picid, caption) VALUES ('7', '4', 'e615a10fc4222ede59ca3316c3fb751c', '');
INSERT INTO contain (sequencenum, albumid, picid, caption) VALUES ('8', '4', '65fb1e2aa4977d9414d1b3a7e4a3badd', '');


#3. Link Sports photos
INSERT INTO contain (sequencenum, albumid, picid, caption) VALUES ('9', '1', 'b94f256c23dec8a2c0da546849058d9e', '');
INSERT INTO contain (sequencenum, albumid, picid, caption) VALUES ('10', '1', '01e37cbdd55913df563f527860b364e8', '');
INSERT INTO contain (sequencenum, albumid, picid, caption) VALUES ('11', '1', '8d554cd1d8bb7b49ca798381d1fc171b', '');
INSERT INTO contain (sequencenum, albumid, picid, caption) VALUES ('12', '1', '2e9e69e19342b98141789925e5f87f60', '');
INSERT INTO contain (sequencenum, albumid, picid, caption) VALUES ('13', '1', '298e8943ef1942159ef88be21c4619c9', '');
INSERT INTO contain (sequencenum, albumid, picid, caption) VALUES ('14', '1', 'cefe45eaeaeb599256dda325c2e972da', '');
INSERT INTO contain (sequencenum, albumid, picid, caption) VALUES ('15', '1', 'bf755d13bb78e1deb59ef66b6d5c6a70', '');
INSERT INTO contain (sequencenum, albumid, picid, caption) VALUES ('16', '1', '5f8d7957874f1303d8300e50f17e46d6', '');


#4. Link World photos
INSERT INTO contain (sequencenum, albumid, picid, caption) VALUES ('17', '3', 'bac4fca50bed35b9a5646f632bf4c2e8', '');
INSERT INTO contain (sequencenum, albumid, picid, caption) VALUES ('18', '3', 'f5b57bd7a2c962c54d55b5ddece37158', '');
INSERT INTO contain (sequencenum, albumid, picid, caption) VALUES ('19', '3', 'b7d833dd3aae203ca618759fc6f4fc01', '');
INSERT INTO contain (sequencenum, albumid, picid, caption) VALUES ('20', '3', 'faa20c04097d40cb10793a19246f2754', '');
INSERT INTO contain (sequencenum, albumid, picid, caption) VALUES ('21', '3', 'aaaadd578c78d21defaa73e7d1f08235', '');
INSERT INTO contain (sequencenum, albumid, picid, caption) VALUES ('22', '3', 'adb5c3af19664129141268feda90a275', '');
INSERT INTO contain (sequencenum, albumid, picid, caption) VALUES ('23', '3', 'abf97ffd1f964f42790fb358e5258e8d', '');
INSERT INTO contain (sequencenum, albumid, picid, caption) VALUES ('24', '3', 'ea2db8b970671856e43dd011d7df5fad', '');
INSERT INTO contain (sequencenum, albumid, picid, caption) VALUES ('25', '3', '76d79b81b9073a2323f0790965b00a68', '');
INSERT INTO contain (sequencenum, albumid, picid, caption) VALUES ('26', '3', '6510a4add59ef655ae3f0b6cdb24e140', '');
INSERT INTO contain (sequencenum, albumid, picid, caption) VALUES ('27', '3', '28d38afca913a728b2a6bcf01aa011cd', '');
INSERT INTO contain (sequencenum, albumid, picid, caption) VALUES ('28', '3', '5fb04eb11cbf99429a05c12ce2f50615', '');
INSERT INTO contain (sequencenum, albumid, picid, caption) VALUES ('29', '3', '39ee267d13ccd32b50c1de7c2ece54d6', '');





















