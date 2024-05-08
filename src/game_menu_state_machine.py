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

    # def get_transitions_to_state(self, state, through_state=None):
    #     transitions = []
    #     if through_state is not None:
    #         # If a through_state is specified, we first check if the current state is the through_state
    #         if self == through_state:
    #             # If the current state is the through_state, we then check if the next_state is the target state
    #             if self.next_state == state:
    #                 transitions.append(self.next_state)
    #             elif self.next_state is not None:
    #                 # If the next_state is not the target state, we recursively call get_transitions_to_state on the next_state
    #                 transitions.extend(self.next_state.get_transitions_to_state(state, through_state))
    #         else:
    #             # If the current state is not the through_state, we recursively call get_transitions_to_state on the next_state
    #             if self.next_state is not None:
    #                 transitions.extend(self.next_state.get_transitions_to_state(state, through_state))
    #     else:
    #         # If no through_state is specified, we proceed as before
    #         if type(self.next_state) == type(state):
    #             transitions.append(self.next_state)
    #         elif self.next_state is not None:
    #             transitions.append(self.next_state)
    #             transitions.extend(self.next_state.get_transitions_to_state(state))
    #     return transitions

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
    
    def select_item(self, target_state):
        current_pos = self.current_menu_item
        target_pos = [type(item) for item in self.menu_items].index(type(target_state))
        total_items = len(self.menu_items)

        if current_pos == target_pos:
            return []

        # Calculate the distance in both directions
        distance_cw = (target_pos - current_pos) % total_items
        distance_ccw = (current_pos - target_pos) % total_items

        # Choose the direction with the shorter distance
        if distance_cw <= distance_ccw:
            return [self.s] * distance_cw
        else:
            return [self.w] * distance_ccw
        
    
    def get_transitions_to_state(self, state):
        transitions = []
        for menu_item in self.menu_items:
            if type(menu_item) == type(state):
                transitions.append(menu_item)
            elif menu_item is not None:
                next_state = menu_item.get_transitions_to_state(state)
                if next_state:
                    transitions.append(menu_item)
                    transitions.extend(next_state)  
                    return transitions
        return transitions
    
    # def get_transitions_to_state(self, state, through_state=None):
    #     transitions = []
    #     for menu_item in self.menu_items:
    #         if through_state is not None:
    #             if self == through_state:
    #                 if menu_item == state:
    #                     transitions.append(menu_item)
    #                 elif menu_item is not None:
    #                     next_state = menu_item.get_transitions_to_state(state, through_state)
    #                     if next_state:
    #                         transitions.append(menu_item)
    #                         transitions.extend(next_state)
    #                         return transitions
    #             else:
    #                 if menu_item is not None:
    #                     next_state = menu_item.get_transitions_to_state(state, through_state)
    #                     if next_state:
    #                         transitions.append(menu_item)
    #                         transitions.extend(next_state)
    #         else:
    #             if type(menu_item) == type(state):
    #                 transitions.append(menu_item)
    #             elif menu_item is not None:
    #                 next_state = menu_item.get_transitions_to_state(state)
    #                 if next_state:
    #                     transitions.append(menu_item)
    #                     transitions.extend(next_state)
    #     return transitions
    
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
            OfflineVersus(),
            OnlineVersus(),
            Variants()
        ])

class MultiplayerPauseMenu(MenuState):
    def __init__(self):
        super().__init__("Multiplayer", [
            UnpauseGame(),
            ChangeLevel(),
            QuitToTitleScreen() #goes to StartingScreen
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

class OnlineVersus(State):
    def __init__(self):
        super().__init__("OnlineVersus")

class Variants(State):
    def __init__(self):
        super().__init__("Variants")

class UnpauseGame(State):
    def __init__(self):
        super().__init__("UnpauseGame")

class ChangeLevel(State):
    def __init__(self):
        super().__init__("ChangeLevel")

class QuitToTitleScreen(State):
    def __init__(self):
        super().__init__("QuitToTitleScreen")

