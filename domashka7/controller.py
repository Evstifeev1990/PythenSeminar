import view
import model
import logger


def button_clik():
    surname = view.vvod_surname()
    name = view.vvod_name()
    phone = view.vvod_phone()
    description = view.vvod_description()
    info = model.init(surname, name, phone, description)
    view.view_spravochnik(info)
    logger.spravochnik_loger(info)
