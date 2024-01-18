-- A script that creates user and grants all privilages
-- Create a user user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1' IDENTIFIED BY 'user_0d_pwd';
-- Grants all privileges to user user_0d_1
GRANT ALL ON *.* TO 'user_0d_1' WITH GRANT OPTION;
