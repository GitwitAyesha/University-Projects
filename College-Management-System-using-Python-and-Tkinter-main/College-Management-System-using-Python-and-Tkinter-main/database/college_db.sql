CREATE DATABASE IF NOT EXISTS `College_db` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `College_db`;

-- Drop and Create Table for courses
DROP TABLE IF EXISTS `course_table`;
CREATE TABLE `course_table` (
    course_id VARCHAR(36) PRIMARY KEY,
    course_name VARCHAR(100),
    semester INT,
    department VARCHAR(100)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Inserting initial data (if needed, otherwise can be left empty)
-- INSERT INTO `course_table` (`course_id`, `course_name`, `semester`, `department`) VALUES
-- ('CSE101', 'Computer Science Basics', 1, 'Computer Science');

-- Other tables (examples) that might be added based on requirements:
-- student_table, employee_table, etc.

-- Table structure for `student_table`
DROP TABLE IF EXISTS `student_table`;
CREATE TABLE `student_table` (
  id CHAR(5) PRIMARY KEY,
  name VARCHAR(30) NOT NULL,
  sem INT(11) NOT NULL,
  stream VARCHAR(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table structure for `employee_table`
DROP TABLE IF EXISTS `employee_table`;
CREATE TABLE `employee_table` (
  id CHAR(5) PRIMARY KEY,
  name VARCHAR(30) NOT NULL,
  desg VARCHAR(15) NOT NULL,
  dept VARCHAR(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table structure for `notice_board`
DROP TABLE IF EXISTS `notice_board`;
CREATE TABLE `notice_board` (
  id CHAR(5) PRIMARY KEY,
  topic VARCHAR(100) NOT NULL,
  description TEXT NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table structure for `global_values`
DROP TABLE IF EXISTS `global_values`;
CREATE TABLE `global_values` (
  x VARCHAR(10) NOT NULL,
  y VARCHAR(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Insert example data for `global_values`
INSERT INTO `global_values` (`x`, `y`) VALUES
('admin', 'admin');

COMMIT;
