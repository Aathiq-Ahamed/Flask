DROP DATABASE `dotpro`;
CREATE DATABASE `dotpro`;
USE dotpro;
CREATE TABLE lectureSessions (
    name varchar(30),
    email text(30),
    sessionStart datetime,
);
-- CREATE TABLE lecturers (email text, firstName text, lastName text, subjectIDs text, hashedPass text);
-- CREATE TABLE students (email text, firstName text, lastName text, subjectIDs text, hashedPass text);
-- CREATE TABLE subjects (subjectID varchar (5), subjectName text);
-- CREATE TABLE questions (questionID varchar (5), question text, answer text, wrongAnswers text, sessionID varchar (5));
-- CREATE TABLE studentAnswers (questionID varchar (5), email text, result text);
-- CREATE TABLE attendance (email text, lectureSessionID varchar(5));
-- CREATE TABLE userSessions (userSessionID varchar(10), expiry datetime);
-- CREATE USER 'testuser'@'localhost' IDENTIFIED BY 'testpassword';
-- GRANT ALL PRIVILEGES ON sdgptest.* TO 'testuser'@'localhost';