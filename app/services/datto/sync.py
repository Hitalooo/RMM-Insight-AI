from app.services.datto.browser import DattoBrowser
from app.services.datto.login import DattoLogin
from app.services.datto.mfa import DattoMFA


def run_sync():

    browser = DattoBrowser()

    page = browser.start(headless=False)

    login = DattoLogin(page)

    login.open()

    login.preencher_email()

    login.preencher_senha()

    mfa = DattoMFA(page)

    mfa.autenticar()

    input("\nPressione ENTER para fechar...")

    browser.close()