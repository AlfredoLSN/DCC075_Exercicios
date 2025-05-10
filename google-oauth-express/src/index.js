import express from "express";
import { OAuth2Client } from "google-auth-library";
import dotenv from "dotenv";

dotenv.config();

const app = express();
const port = 3000;

const client = new OAuth2Client(
  process.env.GOOGLE_CLIENT_ID,
  process.env.GOOGLE_CLIENT_SECRET,
  process.env.GOOGLE_REDIRECT_URI
);

//Lista de usuarios comuns
const commonGroup = ["alfredoliudigispark@gmail.com"];

//Lista de usuarios administradores
const adminGroup = ["alfredo.lucas@estudante.ufjf.br"];

//!Se o usuario nao estiver nos dois grupo acima ele será considerado como convidado

//Opcoes disponiveis para cada cargo
//Opcoes do cargo convidado
const options = {
  guest: ["Explorar conteúdos públicos", "Entrar em contato com o suporte"],
};

//Opcoes do cargo comum
options.common = [
  ...options.guest,
  "Alterar senha pessoal",
  "Visualizar documentos internos",
  "Enviar solicitações para o suporte",
  "Participar de fóruns internos",
];

//Opcoes do cargo admin
options.admin = [
  ...options.common,
  "Criar novos usuários",
  "Editar permissões de usuários",
  "Remover contas do sistema",
  "Ver logs de auditoria",
  "Modificar configurações do sistema",
];

//Funcao que recebe como parametro o email do usuario e retorna a qual grupo de permissoes ele pertence
const getOptionsForUser = (email) => {
  let group;
  if (commonGroup.includes(email)) {
    return options.common;
  } else if (adminGroup.includes(email)) {
    return options.admin;
  } else {
    return options.guest;
  }
};

app.get("/", (req, res) => {
  const url = client.generateAuthUrl({
    access_type: "offline",
    scope: ["email", "profile", "openid"],
  });
  res.send(`<a href="${url}">Login com Google </a>`);
});

app.get("/callback", async (req, res) => {
  try {
    const { code } = req.query;
    const { tokens } = await client.getToken(code);
    client.setCredentials(tokens);
    const ticket = await client.verifyIdToken({
      idToken: tokens.id_token,
      audience: process.env.GOOGLE_CLIENT_ID,
    });
    const payload = ticket.getPayload();
    const name = encodeURIComponent(payload.name);
    const email = encodeURIComponent(payload.email);

    res.redirect(`/welcome?name=${name}&email=${email}`);
  } catch (error) {
    console.error("Erro na autenticacao: ", error);
    res.status(500).send("Erro ao autenticar com o Google.");
  }
});

app.get("/welcome", (req, res) => {
  const { name, email } = req.query;

  const options = getOptionsForUser(email); // De acordo com o email do usuario será pego as opcoes disponiveis para ele confome o grupo de permissoes que ele pertence

  let optionsHTML = "";

  options.forEach((option) => {
    optionsHTML += `<li>${option}</li>`;
  }); // Aqui sera pego a lista de opcoes do usuario e a transforme em uma lista HTML para ser exibido na tela.

  res.send(`
        <h1>Bem-vindo, ${name}!</h1>
        <p>Seu e-email: ${email}</p>
        <ul>${optionsHTML}</ul>
    `);
});

app.listen(3000, () => {
  console.log(`Servidor rodando em http:${port}`);
});
