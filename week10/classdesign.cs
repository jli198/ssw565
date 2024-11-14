using System;
using System.Data.SqlClient;

// Represents single survey
public class Survey
{
  public int SurveyId { get; set; }
  public string BuildingType { get; set; }
  public string Characteristics { get; set; }
  // Add other properties relevant to survey
}

// Database access layer interface for adhering to Dependency Inversion Principle
public interface IDatabaseAccess
{
  void SaveSurvey(Survey survey);
}

// Concrete implementation of IDatabaseAccess for SQL Server