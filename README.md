# IronLang

IronLang — это первый аппаратно-ориентированный язык высокого уровня, который может быть полезен для:
- работы с нейронными сетями;
- программирования микроконтроллеров;
- разработки операционных систем.

Сейчас язык находится в активной разработке.

## Основная фишка
Главная особенность IronLang — это абстракции для работы с аппаратным обеспечением. Язык предоставляет удобные конструкции для взаимодействия с различными аппаратными компонентами, такими как GPU, CPU, сенсоры и другие устройства.

## Основные возможности

### Обработчики
Обработчики позволяют использовать различные аппаратные части системы для решения специфических задач. Например:

```plaintext
@gpu.simd$matrix(i: matrix_a) {
    i += 1;
    assign i to #i;
}
```

В этом примере переменная `matrix_a` передается в GPU-обработчик с методом `simd` и типом `matrix`. Каждый элемент матрицы обрабатывается отдельным мини-ядром графического процессора: к каждому элементу прибавляется 1, и результат присваивается соответствующему элементу в памяти. В итоге все элементы матрицы `matrix_a` увеличиваются на 1.

### Аппаратные прерывания и события
IronLang позволяет обрабатывать прерывания и события, запрашивая данные от устройств. Например:

```plaintext
@interrupt.keyboard_handler -> keyid {
    if (keyid == 'a') {
        print("Клавиша 'a' нажата!");
    }
}
```

Здесь обработчик прерывания от клавиатуры проверяет, была ли нажата клавиша `a`, и выводит сообщение в случае успеха.

### Аппаратные ловушки (traps)
Ловушки предназначены для обработки критических ситуаций, таких как ошибки ввода-вывода или сбои в работе устройств. Например:

```plaintext
@trap(IOError) {
    print("Ошибка ввода-вывода!");
}
```

В этом примере при возникновении ошибки ввода-вывода выводится соответствующее сообщение.

### Аппаратные логи событий
IronLang предоставляет встроенные средства для логирования событий, что упрощает отладку и мониторинг работы системы. Например:

```plaintext
@log(event) {
    file.write(event);
}
```

Здесь событие записывается в файл для дальнейшего анализа.

---

## Текущий статус
IronLang находится в стадии активной разработки. Мы работаем над добавлением новых функций и улучшением существующих возможностей.

---

## Как использовать
Чтобы начать использовать IronLang, следуйте инструкциям по установке и настройке (скоро будет доступно).

---

## Лицензия
IronLang распространяется под лицензией [MIT](LICENSE).
