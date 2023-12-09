from contextlib import contextmanager
from datetime import date, datetime

from sqlalchemy import false

from Database.database import Session, Base, engine, session as perma_session
from Database.employee_models import Employees as Employee
from Database.message_models import Messages as Message
from Database.mood_models import Mood
from password_encryption import hashPassword, checkPassword as verifyPassword
from Database.patient_models import (
    Patients as Patient,
    AccessToPatient as EmployeePatientKey,
)


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


def login_employee(email: str, password: str) -> bool:
    """Returns whether the password is correct or not

    Args:
        email (str): The email of the employee
        password (str): The (unhashed) password

    Returns:
        bool: Correct or incorrect?
    """
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


def delete_employee(employeeId: int) -> bool:
    """Deletes an employee

    Args:
        employeeId (int): The ID of the employee to delete

    Returns:
        bool: Whether they were or weren't deleted (either due to an error or because they don't exist)
    """
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


def set_employee_nickname(employeeId: int, newNickName: str) -> bool:
    """Sets an employee's nickname

    Args:
        employeeId (int): The ID of the employee
        newNickName (str): The new nickname

    Returns:
        bool: Whether we succeeded or not
    """
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
    """Registers a patient if they don't already exist

    Args:
        firstName (str): The first name of the patient
        lastName (str): The last name of the patient
        dob (date): Date of the birth of the patient
        password (str): The passcode of the patient

    Returns:
        int | None: Either the ID of the patient or None if we failed
    """
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
    """Whether the password for the patient is correct or not

    Args:
        firstName (str): The first name
        lastName (str): The last name
        dob (date): The date of birth of the patient
        password (str): The patient's password

    Returns:
        bool: Whether the password is correct or incorrect
    """
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


def get_patient(**query_keys) -> dict | None:
    """retrieves the patient based on any key (matching the model)

    Returns:
        dict: The data of the patient (without password) - dateOfBirth is 'dob'
    """
    with get_db() as session:
        patient: Patient = session.query(Patient).filter_by(**query_keys).first()
        if not patient:
            return None
        return {
            "id": patient.idPatient,
            "firstName": patient.firstName,
            "lastName": patient.lastName,
            "nickname": patient.nick,
            "dob": patient.dateOfBirth,
        }


def delete_patient(patientId: int) -> bool:
    """Deletes the patient based off an ID

    Args:
        patientId (int): The Id of the patient to delete

    Returns:
        bool: Whether we succeeded or not
    """
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


def set_patient_nickname(patientId: int, newNickName: str) -> bool:
    """Sets a patient nickname

    Args:
        patientId (int): The ID of the patient
        newNickName (str): The new nickname

    Returns:
        bool: Whether we succeeded or not
    """
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


def send_message(
    patientId: int,
    employeeId: int,
    isSenderEmployee: bool,
    content: str,
    repliesTo: int | None = None,
) -> bool:
    """Sends a message

    Args:
        patientId (int): The patient to either receive or send the message
        employeeId (int): The nurse to either receive or send the message
        isSenderEmployee (bool): Whether it's the employee that's sending the message
        content (str): The content of the message
        repliesTo (int | None, optional): Whether the message is a reply to another message. If it is, this is the ID of the message it's replying to. Defaults to None.

    Returns:
        bool: Whether we succeeded
    """
    m = Message(
        idEmployee=employeeId,
        idPatient=patientId,
        senderIsPatient=not isSenderEmployee,
        replyTo=repliesTo,
        content=content,
        createdAt=datetime.now(),
    )
    try:
        with get_db() as session:
            session.add(m)
            session.commit()
        return True
    except Exception as _:  # _ means ignored or unused
        pass
    return False


def get_messages(patientId: int) -> list[dict] | None:
    """_summary_

    Args:
        patientId (int): The ID of the patiend we want to get reponses for

    Returns:
        list[dict] | None: None only if we failed.

    Dict Format:
        "messageId": m.idMessage,
        "content": m.content,
        "senderIsPatient": m.senderIsPatient,
        "senderIsEmployee": not m.senderIsPatient,
        "patientId": m.idPatient,
        "employeeId": m.idEmployee,
        "timestamp": m.createdAt.timestamp(),
    """
    try:
        with get_db() as session:
            messages: list[Message] = (
                session.query(EmployeePatientKey).filter_by(idPatient=patientId).all()
            )
            return [
                {
                    "messageId": m.idMessage,
                    "content": m.content,
                    "senderIsPatient": m.senderIsPatient,
                    "senderIsEmployee": not m.senderIsPatient,
                    "patientId": m.idPatient,
                    "employeeId": m.idEmployee,
                    "timestamp": m.createdAt.timestamp(),
                }
                for m in messages
            ]
    except Exception as _:
        pass
    return None


from enum import Enum


class SortMethod(Enum):
    ALPHABETICAL = "Alphabetical"
    REVERSE = "Reverse"
    RECENT = "Recent"


def get_all_patients(
    sort_method: SortMethod = SortMethod.ALPHABETICAL,
) -> list[Patient] | None:
    try:
        with get_db() as session:
            patients: list[Patient] | None = session.query(Patient).all()

            # Define sorting key based on the selected sort method
            if sort_method == SortMethod.RECENT:
                patients.sort(key=lambda p: p.idPatient, reverse=True)
            elif sort_method == SortMethod.ALPHABETICAL:
                patients.sort(key=lambda p: (p.lastName, p.firstName))
            elif sort_method == SortMethod.REVERSE:
                patients.sort(key=lambda p: (p.lastName, p.firstName), reverse=True)

            return [
                {
                    "idPatient": p.idPatient,
                    "firstName": p.firstName,
                    "lastName": p.lastName,
                    "nickname": p.nick,
                    "dateOfBirth": p.dateOfBirth,
                }
                for p in patients
            ]
    except:
        return None


def get_all_patients_of_nurse(
    employeeid: int,
    sort_method: SortMethod = SortMethod.ALPHABETICAL,
) -> list[Patient] | None:
    try:
        with get_db() as session:
            patients: list[Patient] | None = (
                session.query(Patient).filterBy(idEmployee=employeeid).all()
            )

            # Define sorting key based on the selected sort method
            if sort_method == SortMethod.RECENT:
                patients.sort(key=lambda p: p.idPatient, reverse=True)
            elif sort_method == SortMethod.ALPHABETICAL:
                patients.sort(key=lambda p: (p.lastName, p.firstName))
            elif sort_method == SortMethod.REVERSE:
                patients.sort(key=lambda p: (p.lastName, p.firstName), reverse=True)

            return [
                {
                    "idPatient": p.idPatient,
                    "firstName": p.firstName,
                    "lastName": p.lastName,
                    "nickname": p.nick,
                    "dateOfBirth": p.dateOfBirth,
                }
                for p in patients
            ]
    except:
        return None
