-- Creates and fills a table second_table with attributes id, name and score in my MySQL server with multiple rows.
CREATE TABLE IF NOT EXISTS `second_table` (`id` INT, `name` VARCHAR(256), `score` INT);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (1, "lucy", 10);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (2, "Jane", 3);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (3, "June", 14);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (4, "Mark", 8);
