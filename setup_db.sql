INSERT INTO "spatial_unit" (id, address)
VALUES (1, 'Princesshay'),
       (2, 'Princesshay'),
       (3, 'Princesshay'),
       (4, 'Princesshay'),
       (5, 'Princesshay'),
       (6, 'Princesshay'),
       (7, 'Princesshay'),
       (8, 'Princesshay'),
       (9, 'Princesshay'),
       (10, 'Princesshay'),
       (11, 'Princesshay'),
       (21, 'Princesshay'),
       (22, 'Princesshay'),
       (23, 'Princesshay'),
       (24, 'Princesshay'),
       (25, 'Princesshay'),
       (26, 'Princesshay'),
       (27, 'Princesshay'),
       (28, 'Princesshay'),
       (29, 'Princesshay');

INSERT INTO "ba_unit" (id, name)
VALUES (1, 'ABCD123'),
       (2, 'EFGH123'),
       (3, 'IJKL123'),
       (4, 'MNOP123'),
       (5, 'QRST123'),
       (6, 'UVWX123'),
       (7, 'YZAB123'),
       (8, 'DEFG123'),
       (9, 'HIJK123'),
       (10, 'CDEF123'),
       (11, 'ABCD123'),
       (12, 'YZAB123'),
       (13, 'HIJK123'),
       (14, 'CDEF123'),
       (15, 'MNOP123'),
       (16, 'QRST123'),
       (17, 'UVWX123'),
       (18, 'ABCD123'),
       (19, 'ABCD123'),
       (20, 'EFGH123');

INSERT INTO "spatial_unit_ba_unit_association" (spatial_unit_id, ba_unit_id)
VALUES (1, 1),
       (2, 2),
       (3, 3),
       (4, 4),
       (5, 5),
       (6, 6),
       (7, 7),
       (8, 8),
       (9, 9),
       (10, 10),
       (11, 11),
       (21, 12),
       (22, 13),
       (23, 14),
       (24, 15),
       (25, 16),
       (26, 17),
       (27, 18),
       (28, 19),
       (29, 20);

INSERT INTO "party" (id, name, type)
VALUES  (1, 'Peter Morris', 'Individual'),
        (2, 'Alexandra Bailey', 'Individual'),
        (3, 'Jack Farrell', 'Individual'),
        (4, 'Jennifer Patterson', 'Individual'),
        (5, 'Hollister Bank', 'Organisation'),
        (6, 'Jacob Daniels', 'Individual');

INSERT INTO "restriction" (id, ba_unit_id, description, type, party_id)
VALUES (1, 1, '', 'Mortgage', 1),
       (2, 2, '', 'Easement', 3),
       (3, 3, '', 'Mortgage', 2),
       (4, 4, '', 'Mortgage', 5),
       (5, 5, '', 'Mortgage', 6),
       (6, 6, '', 'Easement', 4),
       (7, 7, '', 'Mortgage', 2),
       (8, 8, '', 'Mortgage', 5),
       (9, 9, '', 'Mortgage', 3),
       (10, 10, '', 'Mortgage', 1),
       (11, 11, '', 'Mortgage', 4),
       (12, 11, '', 'Easement', 4),
       (13, 13, '', 'Mortgage', 2),
       (14, 14, '', 'Mortgage', 3),
       (15, 14, '', 'Easement', 1),
       (16, 19, '', 'Mortgage', 3);

INSERT INTO "mortgage" (id, restriction_id, type, amount, interest_rate)
VALUES (1, 1, 'Fixed Rate Mortgage', 257000, 3.5),
       (2, 3, 'Variable Mortgage', 123000, 2),
       (3, 4, 'Variable Mortgage', 450000, 1.5),
       (4, 5, 'Fixed Rate Mortgage', 335000, 3.1),
       (5, 7, 'Fixed Rate Mortgage', 275500, 2.4),
       (6, 8, 'Fixed Rate Mortgage', 181000, 5.5),
       (7, 9, 'Variable Mortgage', 234000, 3),
       (8, 10, 'Fixed Rate Mortgage', 110000, 2.7),
       (9, 11, 'Variable Mortgage', 366000, 1.9),
       (10, 13, 'Fixed Rate Mortgage', 645000, 2.8),
       (11, 14, 'Fixed Rate Mortgage', 521500, 3.3),
       (12, 16, 'Fixed Rate Mortgage', 415000, 4.3);

INSERT INTO "right" (id, ba_unit_id, description, type, party_id)
VALUES (1, 1, 'Absolute Freehold', 'Ownership', 1),
       (2, 2, 'Absolute Freehold', 'Ownership', 1),
       (3, 3, 'Leasehold', 'Ownership', 2),
       (4, 4, 'Leasehold', 'Ownership', 2),
       (5, 5, 'Leasehold', 'Ownership', 2),
       (6, 6, 'Leasehold', 'Ownership', 4),
       (7, 7, 'Leasehold', 'Ownership', 3),
       (8, 8, 'Leasehold', 'Ownership', 3),
       (9, 9, 'Leasehold', 'Ownership', 6),
       (10, 10, 'Leasehold', 'Ownership', 6),
       (11, 11, 'Absolute Freehold', 'Ownership', 1),
       (12, 12, 'Leasehold', 'Ownership', 3),
       (13, 13, 'Leasehold', 'Ownership', 3),
       (14, 14, 'Leasehold', 'Ownership', 3),
       (15, 15, 'Leasehold', 'Ownership', 6),
       (16, 16, 'Leasehold', 'Ownership', 4),
       (17, 17, 'Leasehold', 'Ownership', 4),
       (18, 18, 'Absolute Freehold', 'Ownership', 1),
       (19, 19, 'Absolute Freehold', 'Ownership', 1),
       (20, 20, 'Leasehold', 'Ownership', 4);

INSERT INTO "responsibility" (id, ba_unit_id, description, type, party_id)
VALUES (1, 7, '', 'Monument maintenance', 4),
       (2, 11, '', 'Building maintenance', 2),
       (3, 12, '', 'Building maintenance', 3),
       (4, 15, '', 'Building maintenance', 6);


ALTER SEQUENCE "ba_unit_id_seq" RESTART WITH 21; 
ALTER SEQUENCE "party_id_seq" RESTART WITH 7;
ALTER SEQUENCE "restriction_id_seq" RESTART WITH 17;
ALTER SEQUENCE "mortgage_id_seq" RESTART WITH 13;
ALTER SEQUENCE "right_id_seq" RESTART WITH 21;
ALTER SEQUENCE "responsibility_id_seq" RESTART WITH 5;
