from contextlib import contextmanager
from datetime import date

from sqlalchemy import false

from Database.database import Session, Base, engine, session as perma_session
from Database.employee_models import Employees as Employee
from Database.message_models import Messages as Message
from Database.mood_models import Mood
from password_encryption import hashPassword, verifyPassword
from Database.patient_models import (
    Patients as Patient,
    AccessToPatient as EmployeePatientKey,
)


Base.metadata.create_all(engine)


@contextmanager
def get_db() -> Session:
    db = Session()  # Create a new database session
    try:
        yield db  # Provide the session to the route function
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()  # Close the session after the route function is done


def register_employee(
    firstName: str,
    lastName: str,
    email: str,
    password: str,
    dob: date,
    isAdmin: bool = False,
    nickname: str = None,
) -> int | None:
    """Registers an employee if one doesn't already exist

    Args:
        firstName (str):  The first name of the employee
        lastName (str): The last name of the employee
        email (str): The employee's email
        password (str): The password (unhashed) of the employee
        dob (date): The date the employee was born on
        isAdmin (bool, optional): Whether the employee is an admin. Defaults to False.
        nickname (str, optional): The nickname of the employee (optional). Defaults to None.

    Returns:
        int | None: _description_
    """
    password = password.encode("utf-8")
    e: Employee = Employee(
        firstName=firstName,
        lastName=lastName,
        email=email,
        password=hashPassword(password),
        isAdmin=isAdmin,
        nick=nickname,
        dateOfBirth=dob,
    )
    try:
        with get_db() as session:
            exisiting_employee = session.query(Employee).filter_by(email=email).first()
            if not exisiting_employee is None:
                return None
            session.add(e)
            session.commit()
            return e.idEmployee
    except:
        return None


def login_employee(email: str, password: str) -> int | None:
    password = password.encode("utf-8")
    try:
        with get_db() as session:
            exisiting_employee = session.query(Employee).filter_by(email=email).first()
            if exisiting_employee is None:
                return False
            return verifyPassword(password, exisiting_employee.password)
    except:
        return False


def get_employee(**query_keys) -> dict | None:
    """Returns a JSON of an employee

    Returns:
        dict: Employee (without password)
    """
    with get_db() as session:
        employee: Employee = session.query(Employee).filter_by(**query_keys).first()
        if not employee:
            return None
        return {
            "id": employee.idEmployee,
            "firstName": employee.firstName,
            "lastName": employee.lastName,
            "nickname": employee.nick,
            "hasAdmin": employee.isAdmin,
        }


def delete_employee(employeeId) -> bool:
    try:
        with get_db() as session:
            employee: Employee = (
                session.query(Employee).filter_by(idEmployee=employeeId).first()
            )
            if employee is None:
                return False
            session.delete(employee)
            session.commit()
        return True
    except:
        return False


def set_employee_nickname(employeeId, newNickName) -> bool:
    try:
        with get_db() as session:
            employee: Employee = (
                session.query(Employee).filter_by(idEmployee=employeeId).first()
            )
            if employee is None:
                return False
            employee.nick = newNickName
            session.add(employee)
            session.commit()
        return True
    except:
        return False


def register_patient(
    firstName: str, lastName: str, dob: date, password: str
) -> int | None:
    password = password.encode("utf-8")
    p = Patient(
        firstName=firstName,
        lastName=lastName,
        passcode=hashPassword(password),
        dateOfBirth=dob,
    )
    try:
        with get_db() as session:
            exisiting_patient = (
                session.query(Patient)
                .filter_by(firstName=firstName, lastName=lastName, dateOfBirth=dob)
                .first()
            )
            if not exisiting_patient is None:
                return None
            session.add(p)
            session.commit()
            return p.idEmployee
    except:
        return None


def login_patient(firstName: str, lastName: str, dob: date, password: str) -> bool:
    password = password.encode("utf-8")
    try:
        with get_db() as session:
            patient = (
                session.query(Patient)
                .filter_by(firstName=firstName, lastName=lastName, dateOfBirth=dob)
                .first()
            )
            if patient is None:
                return False
            return verifyPassword(password, patient.passcode)
    except:
        return False


def get_patient(**query_keys):
    with get_db() as session:
        patient: Patient = session.query(Patient).filter_by(**query_keys).first()
        if not patient:
            return None
        return {
            "id": patient.idEmployee,
            "firstName": patient.firstName,
            "lastName": patient.lastName,
            "nickname": patient.nick,
            "hasAdmin": patient.isAdmin,
        }


def delete_patient(patientId: int) -> bool:
    try:
        with get_db() as session:
            patient = session.query(Patient).filter_by(idPatient=patientId).first()
            if patient is None:
                return False
            session.delete(patient)
            session.commit()
        return True
    except:
        return False


def set_patient_nickname(patientId, newNickName) -> bool:
    try:
        with get_db() as session:
            patient: Patient = (
                session.query(Patient).filter_by(idPatient=patientId).first()
            )
            if patient is None:
                return False
            patient.nick = newNickName
            session.add(patient)
            session.commit()
        return True
    except:
        return False


def allow_access(patientId, employeeId) -> bool:
    k: EmployeePatientKey(idEmployee=employeeId, idPatient=patientId)
    try:
        with get_db() as session:
            exisiting_key = (
                session.query(EmployeePatientKey)
                .filter_by(idEmployee=employeeId, idPatient=patientId)
                .first()
            )
            if not exisiting_key is None:
                return False
            exists_primary = (
                session.query(EmployeePatientKey)
                .filter_by(idPatient=patientId, isPrimaryNurse=True)
                .first()
            )
            if not exists_primary:
                k.isPrimaryNurse = True
            session.add(k)
            session.commit()
            return True
    except:
        return False


def deny_access(patientId, employeeId) -> bool:
    try:
        with get_db() as session:
            exisiting_key = (
                session.query(EmployeePatientKey)
                .filter_by(idEmployee=employeeId, idPatient=patientId)
                .first()
            )
            if exisiting_key is None:
                return False
            session.delete(exisiting_key)
            session.commit()
            return True
    except:
        return False


def has_access(patientId, employeeId) -> bool:
    try:
        with get_db() as session:
            exisiting_key = (
                session.query(EmployeePatientKey)
                .filter_by(idEmployee=employeeId, idPatient=patientId)
                .first()
            )
            return not exisiting_key is None
    except:
        return False
