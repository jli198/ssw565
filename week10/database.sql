CREATE TABLE Users (
  UserID INT AUTO_INCREMENT PRIMARY KEY,
  Username VARCHAR(255) NOT NULL UNIQUE,
  PasswordHash VARCHAR(255) NOT NULL,
  Email VARCHAR(255) NOT NULL UNIQUE,
  Role VARCHAR(100) NOT NULL,
  CreatedAt DATETIME NOT NULL,
  UpdatedAt DATETIME
);