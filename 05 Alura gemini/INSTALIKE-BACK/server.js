import express from "express";

const app = express();  //Variável para armazenar o servidor

app.listen(3000, () => {  // Porta para receber requisição, como  se fosse um site, uma porta para receber os clientes
    console.log("Servidor Escutando...")
});

app.get("/api", (req, res) => {
    res.status(200).send("Seja Bem vindo (@)") // O 200 é o tipo de requisição, existe vários tipos de requisição, aqui o que a pessoa solicitou eu irei enviar, e nesse caso eu mando está mensagem
});