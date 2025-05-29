document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("formCliente");

    form.addEventListener("submit", async (e) => {
        e.preventDefault(); // Impede recarregamento

        const formData = new FormData(form);
        const response = await fetch("/addCliente", {
            method: "POST",
            body: formData
        });
        
        if (!response.ok) {
            throw new Error("Erro na requisição");
        }
        
        const contentType = response.headers.get("content-type");
        if (!contentType || !contentType.includes("application/json")) {
            throw new Error("Resposta não é JSON.");
        }
        
        const result = await response.json();        

        Toastify({
            text: result.message,
            duration: 10000,
            close: true,
            gravity: "top",
            position: "right",
            style: {
                background: result.success ? "linear-gradient(90deg, green, lightgreen)" : "#c55",
                color: "#fff",
                borderRadius: "5px",
                padding: "1.5em",
            },
            stopOnFocus: true
        }).showToast();

        // Se for sucesso, limpa o formulário
        if (result.success) {
            form.reset();
        }
    });
});
