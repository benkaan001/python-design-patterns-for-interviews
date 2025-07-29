# Challenge: Cross-Platform UI Elements

## 📝 Scenario

You are building an application that needs to display different UI elements (e.g., buttons, checkboxes) that might look and behave slightly differently depending on the operating system (e.g., Windows, MacOS, Linux). You want to ensure that your application code that *uses* these UI elements doesn't need to know the specific OS-dependent implementation.

This means if you have a part of your application that needs to display a "Save" button, it should just ask for a button, and the system should provide the correct OS-specific button (Windows-style, MacOS-style, etc.) without the "Save" button logic needing to know about `WindowsButton` or `MacOSButton` directly.

## 🚀 Your Task

Implement a system using the **Factory Method Pattern** to create cross-platform UI elements.

### Requirements:

1. **Product (Abstract):**
   * Define an abstract class `UIElement` with an abstract method `render() -> str`. This method should return a string representing how the UI element is rendered.
2. **Concrete Products:**
   * `WindowsButton`: Implements `render()`, returning `"Rendering a Windows Button."`.
   * `MacOSButton`: Implements `render()`, returning `"Rendering a MacOS Button."`.
   * `LinuxButton`: Implements `render()`, returning `"Rendering a Linux Button."`.
3. **Creator (Abstract):**
   * Define an abstract class `UIElementCreator` with:
     * An abstract **factory method** `create_button() -> UIElement`. This method will be overridden by subclasses to create specific button types.
     * A concrete (non-abstract) method `display_dialog() -> str`. This method should encapsulate the client-side logic: it calls `create_button()` to get a `UIElement` object and then calls `render()` on that object. This method should return a string like `"Displaying dialog with: [Button Render Output]"`.
4. **Concrete Creators:**
   * `WindowsCreator`: Overrides `create_button()` to return a `WindowsButton`.
   * `MacOSCreator`: Overrides `create_button()` to return a `MacOSButton`.
   * `LinuxCreator`: Overrides `create_button()` to return a `LinuxButton`.

## 💡 Hints:

* Remember to use `abc.ABC` and `@abstractmethod` for your abstract classes and methods.
* Focus on how the `display_dialog()` method in the abstract `UIElementCreator` uses the `create_button()` factory method without knowing the concrete button type. This is the essence of the pattern's decoupling.

Good luck!
