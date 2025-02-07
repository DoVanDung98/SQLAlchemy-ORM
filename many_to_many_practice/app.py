from sqlalchemy import (Column, ForeignKey, Integer, String, create_engine, Table, DateTime)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import datetime

db_url = "sqlite:///database.db"
engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Appointment(Base):
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    patient_id = Column(Integer, ForeignKey('patients.id'))
    appointment_date = Column(DateTime, default=datetime.utcnow)
    notes = Column(String)

    doctor = relationship("Doctor", backref="appointment")
    patient = relationship("Patient", backref="appointments")


class Doctor(Base):
    __tablename__ = "doctors"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    specialty = Column(String)


class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    dob = Column(DateTime)

Base.metadata.create_all(engine)

dr_smith = Doctor(name='Dr. Smith', specialty='Cardiology')
john_doe = Patient(name='John Doe', dob=datetime(1990, 1, 1))

appointment = Appointment(doctor=dr_smith, patient=john_doe, notes='Routine check-up')

session.add_all(dr_smith, appointment)
session.commit()