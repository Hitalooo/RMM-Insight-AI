import os

from dotenv import load_dotenv

load_dotenv()


class DattoLogin:

    def __init__(self, page):
        self.page = page

    def open(self):

        print("✓ Abrindo Datto...")

        self.page.goto(
            os.getenv("DATTO_URL"),
            wait_until="networkidle"
        )

        print("✓ Página carregada.")

    def preencher_email(self):

        print("✓ Preenchendo e-mail...")

        self.page.get_by_role(
            "textbox",
            name="Email"
        ).fill(
            os.getenv("DATTO_USER")
        )

        self.page.get_by_role(
            "button",
            name="Continue"
        ).click()

        self.page.wait_for_selector("#form_password")

        print("✓ Tela da senha carregada.")

    def preencher_senha(self):

        print("✓ Preenchendo senha...")

        self.page.get_by_role(
            "textbox",
            name="Password"
        ).fill(
            os.getenv("DATTO_PASSWORD")
        )

        self.page.get_by_role(
            "button",
            name="Continue"
        ).click()

        print("✓ Login enviado.")