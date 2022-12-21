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
        if (search.call_log_search(view.interview_search_1())) > 0:                                  # Что с этим контактом сделать
            
            if (view.interview_change_1()) == 1:                                                       # Изменить
                change.call_log_change(view.interview_search_2(), view.interview_change_2())         # Изменение конкретного параметра
                print('\n')
                body.call_log_all()                                                                  # Показать обновленный справочник
            
            if (view.interview_change_1()) == 2:                                                       # Удалить
                delete.call_log_delete(view.interview_search_2())
                print('\n')
                body.call_log_all()                                                                  # Показать обновленный справочник
    
    if result == 3:                                                                                  # Добавить новый контакт
        addition.call_log_addition(view.interview_addition())                                        # Добавление и показ обновленный справочник
