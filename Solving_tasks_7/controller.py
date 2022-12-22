import view
import body
import body_search as search
import body_addition as addition
import body_change as change
import body_delete as delete

def button_click():
    
    result = view.interview_main()                                                                   # Запуск программы
    
    if result == 1: body.call_log_all()                                                              # Показать весь телефонный справочник
    
    if result == 2:                                                                                  # Найти контакт
        search.call_log_search(view.interview_search_1())                                            # Действия с контактом (изменить, удалить)
        body.call_log_all()

    if result == 3:                                                                                  # Добавить новый контакт
        addition.call_log_addition(view.interview_addition())                                        # Добавление и показ обновленный справочник
