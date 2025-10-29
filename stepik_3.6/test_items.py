import time


def test_add_to_cart_button_presence(browser):
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Задержка для визуальной проверки языка (можно убрать после тестирования)
    time.sleep(30)

    # Проверяем наличие кнопки добавления в корзину
    # Используем селектор, который уникален для этой страницы
    add_to_cart_button = browser.find_elements_by_css_selector("button.btn-add-to-basket")

    # Убеждаемся, что кнопка присутствует на странице
    assert len(add_to_cart_button) > 0, "Add to cart button is not found on the page"

    # Дополнительная проверка: кнопка должна быть видимой
    assert add_to_cart_button[0].is_displayed(), "Add to cart button is not visible"

    # Проверяем, что у кнопки есть текст (не пустая)
    button_text = add_to_cart_button[0].text
    assert button_text != "", "Add to cart button has no text"

    print(f"Button text: '{button_text}'")