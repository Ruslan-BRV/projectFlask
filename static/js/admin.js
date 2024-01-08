let arrayBtns = document.querySelectorAll(".delete-good")

for (let btn of arrayBtns) {
    let id = btn.dataset.id
    btn.addEventListener("click", () => {
        fetch("/deleteProduct", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(id)
        })
    })
}

