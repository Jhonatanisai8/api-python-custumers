function abrirFormulario() {
    let htmlModal = document.getElementById("modal");
    if (htmlModal) {
        htmlModal.classList.add("opened");
    } else {
        console.error("El elemento con id 'modal' no existe.");
    };
}
function cerrarModal() {
    let htmlModal = document.getElementById("modal");
    if (htmlModal) {
        htmlModal.classList.remove("opened");
    } else {
        console.error("El elemento con id 'modal' no existe.");
    };
}
function agregar() {
    clean()
    abrirFormulario()
}

const URL_API = 'http://127.0.0.1:8080/api/'
document.addEventListener("DOMContentLoaded", search);

let customers = []
function init() {
    search()
}

async function search() {
    let url = URL_API + 'custumers'
    let response = await fetch(url, {
        "method": 'GET',
        "headers": {
            "Content-Type": 'application/json'
        }
    })
    customers = await response.json();
    // console.log(customers)
    let html = ''
    for (customer of customers) {
        // debugger;
        let row = `
        <tr>
        <td>${customer.firstname}</td>
            <td>${customer.lastname}</td>
            <td>${customer.email}</td>
            <td>${customer.phone}</td>
            <td>${customer.address}</td>
            <td>
            <button class="button-blue" onclick="updateCustomer(${customer.custumer_id})">Modificar</button>
            <button class="button-red" onclick="deleteCustumer(${customer.custumer_id})" >Eliminar</button>
                </td>
        </tr>`
        html = html + row;
    }

    document.querySelector('#customers > tbody').outerHTML = html;
}

async function deleteCustumer(id) {
    let respuesta = confirm('¿ESTAS SEGURO DE ELIMINARLO?')
    if (respuesta) {
        // alert("Se Elimino")
        console.log(respuesta)
        let url = URL_API + 'custumers/' + id
        /*let response =*/
        await fetch(url, {
            "method": 'DELETE',
            "headers": {
                "Content-Type": 'application/json'
            }
        })
        window.location.reload()
    }
}


async function updateCustomer(custumer_id) {
    abrirFormulario();
    // buscamos el objeto con el id pasado por parametro
    let customer = customers.find(x => x.custumer_id == custumer_id);

    // llenamos los campos del formulario con la información del cliente
    document.getElementById('txtId').value = customer.custumer_id;
    document.getElementById('txtNombre').value = customer.firstname;
    document.getElementById('txtApellido').value = customer.lastname;
    document.getElementById('txtEmail').value = customer.email;
    document.getElementById('txtTelefono').value = customer.phone;
    document.getElementById('txtDireccion').value = customer.address;
}

async function saveCustumer() {
    let nombre = document.getElementById("txtNombre").value;
    let apellido = document.getElementById("txtApellido").value;
    let email = document.getElementById("txtEmail").value;
    let telefono = document.getElementById("txtTelefono").value;
    let direccion = document.getElementById("txtDireccion").value;

    var data = {
        "firstname": nombre,
        "lastname": apellido,
        "email": email,
        "phone": telefono,
        "address": direccion
    }

    var customerID = document.getElementById("txtId").value;
    if (customerID != '') {
        data.custumer_id = customerID;
    }

    let url = URL_API + 'custumers';
    let method = customerID ? 'PUT' : 'POST';

    let response = await fetch(url, {
        "method": method,
        "body": JSON.stringify(data),
        "headers": {
            "Content-Type": 'application/json'
        }
    });

    if (response.ok) {
        console.log("Cliente guardado correctamente.");
        window.location.reload();  // Recargamos la página para actualizar la lista
    } else {
        console.error("Error al guardar el cliente", await response.text());
    }
}

function clean() {
    document.getElementById('txtId').value = ''
    document.getElementById('txtNombre').value = ''
    document.getElementById('txtApellido').value = ''
    document.getElementById('txtEmail').value = ''
    document.getElementById('txtTelefono').value = ''
    document.getElementById('txtDireccion').value = ''
}