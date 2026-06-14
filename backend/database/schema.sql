-- ==========================
-- FAILSAFE Database Schema
-- ==========================

CREATE DATABASE failsafe_db;

-- ==========================
-- Faculty Table
-- ==========================

CREATE TABLE faculty (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ==========================
-- Students Table
-- ==========================

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    attendance FLOAT,
    marks FLOAT,
    risk VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ==========================
-- Predictions Table
-- ==========================

CREATE TABLE predictions (
    id SERIAL PRIMARY KEY,
    student_id INT,
    risk VARCHAR(20),
    probability FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_student
    FOREIGN KEY(student_id)
    REFERENCES students(id)
    ON DELETE CASCADE
);

-- ==========================
-- Interventions Table
-- ==========================

CREATE TABLE interventions (
    id SERIAL PRIMARY KEY,
    student_id INT,
    recommendation TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_student_intervention
    FOREIGN KEY(student_id)
    REFERENCES students(id)
    ON DELETE CASCADE
);