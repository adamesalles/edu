-- Documentação SQLite: https://www.sqlite.org/datatype3.html
-- Tutorial SQLite: https://www.sqlitetutorial.net/
-- Tutorial de SQLite feito por Bruno Cuconato.

-- Neste documento vamos fazer um tutorial de SQL & SQLite usando
-- como exemplo um aplicativo de acompanhamento de tarefas.

-- Comandos SQLite começam com um ponto:
.headers on
.echo on
-- set table format
.mode markdown

-- Criar tabela para as tarefas
CREATE TABLE task(id, description, complete);

-- Inserir valores na tabela
INSERT INTO task (id, description, complete)
VALUES
  (1, 'Build website from scratch', TRUE),
  (2, 'Design logo for new product', TRUE),
  (3, 'Write content for blog post', TRUE),
  (4, 'Setup server configurations', FALSE),
  (5, 'Research competitors in market', FALSE),
  (6, 'Develop marketing strategy', TRUE),
  (7, 'Edit video for YouTube channel', FALSE),
  (8, 'Analyze website traffic', TRUE);

-- Mostrar todos os valores da tabela
SELECT id, description, complete FROM task;

-- Podemos inserir dados incompletos na tabela
INSERT INTO task (description, complete)
VALUES
  ('Complete presentation', FALSE);

-- Veja a nova linha inserida:
SELECT id, description, complete FROM task;

-- Para impedir colunas vazias, podemos criar uma nova tabela com
-- restrições de não-vazio (NOT NULL) nas suas colunas
CREATE TABLE task_not_null(
  id INTEGER NOT NULL,
  description TEXT NOT NULL,
  complete INTEGER NOT NULL
  );

-- Agora não podemos mais omitir o id de uma entrada/linha
-- (nem omitir description, nem complete)
INSERT INTO task_not_null (description, complete)
  VALUES ('Build website from scratch', FALSE); -- dá erro

-- Podemos apagar/deletar uma tabela
DROP TABLE IF EXISTS task_not_null;

-- Em geral, toda tabela deve ter uma chave primária. A chave
-- primária de uma tabela é o conjunto mínimo de colunas que serve
-- para identificar uma linha da tabela. Neste caso, nossa chave
-- primária é a coluna id. Se alguém nos dá um id, nós sabemos a
-- qual linha da tabela a pessoa está falando (duas linhas
-- diferentes não podem ter o mesmo id).
CREATE TABLE task_with_pk(
  id INTEGER PRIMARY KEY,
  description TEXT NOT NULL,
  complete INTEGER NOT NULL
  );

-- Ao declarmos uma única coluna da tabela como sendo a chave
-- primária, ela automaticamente recebe as restrições NOT NULL e
-- UNIQUE
INSERT INTO task_with_pk (id, description, complete)
VALUES
  (0, 'Regar as plantas', FALSE),
  (0, 'Fazer apresentação', FALSE); -- dá erro, id tem de ser único

---- Também podemos especificar a chave primária como abaixo:
CREATE TABLE task_with_pk2(
  id INTEGER,
  description TEXT NOT NULL,
  complete INTEGER NOT NULL,
  PRIMARY KEY(id) -- colocamos a restrição de chave primária separado
  );

DROP TABLE IF EXISTS task_with_pk2; -- limpando


-- Uma vantagem de declararmos uma coluna de tipo INTEGER como a
-- chave primária é que os valores dessa coluna podem ser
-- determinados automaticamente, e assim podemos inserir novas
-- entradas na tabela sem especificá-los:
INSERT INTO task_with_pk (description, complete)
VALUES
  ('Build website from scratch', 0),
  ('Design logo for new product', 1),
  ('Write content for blog post', 1),
  ('Setup server configurations', 0),
  ('Research competitors in market', 0),
  ('Develop marketing strategy', 1),
  ('Edit video for YouTube channel', 0),
  ('Analyze website traffic', 1);

-- Veja:
SELECT id, description, complete
FROM task_with_pk;

-- Naturalmente, nada nos impede de especificar o id (desde que ele
-- seja diferente dos já existentes, e não-vazio)
INSERT INTO task_with_pk (id, description, complete)
VALUES
  (43984, 'Save a mockingbird', FALSE);

-- Podemos filtrar resultados de nossas queries usando a
-- palavra-chave WHERE

-- Aqui listamos todas as tarefas que estão completas
SELECT description
FROM task_with_pk
WHERE complete;

-- Podemos listar as tarefas que não estão completas usando o
-- operador de negação NOT
SELECT description
FROM task_with_pk
WHERE NOT complete;

-- Além de NOT, também podemos usar outros operadores booleanos
-- OR, AND

-- Também podemos ordenar resultados
SELECT description, complete
FROM task_with_pk
ORDER BY description DESC; -- ordem decrescente
-- para ordem crescente, usar ASC

SELECT description, complete
FROM task_with_pk
ORDER BY description; -- padrão da ordem é crescente

DROP TABLE IF EXISTS task_with_pk; -- limpando

-- Vamos criar uma nova tabela que inclui a informação sobre a
-- pessoa responsável por uma tarefa
CREATE TABLE task_with_owners (
  id INTEGER PRIMARY KEY,
  description TEXT NOT NULL,
  complete INTEGER NOT NULL,
  owner TEXT
);

INSERT INTO task_with_owners (description, complete, owner)
VALUES
  ('Build website from scratch', TRUE, 'Dwight'),
  ('Design logo for new product', TRUE, 'Philip'),
  ('Write content for blog post', TRUE, 'Anna'),
  ('Setup server configurations', FALSE, 'Peter'),
  ('Research competitors in market', FALSE, null),
  ('Develop marketing strategy', TRUE, 'Philip'),
  ('Edit video for YouTube channel', FALSE, 'Peter'),
  ('Analyze website traffic', TRUE, 'Anna');

-- Para selecionar todos os responsáveis por tarefas, fazemos:

SELECT owner -- com duplicatas
  FROM task_with_owners;

SELECT DISTINCT owner -- sem duplicatas
  FROM task_with_owners
  WHERE owner IS NOT NULL;  -- excluindo vazios/nulos

-- Podemos usar a palavra-chave LIMIT para limitar o número de
-- linhas retornadas
SELECT description, owner
FROM task_with_owners
LIMIT 2;

-- É possível pesquisar quais são as tarefas de uma determinada
-- pessoa só
SELECT id, description
FROM task_with_owners
WHERE owner = 'Peter';

-- Bem como é possível perguntar quais as tarefas de um grupo de
-- pessoas
SELECT id, description
FROM task_with_owners
WHERE owner IN ('Dwight', 'Peter', 'Anna');

DROP TABLE IF EXISTS task_with_owners; -- limpando

-- Para incluir informações sobre os responsáveis de tarefas, é
-- melhor separá-los em uma tabela própria
CREATE TABLE employee (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  team TEXT
);

DROP TABLE IF EXISTS task;
CREATE TABLE task (
  id INTEGER PRIMARY KEY,
  description TEXT NOT NULL,
  complete INTEGER NOT NULL,
  owner INTEGER -- se refere ao id da tabela employee
);

INSERT INTO employee (name, team)
VALUES
  ('Dwight', 'Engineering'),
  ('Philip', 'Design'),
  ('Anna', 'Sales'),
  ('Peter', 'Engineering');

INSERT INTO task (description, complete, owner)
VALUES
  ('Build website from scratch', TRUE, 1),
  ('Design logo for new product', TRUE, 2),
  ('Write content for blog post', TRUE, 3),
  ('Setup server configurations', FALSE, 4),
  ('Research competitors in market', FALSE, null),
  ('Develop marketing strategy', TRUE, 2),
  ('Edit video for YouTube channel', FALSE, 4),
  ('Analyze website traffic', TRUE, 3);

-- Nada nos impede de inserir uma tarefa com um responsável que não
-- existe na tabela employee
INSERT INTO task(description, complete, owner)
VALUES ('Give presentation', FALSE, 99);

-- Podemos selecionar somente as as tarefas cujos responsáveis
-- existem
SELECT description, complete
FROM task
WHERE EXISTS (SELECT employee.id FROM employee WHERE employee.id = task.owner);
-- ou equivalentemente:
SELECT description, complete
FROM task
WHERE owner IN (SELECT id FROM employee);

-- Os resultados dessas duas últimas queries são equivalentes, mas
-- elas não são iguais em termos de tempo de resposta. Nós podemos
-- ver isso facilmente ativando o comando
.eqp on
-- e rodando as queries novamente. Esse comando (eqp = explain query
-- plan) explica em alto nível como uma determina query é
-- executada. Nota-se que os query plans das últimas queries são
-- diferentes, mesmo que os resultados sejam iguais.
.eqp off

-- apagar todas as tarefas cujos responsáveis não existem na tabela
-- employee
DELETE FROM task
WHERE owner NOT IN (SELECT DISTINCT id FROM employee);

-- Para evitar referências inexistentes, podemos dizer ao SQLite
-- explicitamente ao que uma coluna se refere. FOREIGN KEY é uma
-- chave primária de uma outra tabela, e se especificarmos que uma
-- coluna de nossa tabela se refere a uma foreign key, o SQLite pode
-- verificar isso quando inserimos dados, rejeitando entradas
-- inválidas
DROP TABLE IF EXISTS task;
CREATE TABLE task (
  id INTEGER PRIMARY KEY,
  description TEXT NOT NULL,
  complete INTEGER NOT NULL,
  owner INTEGER,
  FOREIGN KEY(owner)
   REFERENCES employee(id)
);

-- por padrão o SQLite não checa restrições de FOREIGN KEY, mas
-- podemos/devemos ativar essa checagem
PRAGMA foreign_keys = ON;

-- inserir tarefas cujos responsáveis não existem agora dá erro:
INSERT INTO task(description, complete, owner)
VALUES ('Give presentation', FALSE, 99);

INSERT INTO task (description, complete, owner)
VALUES
  ('Build website from scratch', TRUE, 1),
  ('Design logo for new product', TRUE, 2),
  ('Write content for blog post', TRUE, 3),
  ('Setup server configurations', FALSE, 4),
  ('Research competitors in market', FALSE, null),
  ('Develop marketing strategy', TRUE, 2),
  ('Edit video for YouTube channel', FALSE, 4),
  ('Analyze website traffic', TRUE, 3);

-- Podemos verificar que não há tarefas cujos responsáveis não
-- existem, se quisermos
SELECT description, complete
FROM task
WHERE owner IS NOT NULL
  AND NOT EXISTS (SELECT id FROM employee WHERE employee.id = task.owner);
-- ou, equivalentemente:
SELECT description, complete
FROM task
WHERE owner IS NOT NULL
  AND owner NOT IN (SELECT id FROM employee);

-- Como pegar as tarefas e seus responsáveis?

-- não é assim
SELECT description, name, complete
FROM task, employee;

-- essa query é equivalente à anterior, e faz o produto cartesiano
-- das tabelas, que não é o que queremos
SELECT description, name, complete
FROM task CROSS JOIN employee;

-- para pegar as tarefas e seus responsáveis precisamos garantir que
-- o nome da pessoa responsável é o que corresponde ao id do
-- responsável pela tarefa
SELECT description, name AS owner_name, complete
FROM task, employee
WHERE owner = employee.id; -- é necessário qualificar
                           -- nomes de colunas quando
                           -- são ambíguos

-- essa query é equivalente à anterior
SELECT description, complete, name
FROM task INNER JOIN employee ON owner = employee.id;

-- E como selecionar todas as tarefas e seus responsáveis, incluindo
-- as que não tem responsáveis?
SELECT description, complete, name
FROM task LEFT JOIN employee ON owner = employee.id;

-- Um inner join faz a interseção de duas tabelas, ao passo que o
-- left join faz a união de uma tabela com a interseção das duas
-- tabelas (tente visualizar os diagramas de Venn de cada situação)

-- Podemos contar quantas tarefas cada empregado tem usando COUNT e
-- GROUP BY
SELECT name, COUNT(task.id) AS nr_tasks
FROM employee INNER JOIN task ON employee.id = owner
GROUP BY employee.id;

-- COUNT é uma forma de agregação; o SQLite oferece outras, veja a
-- lista completa em
-- https://www.sqlite.org/lang_aggfunc.html#aggfunclist
--- Note que outras bases de dados podem tem outras funções de
--- agregação

-- Outra agregação possível é listar as tarefas de cada empregado
SELECT name, GROUP_CONCAT(task.description, ', ') AS employee_tasks
FROM employee, task
WHERE employee.id = task.owner
GROUP BY employee.id;

-- Também podemos fazer a mesma coisa usando uma sub-query
SELECT
  name,
  (SELECT GROUP_CONCAT(description, ', ')
   FROM task
   WHERE owner = employee.id
   GROUP BY owner) AS employee_tasks
FROM employee;

---- Ou mesmo usando Common Table Expressions (CTE)
WITH employee_tasks
  AS (SELECT owner, GROUP_CONCAT(description, ', ') AS tasks
      FROM task
      GROUP BY owner)
SELECT name, tasks
FROM employee, employee_tasks
WHERE employee.id = employee_tasks.owner;

-- Note que apesar dos resultados serem equivalentes, os tempos de
-- resposta esperados são diferentes. Novamente, podemos ver isso
-- usando o comando
.eqp on

-- Uma coisa que afeta a performance da última query é a existência
-- de um índice sobre a coluna owner da tabela task
CREATE INDEX task_owner_index
ON task(owner);

-- Note que o plano da última query é diferente se o índice existe
-- ou não. Você pode apagar um índice usando o comando
DROP INDEX task_owner_index;

-- A diferença da existência ou inexistência de um índice é
-- semelhante a usarmos um dicionário ou uma lista para guardar as
-- tarefas, se não estivéssemos usando uma base de dados. Se
-- guardamos as tarefas em uma única lista, precisamos fazer um loop
-- sobre todas as tarefas para filtrar às tarefas referentes a uma
-- única pessoa. Se usamos um dicionário cujas chaves são as pessoas
-- responsáveis e os valores correspondentes são as suas tarefas,
-- obtemos todas as tarefas de uma pessoa com um único lookup.

--- Como filtrar resultados de um agrupamento ou agregação?
-- Não podemos usar a clásula WHERE pois uma agregação não está
-- disponível neste ponto da query.

-- Se estamos tentando listar os empregados que tem mais de uma
-- tarefa temos um erro ao tentar usar WHERE para filtrar o
-- resultado da agregação:
SELECT name, COUNT(task.id) AS nr_tasks
FROM employee INNER JOIN task ON employee.id = owner
WHERE nr_tasks > 1
GROUP BY employee.id;

-- Para filtrar no resultado de um agrupamento ou agregação, usamos
-- a cláusula HAVING:
SELECT name, COUNT(task.id) AS nr_tasks
FROM employee INNER JOIN task ON employee.id = owner
GROUP BY employee.id
HAVING nr_tasks > 1;

-- Funções de tempo: https://www.sqlite.org/lang_datefunc.html

-- date(time-value, modifier, modifier, ...)
-- time(time-value, modifier, modifier, ...)
-- datetime(time-value, modifier, modifier, ...)
-- julianday(time-value, modifier, modifier, ...)
-- unixepoch(time-value, modifier, modifier, ...)
-- strftime(format, time-value, modifier, modifier, ...)

-- Tecnicamente, poderíamos usar DELETE + INSERT, mas o UPDATE tem a
-- vantagem de não mudar o ID do dado, o que quebraria referências a
-- ele
UPDATE task
SET complete = TRUE
WHERE id = 4;

-- Outro problema de usar DELETE + INSERT ao invés de um update é
-- que as duas queries são independentes, e portanto uma pode falhar
-- e a outra não, causando inconsistências nos dados. Veja o exemplo
-- abaixo, em que queremos colocar um responsável para a tarefa 5
-- que até aqui não tem um responsável:
DELETE FROM task
WHERE id = 5;
INSERT INTO task(description, complete, owner)
VALUES ('Research competitors in market', FALSE, 42);
-- Infelizmente, inserimos um id de responsável inválido, e portanto
-- o INSERT falhou; o DELETE funcionou perfeitamente, no entanto, e
-- por isso acabamos perdendo dados: a tarefa 5 foi apagada sem ser
-- substituída.

-- Vamos restaurá-la:
INSERT INTO task(id, description, complete, owner)
VALUES (5, 'Research competitors in market', FALSE, null);

-- Não perderíamos dados se fizéssemos um UPDATE:
UPDATE task
SET owner = 42
WHERE id = 5;
-- A query simplesmente falha, e é como se não tivéssemos feito
-- nada.

-- É possível superar esse problema de independência de queries que
-- deveriam ser dependentes: podemos usar transações. Transações
-- fazem com que uma série de queries sejam vistas como uma única
-- unidade de trabalho indivisível: ou todas são bem-sucedidas (sem
-- erros), ou todas falham.

-- Para iniciar uma transação, fazemos:
BEGIN TRANSACTION;
-- e então escrevemos nossas queries:
DELETE FROM task
WHERE id = 5;
INSERT INTO task(description, complete, owner)
VALUES ('Research competitors in market', FALSE, 42);
-- como a última query dá erro, podemos fazer um ROLLBACK
ROLLBACK TRANSACTION;
-- O rollback restaura a base de dados para um estado em que nenhuma
-- das queries da transação fez modificação alguma. Nesse caso, é
-- como se voltássemos no tempo, mas note que bases de dados podem
-- atender a várias queries ao mesmo tempo, e portanto não
-- necessariamente o resultado de
SELECT description, owner FROM task;
-- seria o mesmo entre antes do BEGIN TRANSACTION e depois do
-- ROLLBACK TRANSACTION. O que é garantido é que depois de um
-- rollback os efeitos das queries da transação são desfeitos.

-- Quando as queries de uma transação completam sem erros, queremos
-- finalizá-la para que as queries seguintes não façam todas parte
-- de uma transação enorme. Para isso usamos COMMIT
-- TRANSACTION. Aqui colocamos um responsável existente para a
-- tarefa 5 e finalizamos a transação:
BEGIN TRANSACTION;
DELETE FROM task
WHERE id = 5;
INSERT INTO task(id, description, complete, owner)
VALUES (5, 'Research competitors in market', FALSE, 1);
COMMIT TRANSACTION; -- termina a transação atual


-- Até aqui temos trabalhado com uma base de dados em memória
-- transiente/volátil, que é perdida/apagada sempre que o saímos do
-- console SQLite. Podemos salvá-la para um arquivo em memória
-- não-volátil persistente assim:
.backup "tasks.db"

-- Se fecharmos o console SQLite depois disso, não perdemos nada:
-- podemos abrir o arquivo e termos todos os nossos dados de volta:
.open "tasks.db"
-- Esse arquivo .db é portátil, e pode ser transferido para qualquer
-- outro computador (para backup, para compartilhamento de
-- informações) e aberto normalmente por uma outra instalação de
-- SQLite, sem problemas.
SELECT name, GROUP_CONCAT(task.description, ', ') AS employee_tasks
FROM employee, task
WHERE employee.id = task.owner
GROUP BY employee.id;
