const readline = require("readline");

//Lista para simular 3 usuarios com cargos diferentes em um sistema qualquer
//Guest - Convidado
//Common - Comum
//Admin - Administrador
const users = [
  {
    username: "user1",
    password: "guest123",
    role: "guest",
  },
  {
    username: "user2",
    password: "common123",
    role: "common",
  },
  {
    username: "user3",
    password: "admin123",
    role: "admin",
  },
];

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

//Uso de um pacote do node para conseguir ler entradas do teclado
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

//Funcao para fazer perguntas ao usuario no terminal
const askQuestion = (question) => {
  return new Promise((resolve) => {
    rl.question(question, (answer) => resolve(answer));
  });
};

//Funcao para buscar um determinado usuario com o username e password que foram passados no terminal
const findUser = (username, password) => {
  const index = users.findIndex(
    (user) => user.username === username && user.password === password
  );

  return index !== -1 ? users[index] : null;
};

//Funcao para printar no terminal as opcoes disponiveis para o usuario com base no seu cargo
const printOptions = (user) => {
  console.log("Bem vindo ", user.username);

  if (options[user.role]) {
    console.log("Opcoes disponiveis");
    options[user.role].forEach((option, index) => {
      console.log(`${index + 1} - ${option}`);
    });
  } else {
    console.log("Role Invalida");
  }
};

//Funcao principal que executa o programa
async function main() {
  let username, password;
  username = await askQuestion("Usuario: ");
  password = await askQuestion("Senha: ");
  const user = findUser(username, password);
  if (user === null) {
    console.log("Usuario nao encontrado");
  } else {
    printOptions(user);
  }
  rl.close();
}

//Executa a funcao principal
main();
