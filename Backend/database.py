from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mssql+pyodbc://sb:sa@VISHNUJI\\MSSQLSERVER01/Clinic?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"

# Create the engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
