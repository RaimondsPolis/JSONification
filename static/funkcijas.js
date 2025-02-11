
const LAIKS = 1000



async function suutiitzinju(){
    let zinja = document.getElementById("teksts").value;
    let vards = document.getElementById("vards").value;
    document.getElementById("teksts").value = "";
    const atbilde = await fetch("/suutiit", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({"saturs": zinja, "vards": vards})
    });
    // lasiitZinju()
}

async function lasiitZinju(){
    let vieta = document.getElementById("chats");
    const atbilde = await fetch('/jschats/lasiit')
    zinas = await atbilde.json()
    raadiitZinjas(zinas)
    await new Promise(resolve => setTimeout(resolve, LAIKS))
    await lasiitZinju()
}

function raadiitZinjas(saturs){
    let vieta = document.getElementById("chats");
    teksts = ""
    for(rinda of saturs){
        elementi = rinda.split("----")
        teksts += "<b>"+elementi[0]+"</b> - "+ elementi[1] + "<br>" 
    }
    vieta.innerHTML = teksts
}