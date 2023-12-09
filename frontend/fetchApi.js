let restApiAddress = 'http://10.253.180.176:8002'
        
async function comune(restApiAddress, payload) {
    try {
        const response = await fetch(restApiAddress+payload[1], {
            method: payload[2],
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload[0])
        });

        const data = await response.json();
        console.log('Response data:', data);
    } catch (error) {
        console.error('Error:', error);
    }
}

function newEmployeeLoad(firstName, lastName, password, email, dateOfBirth, isAdmin, nick) {
    return [
        {
            firstName: 'honza',
            lastName:"palma",
            password:"pass",
            email:"mail@gmail.com",
            dateOfBirth:"2023-12-09",
            isAdmin: true,
            nick: "palma"
        },
        "/employee/new",
        "POST"
    ]
};
function getEmployeeLoad(idEmployee) {
    return [
        {
            idEmployee: '3'
        },
        "/employee/get",
        "GET"
    ]
};
function authEmployeeLoad(email, password) {
    return [
        {
            email:"mail@gmail.com",
            password:"pass"
        },
        "/employee/auth",
        "POST"
    ]
};
function deletEmployeeLoad(idEmployee) {
    return [
        {
            idEmployee: 'honza'
        },
        "/employee/delete",
        "DELETE"
    ]
};
function getMessages(idEmployee) {
    return [
        {
            idEmployee: 'honza'
        },
        "/messages/get",
        "GET"
    ]
};
function postMessages(idPatient, idEmployee, isSenderEmployee, content, repliesTo) {
    return [
        {
            idPatient: idPatient, 
            idEmployee: idEmployee, 
            isSenderEmployee: isSenderEmployee, 
            content: content, 
            repliesTo: repliesTo
        },
        "/messages/post",
        "POST"
    ]
};
function createPatients(firstName, lastName, password, dateOfBirth) {
    return [
        {
            firstName: firstName,
            lastName: lastName,
            password: password,
            dateOfBirth: dateOfBirth
        },
        "/patients/create",
        "POST"
    ]
};
function getPatients(firstName, lastName, password, dateOfBirth) {
    return [
        {
            firstName: firstName,
            lastName: lastName,
            password: password,
            dateOfBirth: dateOfBirth
        },
        "/patients/get",
        "GET"
    ]
};
function loginPatients(firstName, lastName, password, dateOfBirth) {
    return [
        {
            firstName: firstName,
            lastName: lastName,
            password: password,
            dateOfBirth: dateOfBirth
        },
        "/patients/login",
        "POST"
    ]
};
function deletePatients(idPatient) {
    return [
        {
            idPatient: idPatient
        },
        "/patients/delete",
        "DELETE"
    ]
};
function renamePatients(idPatient, newNick) {
    return [
        {
            idPatient: idPatient,
            newNick: newNick
        },
        "/patients/put",
        "PUT"
    ]
};