from abc import ABC, abstractmethod

class Browser(ABC):
    # Interface - Create Search Toolbar
    @abstractmethod
    def create_search_toolbar(self):
        pass

    # Interface - Create Browser Window
    @abstractmethod
    def create_browser_window(self):
        pass

class Messenger(ABC):
    @abstractmethod
    # Interface - Create Messenger Window
    def create_messenger_window(self):
        pass

class VanillaBrowser(Browser):
    # Interface - Create Search Toolbar
    def create_search_toolbar(self):
        print("Search Toolbar Created")

    # Interface - Create Browser Window]
    def create_browser_window(self):
        print("Browser Window Created")

class VanillaMessenger(Messenger):
    # Interface - Create Messenger Window
    def create_messenger_window(self):
        print("Messenger Window Created")

class SecureBrowser(Browser):
    # Abstract Method of the Browser base class
    def create_search_toolbar(self):
        print("Secure Browser - Search Toolbar Created")

    # Abstract Method of the Browser base class
    def create_browser_window(self):
        print("Secure Browser - Browser Window Created")

    def create_incognito_mode(self):
        print("Secure Browser - Incognito Mode Created")

class SecureMessenger(Messenger):

    # Abstract Method of the Messenger base class
    def create_messenger_window(self):
        print("Secure Messenger - Messenger Window Created")

    def create_privacy_filter(self):
        print("Secure Messenger - Privacy Filter Created")

    def disappearing_messages(self):
        print("Secure Messenger - Disappearing Messages Feature Enabled")

class AbstractFactory(ABC):
    @abstractmethod
    def create_browser(self):
        pass

    @abstractmethod
    def create_messenger(self):
        pass

class VanillaProductsFactory(AbstractFactory):
    def create_browser(self):
        return VanillaBrowser()

    def create_messenger(self):
        return VanillaMessenger()

class SecureProductsFactory(AbstractFactory):

    def create_browser(self):
        return SecureBrowser()

    def create_messenger(self):
        return SecureMessenger()

def main():
    for factory in (VanillaProductsFactory(), SecureProductsFactory()):
        product_a = factory.create_browser()
        product_b = factory.create_messenger()
        product_a.create_browser_window()
        product_a.create_search_toolbar()
        product_b.create_messenger_window()

if __name__ == "__main__":
    main()