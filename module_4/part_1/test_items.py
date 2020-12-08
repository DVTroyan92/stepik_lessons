link_page = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

button_add_to_basket_locator = ".btn-add-to-basket"
language_locator = "[selected='selected']"

exp_btn_text_dict = {
    "ru": "Добавить в корзину",
    "en-GB": "Add to basket",
    "es": "Añadir al carrito",
    "fr": "Ajouter au chariot"
}


def test_add_to_basket_button(browser):
    # Data
    expected_lang_code = browser.usr_language
    expected_btn_text = exp_btn_text_dict[expected_lang_code]

    # Arrange
    browser.get(link_page)

    # Act
    button_add_to_basket = browser.find_element_by_css_selector(button_add_to_basket_locator)
    succeful_button_text = button_add_to_basket.text 

    # Assrt

    assert expected_btn_text in succeful_button_text, "button text is different"
