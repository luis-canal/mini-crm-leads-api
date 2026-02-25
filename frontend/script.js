const API_URL = "http://127.0.0.1:8000"

const headers = {
    "Content-Type": "application/json",
    "x-api-key": "123456"
}


async function criarLead() {

    const nome = document.getElementById("nome").value
    const telefone = document.getElementById("telefone").value
    const carro = document.getElementById("carro").value

    await fetch(API_URL + "/leads", {
        method: "POST",
        headers: headers,
        body: JSON.stringify({
            nome,
            telefone,
            carro,
            status: "novo"
        })
    })

    carregarLeads()
}


async function carregarLeads() {

    const response = await fetch(API_URL + "/leads", {
        headers: headers
    })

    const data = await response.json()

    const lista = document.getElementById("lista-leads")

    lista.innerHTML = ""

    data.leads.forEach(lead => {

        const li = document.createElement("li")

        li.innerHTML = `
            ${lead.nome} | ${lead.carro} | ${lead.status}
            <button onclick="deletarLead(${lead.id})">Excluir</button>
        `

        lista.appendChild(li)

    })
}


async function deletarLead(id) {

    await fetch(API_URL + "/leads/" + id, {
        method: "DELETE",
        headers: headers
    })

    carregarLeads()
}


carregarLeads()