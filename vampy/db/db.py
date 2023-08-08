"""DOCSTRING"""
from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine, MetaData
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlite3
from sqlite3 import Error


Base = declarative_base()

experiment_run = Table(
    "experiment_run",
    Base.metadata,
    Column("experiment_id", Integer, ForeignKey("experiment.experiment_id")),
    Column("run_id", Integer, ForeignKey("run.run_id"))
)

run_data = Table(
    "run_data",
    Base.metadata,
    Column("run_id", Integer, ForeignKey("run.run_id")),
    Column ("data_id", Integer, ForeignKey("data.data_id"))
)


class Experiment(Base):
    __tablename__ = "experiment"
    experiment_id = Column(Integer, primary_key=True)
    experiment_label = Column(String)
    runs = relationship("Run", secondary=experiment_run, back_populates="experiment_id")
    experiment_notes = Column(String)


class Run(Base):
    __tablename__ = "run"
    run_id = Column(Integer, primary_key=True)
    run_label = Column(String)
    experiment_id = relationship("Experiment", secondary=experiment_run, back_populates="runs")
    data = relationship("Data", secondary=run_data,  back_populates="run_id")
    system = Column(Integer, ForeignKey("system.system_id"))
    simulation = Column(Integer, ForeignKey("simulation.simulation_id"))
    environment = Column(Integer, ForeignKey("environment.environment_id"))
    run_notes = Column(String)


class Data(Base):
    __tablename__ = "data"
    data_id = Column(Integer, primary_key=True)
    data_label = Column(String)
    run_id = relationship("Run", secondary=run_data, back_populates="data")
    data_path = Column(String)


class System(Base):
    __tablename__ = "system"
    system_id = Column(Integer, primary_key=True)
    system_label = Column(String)
    system_obj = Column(String)


class Simulation(Base):
    __tablename__ = "simulation"
    simulation_id = Column(Integer, primary_key=True)
    simulation_label = Column(String)
    simulation_obj = Column(String)


class Environment(Base):
    __tablename__ = "environment"
    environment_id = Column(Integer, primary_key=True)
    environment_label = Column(String)
    environment_path = Column(String)


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    engine = create_engine(f"sqlite:////home/luc/test.db")
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    session.add(Data(data_label="test_data", data_path="test"))
    session.commit()
    print(session.query(Data).all()[3].data_id)