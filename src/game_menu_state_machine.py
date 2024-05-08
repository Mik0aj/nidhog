class State:
    def __init__(self, name):
        self.name = name
        self.next_state = None

    def w(self):
        pass

    def s(self):
        pass

    def enter(self):
        pass

    def get_transitions_to_state(self, state):
        transitions = []
        if type(self.next_state) == type(state):
            transitions.append(self.next_state)
        elif self.next_state is not None:
            transitions.append(self.next_state)
            transitions.extend(self.next_state.get_transitions_to_state(state))
        return transitions



class StartScreen(State):
    def __init__(self):
        super().__init__("Start Screen")
        self.next_state = MainMenu() 

    def w(self):
        pass

    def s(self):
        pass

    def enter(self):
        return self.next_state
    


class MenuState(State):
    def __init__(self, name, menu_items):
        super().__init__(name)
        self.current_menu_item = 0
        self.menu_items = menu_items
        self.next_state = self.menu_items[self.current_menu_item]

    def w(self):
        self.current_menu_item = (self.current_menu_item - 1) % len(self.menu_items)

    def s(self):
        self.current_menu_item = (self.current_menu_item + 1) % len(self.menu_items)

    def enter(self):
        self.next_state = self.menu_items[self.current_menu_item]
        return self.next_state
    
    def get_transitions_to_state(self, state):
        transitions = []
        for menu_item in self.menu_items:
            if type(menu_item) == type(state):
                transitions.append(menu_item)
            elif menu_item is not None:
                next_state = menu_item.get_transitions_to_state(state)
                if next_state:
                    transitions.append(menu_item)
                    transitions.extend(next_state)  # Use extend to add the elements of the list rather than the list itself
                    return transitions
        return transitions
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

class Begin(State):
    def __init__(self):
        super().__init__("Begin")

