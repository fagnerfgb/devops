const express = require("express")

const app = express();
const PORT = process.env.PORT || 8080;

app.use(express.json());
app.use(express.static("public"));
app.set("view engine", "ejs");

app.get("/", (req, res) => {
    res.render("index");
});

app.listen(PORT, () => console.log(`Aplicação em execução na porta ${PORT}`));