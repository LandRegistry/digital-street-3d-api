INSERT INTO "spatial_unit" (id, address)
VALUES (1, '10 Spicer Road, EX1 1AB'),
       (2, 'Flat 1, 10 Spicer Road, EX1 1AB'),
       (3, 'Flat 2, 10 Spicer Road, EX1 1AB'),
       (4, 'Flat 3, 10 Spicer Road, EX1 1AB'),
       (5, 'Flat 4, 10 Spicer Road, EX1 1AB'),
       (6, '');

INSERT INTO "ba_unit" (id, name)
VALUES (1, 'ABCD123'),
       (2, 'EFGH123'),
       (3, 'IJKL123'),
       (4, 'MNOP123'),
       (5, 'QRST123'),
       (6, 'UVWX123');

INSERT INTO "price_paid" (id, spatial_unit_id, amount, date)
VALUES (1, 1, 500000, DATE '2006-10-05'),
       (2, 2, 105000, DATE '2008-01-18'),
       (3, 1, 1000000, DATE '2009-12-03'),
       (4, 5, 140000, DATE '2010-04-01'),
       (5, 4, 139000, DATE '2010-11-21'),
       (6, 2, 104000, DATE '2011-06-13'),
       (7, 2, 153000, DATE '2013-05-08'),
       (8, 3, 145000, DATE '2016-02-26'),
       (9, 6, 200000, DATE '2019-03-15');

INSERT INTO "spatial_unit_ba_unit_association" (spatial_unit_id, ba_unit_id)
VALUES (1, 1),
       (2, 2),
       (3, 3),
       (4, 4),
       (5, 5),
       (6, 6);

INSERT INTO "party" (id, name, type)
VALUES  (1, 'Peter Morris', 'Individual'),
        (2, 'Alexandra Bailey', 'Individual'),
        (3, 'Jack Farrell', 'Individual'),
        (4, 'Jennifer Patterson', 'Individual'),
        (5, 'Hollister Bank', 'Organisation'),
        (6, 'Jacob Daniels', 'Individual'),
        (7, 'Airspace Limited', 'Organisation'),
        (8, 'Woodbury Bank', 'Organisation'),
        (9, 'Royal Bank', 'Organisation'),
        (10, 'Western Bank', 'Organisation');

INSERT INTO "restriction" (id, ba_unit_id, description, type, party_id)
VALUES (1, 1, '', 'Mortgage', 8),
       (2, 2, '', 'Easement', 3),
       (3, 2, '', 'Mortgage', 9),
       (4, 3, '', 'Mortgage', 5),
       (5, 4, '', 'Mortgage', 5),
       (6, 5, '', 'Mortgage', 10),
       (7, 5, '', 'Easement', 7),
       (8, 6, '', 'Mortgage', 9);

INSERT INTO "right" (id, ba_unit_id, description, type, party_id)
VALUES (1, 1, 'Ownership of the land, its subsoil and airspace', 'Absolute Freehold', 1),
       (2, 2, 'Ownership of entire flat', 'Leasehold', 2),
       (3, 3, 'Ownership of entire flat', 'Leasehold', 3),
       (4, 4, 'Ownership of entire flat', 'Leasehold', 4),
       (5, 5, 'Ownership of entire flat', 'Leasehold', 6),
       (6, 6, 'Ownership of the airspace above the building, rising 15 metres vertically from the outer edge and flat roof of the building', 'Leasehold', 7);

INSERT INTO "responsibility" (id, ba_unit_id, description, type, party_id)
VALUES (1, 1, '', 'Building maintenance', 1),
       (2, 1, '', 'Monument maintenance', 1),
       (3, 2, '', 'Building maintenance', 2),
       (4, 3, '', 'Building maintenance', 3),
       (5, 4, '', 'Building maintenance', 4),
       (6, 5, '', 'Building maintenance', 6),
       (7, 6, '', 'Building maintenance', 7);


ALTER SEQUENCE "ba_unit_id_seq" RESTART WITH 7; 
ALTER SEQUENCE "price_paid_id_seq" RESTART WITH 10;
ALTER SEQUENCE "party_id_seq" RESTART WITH 11;
ALTER SEQUENCE "restriction_id_seq" RESTART WITH 9;
ALTER SEQUENCE "right_id_seq" RESTART WITH 7;
ALTER SEQUENCE "responsibility_id_seq" RESTART WITH 7;
