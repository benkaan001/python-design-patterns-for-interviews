from abc import ABC, abstractmethod

class UIElement(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class WindowsButton(UIElement):
    def render(self) -> str:
        return "Rendering a Windows Button."

class MacOSButton(UIElement):
    def render(self) -> str:
        return "Rendering a MacOS Button."

class LinuxButton(UIElement):
    def render(self) -> str:
        return "Rendering a Linux Button."


class UIElementCreator(ABC):
    @abstractmethod
    def create_button(self) -> UIElement:
        pass

    def display_dialog(self) -> str:
        button = self.create_button()
        result = button.render()
        return f"Displaying dialog with: {result}"

class WindowsCreator(UIElementCreator):
    def create_button(self) -> WindowsButton:
        return WindowsButton()

class MacOSCreator(UIElementCreator):
    def create_button(self) -> MacOSButton:
        return MacOSButton()


class LinuxCreator(UIElementCreator):
    def create_button(self) -> LinuxButton:
        return LinuxButton()

windows_creator = WindowsCreator()
windows_creator.display_dialog()

macos_creator = MacOSCreator()
macos_creator.display_dialog()

linux_creator = LinuxCreator()
linux_creator.display_dialog()

# Output:
# Displaying dialog with: Rendering a Windows Button.
# Displaying dialog with: Rendering a MacOS Button.
# Displaying dialog with: Rendering a Linux Button.
