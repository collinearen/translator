Description of the language in Nowur-Beckus form. Constants in this language can be either integers or fractions. Variable names are limited to one Latin character. This limitation assumes that variables are represented by short identifiers consisting of one Latin letter. This is a language feature that simplifies variable identification and improves code readability.

<программа>::=  <Объявление переменных> <Описание вычислений> <Оператор печати> 
<Описание вычислений> ::= [ <Список присваиваний> ] 
<Объявление переменных> ::= Var <Список переменных> ;
 <Список переменных> ::= <Идент> | <Идент> , <Список переменных> 
<Список присваиваний>::= <Присваивание> | <Присваивание> <Список присваиваний> <Присваивание> ::= <Идент> = <Выражение> ;
<Выражение> ::= <Ун.оп.> <Подвыражение> | <Подвыражение>
<Подвыражение> :: = ( <Выражение> ) | <Операнд> |  < Подвыражение > <Бин.оп.> <Подвыражение>
<Ун.оп.> ::= "-"
<Бин.оп.> ::= "-" | "+" | "*" | "/"
<Операнд> ::= <Идент> | <Const>
<Идент> ::= <Буква> <Идент> | <Буква>
<Const> ::= <Цифра> <Const> | <Цифра>
<Оператор печати>::=Print <Идент>
WHILE <Выражение> DO  <Список операторов>  ENDWHILE
<буква>::= A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T |
U | V | W | X | Y | Z | a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p
q | r | s | t | u | v | w | x | y | z 
<цифра>::= 0|1|2|3|4|5|6|7|8|9


# Formal grammar

Программа:S →DFP.
Описание вычислений: F → [G]
Объявление переменных: D → var V
Список переменных: V → I | I, V
Список присваиваний: G → A | AG
Присваивание: A→ I = E
Выражение: E → UH | H
Подвыражение: H→ (E) | O | HBH
Унарный оператор: U → “-“
Бинарный оператор: B → «-» | «+» | «*»| «/»
Операнд: O → I | Const
Идентификатор: I → LI | I
Константа: Const → N Const | N
Оператор печати: P → Print I
Буква: L → a…z
Цифра: N → 0…9
Конструкция высокого уровня: W → while E do F endwhile







There are four categories of tokens in this program: keywords, delimiters, identifiers, and constants. Only integers can be used as constants.

When developing a store analyzer and generating the corresponding control table, the following main aspects must be taken into account: 1. Lexical analysis is carried out to identify identifiers and constants, their correspondence to the alphabet and the correct form (for example, the numbers 0 or 1). This step reduces the number of grammar rules that need to be checked in the next step, parsing, and ultimately reduces the size of the store parser control table. 2. Variables [var_name] and constants [const_name] are entered by the user and do not have fixed values. Verification is carried out by analyzing whether the collected lexeme belongs to predefined lexeme classes defined at the lexical analysis stage. 3. The store machine interacts with the current symbol of the input string and the stack. For the operational functioning of this analyzer, the following abbreviations are established: - ↕F - pop the top of the stack and push the nonterminal F onto the stack; - → - shift the input string (get the next character of the input string); - ↑ - pop the top of the stack. Combinations of these symbols are applied from left to right in each cell of the control table. 4. If the command ↕ A B C is encountered, where A, B, C are nonterminals of the language, it is interpreted as “pop the top of the stack and push nonterminals A B C onto the stack.” Using these terms, abbreviations and substitution rules, the store analyzer control table is a structured view described in tables 1.1, 1.2, 1.3. 




# The working principle of Dijkstra's algorithm can be described as follows:

1. We go through the original line.
2. If we encounter a number, add it to the output line.
3. If we encounter an operator, we push it onto the stack.
4. If we encounter an operator with a higher priority than the current operator under consideration, we push the operators from the stack to the output line while the operators on the stack have a higher priority.
5. If we encounter an opening parenthesis, we push it onto the stack.
6. If we encounter a closing parenthesis, we pop the statements from the stack onto the output line until we encounter a corresponding opening parenthesis, then remove the opening parenthesis from the stack.

Thus, by step-by-step processing each character of the input string, Dijkstra's algorithm generates an output string, which is an expression in reverse Polish notation (RPR).
