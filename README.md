# TeaWeb
![image](https://github.com/Puerh0x1/TeaWeb/assets/162372951/c2a9794b-698c-4ae0-ae9e-fd131e703d6b)

### Ultrafast Modern, Customizable Multi-threaded Subdomains and Directory Links Fuzzer

Сверх-быстрый современный кастомизируемый многопоточный фаззер субдоменов и директорий.


## Особенности

- **-m Режим фаззинга.**  
  Режимы:
  - фаззинг директорий или субдоменов  (-m fuzz)

- **-w Файл со словарем** (-w file.txt)

- **-u URL** (-u example.com)  
  Для фаззинга замените ту часть, которую необходимо на _TEA_  
  Пример: `https://_TEA_.example.com | https://example.com/_TEA_`

- **-ft Методы фаззинга.**  
  - requests (-ft requests) - обычные GET запросы  
  - hostheader (-ft hostheader) - заголовок HOST: в запросах (лучший вариант для поддоменов, особенно в локальных сетях)  
  По умолчанию: hostheader

- **-t таймаут запроса** (-t 2)  
  По умолчанию: 1 секунда (1)

- **-T threads** (-T 10)  
  По умолчанию: 5

- **-v verbose mode**  
  - all - выводит все логи (и успешные и нет)  
  - good - выводит только верные ссылки  
  Пример: -v good  
  По умолчанию: good

- **-gc статусы ответов** по которым запросы будут считаться успешными (ссылки валидными)  
  Пример: -gc 200,301,500  
  Без пробелов.  
  По умолчанию: 200,201,202,203,204,205,206,300,301,302,303,304,500,502,503,504

![image](https://github.com/Puerh0x1/TeaWeb/assets/162372951/6c096137-65e5-43db-80bb-c1a3939f0452)

 
## English Documentation

### Features

- **-m Fuzzing mode.**  
  Fuzzing modes:
  - Subdomains or links fuzzing (-m fuzz)

- **-w Wordlist file** (-w file.txt)

- **-u URL** (-u example.com)  
  For subdomains fuzzing mark the part you want to fuzz with the symbol _TEA_  
  Example: `https://_TEA_.example.com | https://example.com/_TEA_`

- **-ft Fuzzing method.**  
  - requests (-ft requests) - simple GET requests  
  - hostheader (-ft hostheader) - making header HOST: in requests (best for local networks)  
  Default: hostheader

- **-t Request timeout** in seconds (-t 2)  
  Default: 1 second (1)

- **-T Threads** (-T 10)  
  Default: 5

- **-v Verbose mode**  
  - all - prints all requests (bad and good)  
  - good - prints only good requests  
  Example: -v good  
  Default: good

- **-gc Requests goodcodes** (response codes of good results)  
  Example: -gc 200,301,500  
  No Space.  
  Default: 200,201,202,203,204,205,206,300,301,302,303,304,500,502,503,504

![image](https://github.com/Puerh0x1/TeaWeb/assets/162372951/6c096137-65e5-43db-80bb-c1a3939f0452)

