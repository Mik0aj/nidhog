class State:
    def __init__(self, name):
        self.name = name

    def w(self):
        pass

    def s(self):
        pass

    def enter(self):
        pass

class StartScreen(State):
    def __init__(self):
        super().__init__("Start Screen")

    def w(self):
        pass

    def s(self):
        pass

    def enter(self):
        return MainMenu()

class MenuState(State):
    def __init__(self, name, menu_items):
        super().__init__(name)
        self.current_menu_item = 0
        self.menu_items = menu_items

    def w(self):
        self.current_menu_item = (self.current_menu_item + 1) % len(self.menu_items)

    def s(self):
        self.current_menu_item = (self.current_menu_item - 1) % len(self.menu_items)

    def enter(self):
        return self.menu_items[self.current_menu_item]

class MainMenu(MenuState):
    def __init__(self):
        super().__init__("Main Menu", [
            Multiplayer(),
            Tournament(),
            Options(),
            Credits(),
            QuitToDesktop(),
            HowToPlay(),
            SinglePlayer()
        ])

class Multiplayer(MenuState):
    def __init__(self):
        super().__init__("Multiplayer", [
            OfflineVersus()
        ])

class OfflineVersus(State):
    def __init__(self):
        super().__init__("Offline Versus")

class SinglePlayer(State):
    def __init__(self):
        super().__init__("Single Player")



class Tournament(State):
    def __init__(self):
        super().__init__("Tournament")



class Options(State):
    def __init__(self):
        super().__init__("Options")



class Credits(State):
    def __init__(self):
        super().__init__("Credits")



class QuitToDesktop(State):
    def __init__(self):
        super().__init__("QuitToDesktop")



class HowToPlay(State):
    def __init__(self):
        super().__init__("HowToPlay")

