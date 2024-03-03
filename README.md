Description of the language in Nowur-Beckus form. Constants in this language can be either integers or fractions. Variable names are limited to one Latin character. This limitation assumes that variables are represented by short identifiers consisting of one Latin letter. This is a language feature that simplifies variable identification and improves code readability.

<img src="https://github.com/collinearen/source/blob/main/Снимок%20экрана%202024-03-03%20в%2020.49.10.png"> 

# Formal grammar

<img src="https://github.com/collinearen/source/blob/main/Снимок%20экрана%202024-03-03%20в%2020.49.15.png"> 


There are four categories of tokens in this program: keywords, delimiters, identifiers, and constants. Only integers can be used as constants.

When developing a store analyzer and generating the corresponding control table, the following main aspects must be taken into account: 1. Lexical analysis is carried out to identify identifiers and constants, their correspondence to the alphabet and the correct form (for example, the numbers 0 or 1). This step reduces the number of grammar rules that need to be checked in the next step, parsing, and ultimately reduces the size of the store parser control table. 2. Variables [var_name] and constants [const_name] are entered by the user and do not have fixed values. Verification is carried out by analyzing whether the collected lexeme belongs to predefined lexeme classes defined at the lexical analysis stage. 3. The store machine interacts with the current symbol of the input string and the stack. For the operational functioning of this analyzer, the following abbreviations are established: - ↕F - pop the top of the stack and push the nonterminal F onto the stack; - → - shift the input string (get the next character of the input string); - ↑ - pop the top of the stack. Combinations of these symbols are applied from left to right in each cell of the control table. 4. If the command ↕ A B C is encountered, where A, B, C are nonterminals of the language, it is interpreted as “pop the top of the stack and push nonterminals A B C onto the stack.” Using these terms, abbreviations and substitution rules, the store analyzer control table is a structured view described in tables 1.1, 1.2, 1.3. 


## Variable declaration search machine
<img src="https://github.com/collinearen/source/blob/main/Снимок%20экрана%202024-03-03%20в%2020.47.27.png"> 


## Program code search machine
<img src="https://github.com/collinearen/source/blob/main/Снимок%20экрана%202024-03-03%20в%2020.47.33.png"> 

## while loop automaton
<img src="https://github.com/collinearen/source/blob/main/Снимок%20экрана%202024-03-03%20в%2020.47.40.png"> 



# The working principle of Dijkstra's algorithm can be described as follows:

1. We go through the original line.
2. If we encounter a number, add it to the output line.
3. If we encounter an operator, we push it onto the stack.
4. If we encounter an operator with a higher priority than the current operator under consideration, we push the operators from the stack to the output line while the operators on the stack have a higher priority.
5. If we encounter an opening parenthesis, we push it onto the stack.
6. If we encounter a closing parenthesis, we pop the statements from the stack onto the output line until we encounter a corresponding opening parenthesis, then remove the opening parenthesis from the stack.

Thus, by step-by-step processing each character of the input string, Dijkstra's algorithm generates an output string, which is an expression in reverse Polish notation (RPR).



The presented set of functions and code constitutes a syntax analyzer for compiling source code into a language corresponding to the proposed grammar. The program is divided into several functions, each of which is responsible for a specific aspect of code analysis.

The analyzer is based on the top-down parsing method, in which the analyzer starts from the root of the syntax tree and recursively descends to the leaves. Each function in the analyzer performs specific analysis steps, checking that the current state of the code conforms to certain grammar rules.

The main idea of ​​the analyzer is to sequentially check each line of code and split it into components according to the rules of grammar. If syntax errors or code structure inconsistencies with grammar rules are detected, the program displays appropriate error messages.

In general, the parser is a key component of the compilation process, which allows you to convert source code in a special programming language into a sequence of instructions that the computer can understand for further execution.



1)   Функция analyze.

Этот код представляет собой простой механизм анализа, который продолжает проверку кода в цикле до тех пор, пока не встретит ошибки или не завершит успешно. В зависимости от результата анализа, программа вставляет соответствующие сообщения в текстовый виджет text_mistakes.


2)   Функция Parser

Этот алгоритм представляет собой часть процесса анализа кода программы в рамках компилятора. Он обеспечивает последовательный анализ исходного текста с целью выявления структурных элементов и проверки их корректности согласно заданной грамматике. В конечном итоге, алгоритм определяет, соответствует ли входной код установленным правилам и может ли быть далее скомпилирован для последующего выполнения программы.


  

3)   Функция nonterminal_d()

Эта функция предназначена для анализа и обработки раздела кода, отвечающего за объявление переменных “var” в рамках компилятора. Раздел var предваряет начало основного кода программы “begin”


  

4)   Функция nonterminal_v()

Эта функция предназначена для обработки объявлений переменных в исходном коде. Играет ключевую роль в обработке частей кода, связанных с объявлением переменных, и выполняет необходимые проверки и анализы для обеспечения корректности структуры программы.


  

5)   Функция nonterminal_i

Эта функция выполняет важную роль в анализе кода, отвечая за обработку идентификаторов, и записывает информацию о них в соответствующий файл при необходимости.



  

6)   Функция parsing_literals

Предназначена для анализа литералов в исходном коде.

Она проверяет, установлен ли флаг literals_flag. Если да, то проверяется, присутствует ли текущий литерал в словаре literal. Если литерал найден, его эквивалент в языке Python добавляется в переменную python_code, а также литерал добавляется в список micro_poliz, если он является частью полиза. Затем флаг literals_flag устанавливается в False, чтобы остановить дальнейший поиск литералов.


7)   Функция Type

Данный код предназначен для обработки типов переменных в компиляторе. При вызове этого метода он пытается определить тип переменной на основе текущего символа в исходном коде. Если определение проходит успешно, программа добавляет соответствующий код Python и, если тип представляет собой список, добавляет его в micro-poliz. В случае ошибки типа, программа добавляет сообщение об ошибке в текст ошибок.


  

8) Функция nonterminal_f

Представляет собой один из нетерминалов грамматики и отвечает за анализ конструкции кода до следующего ключевого слова или символа.


  
9) Функция nonterminal_g

Функция nonterminal_g является частью анализатора синтаксиса, который следует грамматике языка программирования. Она отвечает за анализ определенной части кода, проверяя наличие определенных конструкций и синтаксических элементов.

Таким образом, она является частью механизма анализа синтаксиса, который последовательно проверяет различные конструкции программы в соответствии с грамматикой языка программирования.


  

10) Функция nonterminal_a

Данная функция является частью анализатора синтаксиса, который проверяет соответствие частей кода грамматике языка программирования.


         11) Функция Equality (Проверка на равенство)

Функция Equality предназначена для проверки, является ли текущий символ оператором присваивания.


  

12) Функция nonterminal_e

Эта функция используется для анализа частей кода и принимает решение на основе синтаксических правил грамматики. Необходимая часть более общего алгоритма разбора кода.


  

13) Функция nonterminal_h

Эта функция является частью анализатора синтаксиса и отвечает за анализ конструкций, содержащих выражения в скобках “)” и “(”


  

14) Функция nonterminal_b

Эта функция, вероятно, используется при разборе выражений и операций с бинарными операторами в коде.


  

15) Функция nonterminal_o

Вызывает функцию nonterminal_o для разбора токена, который, вероятно, представляет оператор (например, присваивание или оператор печати).

Устанавливает флаг end_flag в True, так как достигнут символ конца строки (;\n).

Проверяет, что текущий токен - это именно символ конца строки.

Собирает из микро-Poliz те элементы, которые относятся к литералам, и формирует из них строку poliz_on_sending_new.

Добавляет полученную строку poliz_on_sending_new к основной строке poliz.

Очищает микро-Poliz и устанавливает флаги и счетчики в начальное состояние для новой строки кода.

Возвращает True для сигнала об успешном завершении обработки строки кода.



  

16) Функция nonterminal_const

Проверяет, является ли текущий токен числовой константой (Const). В случае успешного соответствия добавляет его значение как строку к python_code и также добавляет его в micro-poliz.

  

17) Функция nonterminal_u

Проверяет, является ли текущий токен унарным оператором -. Если это так, то добавляет символ - к python_code и возвращает True, указывая на успешное распознавание унарного оператора. В противном случае, возвращает False.


  
18) Функция play_py

Создает файл results.py и записывает в него сгенерированный Python-код.

Запускает выполнение файла results.py с использованием функции exec.

Вставляет сгенерированный Python-код в виджет text_end_python_code.

Создает файл poliz.txt и записывает в него содержимое переменной poliz.

Вставляет содержимое переменной poliz в виджет poliz_text.

  

19) Функция nonterminal_p

Функция (nonterminal_p) проверяет, начинается ли текущая строка с ключевого слова "print" и отвечает за анализ и генерацию кода для оператора печати (print) в исходном тексте. Если оператор печати обнаружен и выражение для печати успешно найдено, то код оператора печати сгенерирован. Если обнаружена какая-либо ошибка в структуре оператора печати, функция возвращает False, указывая на ошибку анализа.


20) Функция nonterminal_w

Анализирует конструкцию while в коде и формирует соответствующий Python код, а также записывает маркеры в полиз для последующего использования.




# Example of how the program works

<img src="https://github.com/collinearen/source/blob/main/Снимок%20экрана%202024-03-03%20в%2021.03.51.png">

